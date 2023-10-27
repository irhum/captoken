import regex as re

def replace_caps_fn(matchv):
    caps_text = matchv.group(0).lower()
    if len(caps_text.strip()) > 1:
        text_len = len(caps_text.rstrip())
        return f"<CAPSS>{caps_text[:text_len]}<CAPSE>{caps_text[text_len:]}"
    else:
        return f"<SHIFT>{caps_text}"

def replace_caps(text):
    if text[0] != ' ': text = ' ' + text
    text = re.sub(r'([^\x20\w])([^\s\p{P}])', r'\1<bksp> \2', text)
    pattern = u'\x20*(\p{Lu}+[\s\p{P}\p{Lu}]*)+'

    result = re.sub(pattern, replace_caps_fn, text)
    return result