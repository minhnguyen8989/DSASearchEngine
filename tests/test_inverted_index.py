from src.inverted_index import InvertedIndex


def test_add_document_indexes_words():
    index = InvertedIndex()

    index.add_document(
        "doc1",
        "Python data structures"
    )

    assert index.search("python") == {"doc1"}