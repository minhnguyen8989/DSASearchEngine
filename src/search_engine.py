from src.inverted_index import InvertedIndex
from src.ranking import rank_results, top_k_results
from src.tokenizer import tokenize
from src.trie import Trie


class SearchEngine:
    def __init__(self):
        self.index = InvertedIndex()
        self.trie = Trie()

    def add_document(self, document_id, text):
        self.index.add_document(document_id, text)

        words = tokenize(text)

        for word in words:
            self.trie.insert(word)

    def search(self, query):
        words = tokenize(query)

        if not words:
            return set()

        if len(words) == 1:
            return self.index.search(words[0])

        return self.index.search_all(words)

    def autocomplete(self, prefix):
        return self.trie.autocomplete(prefix)

    def search_ranked(self, query):
        words = tokenize(query)

        if not words:
            return []

        scores = self._calculate_scores(words)

        return rank_results(scores)

    def search_top_k(self, query, k):
        words = tokenize(query)

        if not words:
            return []

        scores = self._calculate_scores(words)

        return top_k_results(scores, k)

    def _calculate_scores(self, words):
        scores = {}

        for word in words:
            matching_documents = self.index.search(word)

            for document_id in matching_documents:
                scores[document_id] = scores.get(document_id, 0) + 1

        return scores