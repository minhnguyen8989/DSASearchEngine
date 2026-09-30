from pathlib import Path


def load_documents(directory):
    documents = {}

    directory = Path(directory)

    for file_path in directory.glob("*.txt"):
        content = file_path.read_text(encoding="utf-8")

        documents[file_path.name] = content

    return documents