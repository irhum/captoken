Tokenizers will tokenize capitalized versions of words differently than lowercased ones ("Hello" does not share its representation with "hello"). This results in a fair amount of redundancy in a tokenizer.

At its core, a language model is simply a model of humans pressing a keyboard. What if we took that literally, and "placed in" the SHIFT and Caps Lock button presses needed to produce text? That way, capitalization could be represented *seperately* from the words themselves.

We do this with four specialized tokens \<shift>, \<capss>, \<capse> and \<bksp> (which are always tokenized as whole, never broken) to absorb this syntactic information, leaving all the other words lowercased.

### Current Status
There are four self contained notebooks in this repository, inside `notebooks`:

1. `GPT2 Tokenizer.ipynb` - contains baseline experiments on the GPT-2 tokenizer, to quantify the number of redundant tokens.
2. `Train Tokenizer` - This trains the two 16k vocabulary SentencePiece tokenizers on the Wikipedia dataset.
3. `Newsgroups.ipynb` - This (and the `Caps` variant) performs the experiments and plots using the two trained tokenizers.