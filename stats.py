def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
def sort_char_counts(char_dict):
    sorted_chars = []
    return [{"char": k, "num": v} for k, v in sorted(char_dict.items(), key=lambda item: item[1], reverse=True)]