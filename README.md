# DSA Search Engine

A command-line search engine built with Python to demonstrate practical knowledge of **Data Structures and Algorithms (DSA)** and **Test Driven Development (TDD)**.

The project indexes text documents, supports keyword searching, ranks results, returns Top-K matches, and provides autocomplete suggestions.

## Features

- Single and multi-keyword document search
- Inverted index for efficient word lookup
- Trie-based autocomplete
- Depth First Search for prefix traversal
- Heap-based result ranking
- Top-K search results
- Text document loading
- Interactive command-line interface
- Automated testing with Pytest
- Test Driven Development using Red-Green-Refactor

## Data Structures and Algorithms

### Hash Table

The inverted index uses a Python dictionary to map words to documents.

Example:

```python
{
    "python": {"python.txt", "programming.txt"},
    "algorithms": {"algorithms.txt"}
}
```

Average dictionary lookup:

```text
O(1)
```

### Set

Sets store document IDs and prevent duplicate entries.

They are also used for multi-keyword searches through set intersection.

Example:

```text
python     → {"doc1", "doc2"}
algorithms → {"doc1", "doc3"}

Intersection → {"doc1"}
```

### Trie

A Trie stores words character by character and supports efficient prefix searches.

Example:

```text
root
 └── p
      └── y
           ├── python
           ├── pytest
           └── pytorch
```

Word insertion and exact lookup depend primarily on word length.

### Depth First Search

Autocomplete uses recursive Depth First Search to traverse Trie nodes below a matching prefix.

Example:

```text
Prefix: py

Results:
python
pytest
pytorch
```

### Heap / Priority Queue

Search results can be ranked using Python's `heapq` module.

Documents with more matching query terms receive higher scores.

Example:

```text
doc1 → Score 3
doc2 → Score 2
doc3 → Score 1
```

### Top-K Search

The project can return only the highest-ranking search results instead of displaying every match.

This demonstrates heap-based selection and priority-queue concepts.

## Test Driven Development

The project was developed using the **Red-Green-Refactor** TDD workflow.

```text
RED
Write a failing test
      ↓
GREEN
Write the minimum implementation required
to make the test pass
      ↓
REFACTOR
Improve the implementation while keeping
the test suite passing
```

Tests were written with **Pytest** before implementing major features.

The test suite includes:

- Tokenizer unit tests
- Inverted index unit tests
- Trie unit tests
- Ranking tests
- Search engine integration tests
- Document loader tests
- Command-line interface tests
- Edge-case and boundary tests

## Project Structure

```text
DSASearchEngine/
│
├── documents/
│   ├── python.txt
│   ├── algorithms.txt
│   └── java.txt
│
├── src/
│   ├── __init__.py
│   ├── document_loader.py
│   ├── inverted_index.py
│   ├── ranking.py
│   ├── search_engine.py
│   ├── tokenizer.py
│   └── trie.py
│
├── tests/
│   ├── test_document_loader.py
│   ├── test_inverted_index.py
│   ├── test_main.py
│   ├── test_ranking.py
│   ├── test_search_engine.py
│   ├── test_tokenizer.py
│   └── test_trie.py
│
├── main.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Running the Project

Clone the repository and open it in PyCharm or another Python IDE.

Create and activate a virtual environment, then install the dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

The menu provides:

```text
================================
       DSA Search Engine
================================

1. Search documents
2. Ranked search
3. Top-K search
4. Autocomplete
5. Exit
```

## Running Tests

Run all automated tests with:

```bash
python -m pytest -v
```

## Technologies

- Python
- Pytest
- Git
- GitHub
- PyCharm

## Concepts Demonstrated

- Data Structures and Algorithms
- Test Driven Development
- Unit Testing
- Integration Testing
- Hash Tables
- Sets
- Trees and Tries
- Depth First Search
- Recursion
- Heaps
- Priority Queues
- Searching
- Ranking Algorithms
- Big-O Analysis
- Object-Oriented Programming