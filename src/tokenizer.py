import string


def tokenize(text):
    punctuation_to_spaces = str.maketrans(
        string.punctuation,
        " " * len(string.punctuation)
    )

    cleaned_text = text.translate(punctuation_to_spaces)

    return cleaned_text.lower().split()