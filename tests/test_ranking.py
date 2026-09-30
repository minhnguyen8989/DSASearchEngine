from src.ranking import rank_results, top_k_results


def test_rank_results_returns_highest_score_first():
    scores = {
        "doc1": 3,
        "doc2": 7,
        "doc3": 5
    }

    result = rank_results(scores)

    assert result[0] == ("doc2", 7)

def test_rank_results_orders_all_documents_by_score():
    scores = {
        "doc1": 3,
        "doc2": 7,
        "doc3": 5
    }

    result = rank_results(scores)

    assert result == [
        ("doc2", 7),
        ("doc3", 5),
        ("doc1", 3)
    ]

def test_top_k_results_returns_best_documents():
    scores = {
        "doc1": 3,
        "doc2": 7,
        "doc3": 5,
        "doc4": 9
    }

    result = top_k_results(scores, 2)

    assert result == [
        ("doc4", 9),
        ("doc2", 7)
    ]