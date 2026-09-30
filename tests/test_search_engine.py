from src.search_engine import SearchEngine


def test_search_engine_finds_matching_document():
    engine = SearchEngine()

    engine.add_document(
        "doc1",
        "Python data structures and algorithms"
    )

    engine.add_document(
        "doc2",
        "Java object oriented programming"
    )

    result = engine.search("python")

    assert result == {"doc1"}

def test_search_engine_finds_documents_with_all_query_words():
    engine = SearchEngine()

    engine.add_document(
        "doc1",
        "Python algorithms and data structures"
    )

    engine.add_document(
        "doc2",
        "Python programming"
    )

    engine.add_document(
        "doc3",
        "Algorithms and data structures"
    )

    result = engine.search("python algorithms")

    assert result == {"doc1"}

def test_search_engine_returns_empty_set_for_empty_query():
    engine = SearchEngine()

    engine.add_document(
        "doc1",
        "Python algorithms"
    )

    result = engine.search("")

    assert result == set()

def test_search_engine_autocomplete_returns_matching_words():
    engine = SearchEngine()

    engine.add_document(
        "doc1",
        "Python pytest pytorch"
    )

    engine.add_document(
        "doc2",
        "Java programming"
    )

    result = engine.autocomplete("py")

    assert set(result) == {
        "python",
        "pytest",
        "pytorch"
    }

def test_search_engine_returns_ranked_results():
    engine = SearchEngine()

    engine.add_document(
        "doc1",
        "Python algorithms data structures"
    )

    engine.add_document(
        "doc2",
        "Python programming"
    )

    engine.add_document(
        "doc3",
        "Algorithms data"
    )

    result = engine.search_ranked(
        "python algorithms"
    )

    assert result == [
        ("doc1", 2),
        ("doc2", 1),
        ("doc3", 1)
    ]

def test_search_engine_returns_top_k_ranked_results():
    engine = SearchEngine()

    engine.add_document(
        "doc1",
        "Python algorithms data structures"
    )

    engine.add_document(
        "doc2",
        "Python programming"
    )

    engine.add_document(
        "doc3",
        "Algorithms data"
    )

    engine.add_document(
        "doc4",
        "Python algorithms testing"
    )

    result = engine.search_top_k(
        "python algorithms",
        2
    )

    assert result == [
        ("doc1", 2),
        ("doc4", 2)
    ]

def test_search_top_k_returns_empty_list_when_k_is_zero():
    engine = SearchEngine()

    engine.add_document(
        "doc1",
        "Python algorithms"
    )

    result = engine.search_top_k(
        "python",
        0
    )

    assert result == []


def test_search_top_k_handles_k_larger_than_number_of_results():
    engine = SearchEngine()

    engine.add_document(
        "doc1",
        "Python algorithms"
    )

    engine.add_document(
        "doc2",
        "Python programming"
    )

    result = engine.search_top_k(
        "python",
        5
    )

    assert result == [
        ("doc1", 1),
        ("doc2", 1)
    ]