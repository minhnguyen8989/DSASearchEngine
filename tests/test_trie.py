from src.trie import Trie


def test_trie_finds_inserted_word():
    trie = Trie()

    trie.insert("python")

    assert trie.search("python") is True

def test_trie_rejects_unknown_word():
    trie = Trie()

    trie.insert("python")

    assert trie.search("java") is False

def test_trie_does_not_treat_prefix_as_complete_word():
    trie = Trie()

    trie.insert("python")

    assert trie.search("py") is False

def test_trie_autocomplete_returns_matching_words():
    trie = Trie()

    trie.insert("python")
    trie.insert("pytest")
    trie.insert("pytorch")
    trie.insert("java")

    result = trie.autocomplete("py")

    assert set(result) == {"python", "pytest", "pytorch"}

def test_trie_autocomplete_returns_empty_list_for_unknown_prefix():
    trie = Trie()

    trie.insert("python")
    trie.insert("pytest")

    result = trie.autocomplete("java")

    assert result == []