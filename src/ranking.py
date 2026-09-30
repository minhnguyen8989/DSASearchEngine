import heapq


def rank_results(scores):
    heap = []

    for document_id, score in scores.items():
        heapq.heappush(
            heap,
            (-score, document_id)
        )

    ranked_results = []

    while heap:
        negative_score, document_id = heapq.heappop(heap)

        ranked_results.append(
            (document_id, -negative_score)
        )

    return ranked_results


def top_k_results(scores, k):
    if k <= 0:
        return []

    if not scores:
        return []

    best_results = heapq.nsmallest(
        k,
        scores.items(),
        key=lambda item: (-item[1], item[0])
    )

    return [
        (document_id, score)
        for document_id, score in best_results
    ]