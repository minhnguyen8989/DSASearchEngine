from src.tokenizer import tokenize

class InvertedIndex:
    def __init__(self):
        self.index = {}

    def add_document(self, document_id, text):
        words = tokenize(text)

        for word in words:
            if word not in self.index:
                self.index[word] = set()

            self.index[word].add(document_id)

    def search(self, word):
        return self.index.get(word.lower(), set())