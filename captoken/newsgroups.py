import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets


def get_newsgroups(min_chars=100):
    categories = [
        "alt.atheism",
        "talk.religion.misc",
        "comp.graphics",
        "sci.space",
    ]

    # Load in training data.
    newsgroups_train = datasets.fetch_20newsgroups(
        subset="train", categories=categories, remove=("headers", "footers", "quotes")
    )

    # Only keep examples with atleast 100 chars.
    data = [
        (x, y)
        for (x, y) in zip(newsgroups_train.data, newsgroups_train.target)
        if len(x) > min_chars
    ]
    xs, ys = [x[0] for x in data], [x[1] for x in data]

    # Do likewise with test data.
    newsgroups_test = datasets.fetch_20newsgroups(
        subset="test", categories=categories, remove=("headers", "footers", "quotes")
    )

    data_test = [
        (x, y)
        for (x, y) in zip(newsgroups_test.data, newsgroups_test.target)
        if len(x) > min_chars
    ]
    xs_test, ys_test = [x[0] for x in data_test], [x[1] for x in data_test]

    target_names = newsgroups_train.target_names

    return (xs, ys), (xs_test, ys_test), target_names


# Plotting code from https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html
def plot_feature_effects(clf, feature_names, target_names):
    # learned coefficients weighted by frequency of appearance
    average_feature_effects = clf.coef_

    for i, label in enumerate(target_names):
        top5 = np.argsort(average_feature_effects[i])[-5:][::-1]
        if i == 0:
            top = pd.DataFrame(feature_names[top5], columns=[label])
            top_indices = top5
        else:
            top[label] = feature_names[top5]
            top_indices = np.concatenate((top_indices, top5), axis=None)
    top_indices = np.unique(top_indices)
    predictive_words = feature_names[top_indices]

    # plot feature effects
    bar_size = 0.25
    padding = 0.75
    y_locs = np.arange(len(top_indices)) * (4 * bar_size + padding)

    fig, ax = plt.subplots(dpi=300)
    for i, label in enumerate(target_names):
        ax.barh(
            y_locs + (i - 2) * bar_size,
            average_feature_effects[i, top_indices],
            height=bar_size,
            label=label,
        )
    ax.set(
        yticks=y_locs,
        yticklabels=predictive_words,
        ylim=[
            0 - 4 * bar_size,
            len(top_indices) * (4 * bar_size + padding) - 4 * bar_size,
        ],
    )
    ax.legend(loc="lower right")

    ax.set_ylabel("Token")
    ax.set_xlabel("Regression coefficient")

    print("top 5 keywords per class:")
    print(top)

    return ax


# Calculate the number of spaced, spaced + capitalized,
# and unspaced + capitalized duplicates.
def calculate_duplicates(vocab, space_tok="▁"):
    spaced = []
    spaced_cap = []
    unspaced_cap = []

    for token in vocab:
        # Only use token as "base" if all lowercase, and unspaced.
        if token[0] != space_tok and token.lower() == token and len(token) > 1:
            # Find potential spaced duplicate.
            if space_tok + token in vocab:
                spaced += [space_tok + token]
            # Find potential capitalized, spaced duplicate.
            if space_tok + token[0].upper() + token[1:] in vocab:
                spaced_cap += [space_tok + token[0].upper() + token[1:]]
            # Find potential capitalized, unspaced duplicate.
            if token[0].upper() + token[1:] in vocab and token[0].isalpha():
                unspaced_cap += [token[0].upper() + token[1:]]

    # Return all identified duplicates.
    return spaced, spaced_cap, unspaced_cap
