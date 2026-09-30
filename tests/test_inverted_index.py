from src.inverted_index import InvertedIndex


def test_add_document_indexes_words():
    index = InvertedIndex()

    index.add_document(
        "doc1",
        "Python data structures"
    )

    assert index.search("python") == {"doc1"}

def test_same_word_can_exist_in_multiple_documents():
    index = InvertedIndex()

    index.add_document(
        "doc1",
        "Python programming"
    )

    index.add_document(
        "doc2",
        "Python algorithms"
    )

    result = index.search("python")

    assert result == {"doc1", "doc2"}

def test_repeated_word_does_not_duplicate_document():
    index = InvertedIndex()

    index.add_document(
        "doc1",
        "Python Python Python"
    )

    result = index.search("python")

    assert result == {"doc1"}

def test_search_all_returns_documents_containing_all_words():
    index = InvertedIndex()

    index.add_document(
        "doc1",
        "Python algorithms data"
    )

    index.add_document(
        "doc2",
        "Python programming"
    )

    index.add_document(
        "doc3",
        "Algorithms data structures"
    )

    result = index.search_all(
        ["python", "algorithms"]
    )

    assert result == {"doc1"}

def test_search_all_returns_empty_set_when_word_not_found():
    index = InvertedIndex()

    index.add_document(
        "doc1",
        "Python algorithms"
    )

    result = index.search_all(
        ["python", "java"]
    )

    assert result == set()