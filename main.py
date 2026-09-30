from src.document_loader import load_documents
from src.search_engine import SearchEngine
from pathlib import Path

def create_search_engine(directory):
    engine = SearchEngine()

    documents = load_documents(directory)

    for document_id, text in documents.items():
        engine.add_document(document_id, text)

    return engine


def display_menu():
    print("=" * 32)
    print("       DSA Search Engine")
    print("=" * 32)
    print()
    print("1. Search documents")
    print("2. Ranked search")
    print("3. Top-K search")
    print("4. Autocomplete")
    print("5. Exit")


def run_cli(engine=None):
    if engine is None:
        engine = SearchEngine()

    while True:
        display_menu()

        choice = input("Select an option: ")

        if choice == "1":
            query = input("Enter search query: ")

            results = engine.search(query)

            if results:
                print("Search results:")

                for document_id in sorted(results):
                    print(document_id)
            else:
                print("No documents found.")

        elif choice == "2":
            query = input("Enter search query: ")

            results = engine.search_ranked(query)

            if results:
                print("Ranked results:")

                for document_id, score in results:
                    print(f"{document_id} - Score: {score}")
            else:
                print("No documents found.")

        elif choice == "3":
            query = input("Enter search query: ")
            k = int(input("Enter number of results: "))

            results = engine.search_top_k(query, k)

            if results:
                print(f"Top {k} results:")

                for document_id, score in results:
                    print(f"{document_id} - Score: {score}")
            else:
                print("No documents found.")

        elif choice == "4":
            prefix = input("Enter prefix: ")

            suggestions = engine.autocomplete(prefix)

            if suggestions:
                print("Suggestions:")

                for word in sorted(suggestions):
                    print(word)
            else:
                print("No suggestions found.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

def main():
    project_directory = Path(__file__).parent
    documents_directory = project_directory / "documents"

    engine = create_search_engine(documents_directory)

    run_cli(engine)


if __name__ == "__main__":
    main()