Tokenizers will tokenize capitalized versions of words differently than lowercased ones ("Hello" does not share its representation with "hello"). This results in a fair amount of redundancy in a tokenizer.

At its core, a language model is simply a model of humans pressing a keyboard. What if we took that literally, and "placed in" the SHIFT and Caps Lock button presses needed to produce text? That way, capitalization could be represented *seperately* from the words themselves.

We do this with four specialized tokens \<SHIFT>, \<CAPSS>, \<CAPSE> and \<bksp> (which are always tokenized as whole, never broken) to absorb this syntactic information, leaving all the other words lowercased.