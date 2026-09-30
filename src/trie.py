class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root

        for character in word.lower():
            if character not in current.children:
                current.children[character] = TrieNode()

            current = current.children[character]

        current.is_end_of_word = True

    def search(self, word):
        current = self.root

        for character in word.lower():
            if character not in current.children:
                return False

            current = current.children[character]

        return current.is_end_of_word

    def autocomplete(self, prefix):
        current = self.root
        prefix = prefix.lower()

        for character in prefix:
            if character not in current.children:
                return []

            current = current.children[character]

        results = []

        self._dfs(current, prefix, results)

        return results

    def _dfs(self, node, current_word, results):
        if node.is_end_of_word:
            results.append(current_word)

        for character, child_node in node.children.items():
            self._dfs(
                child_node,
                current_word + character,
                results
            )