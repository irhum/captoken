import regex as re


# Replacement function for re.sub, with the <capss> and <capse> tags.
def replace_caps_fn(m):
    # Concatenate <capss> and <capse> tags with lowercase version of matched group.
    return "<capss>" + m.group(1).lower() + "<capse>" + m.group(3)


# Main function to replace uppercase words, and insert tags.
def replace_caps(text):
    # Add a space at the beginning of the text, if it doesn't start with a space.
    if text[0] != " ":
        text = " " + text
        add_bksp_start = True
    else:
        add_bksp_start = False

    # Insert a '<bksp> ' for all words that are immediately preceded by punctuation.
    text = re.sub(r"([^\x20\w])([^\s\p{P}\p{Nd}])", r"\1<bksp> \2", text)

    # Regex pattern matching all spans on ALL CAPS text.
    pattern = "(\x20*\p{Lu}{2,}([\s\p{P}]*\p{Lu}{2,})*)([\s\p{P}])"
    # Replace all caps span with tags + lowercase
    text = re.sub(pattern, replace_caps_fn, text)

    # Replace all caps letters with <shift> + lowered version.
    text = re.sub("(\x20*[\p{Lu}])", lambda x: "<shift>" + x.group(1).lower(), text)

    if add_bksp_start:
        text = "<bksp>" + text
    return text
