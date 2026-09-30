from src.tokenizer import tokenize


def test_tokenize_converts_text_to_lowercase():
    result = tokenize("Python Programming")

    assert result == ["python", "programming"]

def test_tokenize_removes_punctuation():
    result = tokenize("Python, Java!")

    assert result == ["python", "java"]

def test_tokenize_handles_extra_whitespace():
    result = tokenize("Python    Data   Structures")

    assert result == ["python", "data", "structures"]

def test_tokenize_separates_words_connected_by_punctuation():
    result = tokenize("Data-Structures and Algorithms")

    assert result == ["data", "structures", "and", "algorithms"]