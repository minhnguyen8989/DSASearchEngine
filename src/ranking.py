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

    heap = []

    for document_id, score in scores.items():
        heapq.heappush(
            heap,
            (score, document_id)
        )

        if len(heap) > k:
            heapq.heappop(heap)

    results = [
        (document_id, score)
        for score, document_id in heap
    ]

    results.sort(
        key=lambda item: (-item[1], item[0])
    )

    return results