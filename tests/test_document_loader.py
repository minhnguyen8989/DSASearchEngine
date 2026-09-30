from src.document_loader import load_documents


def test_load_documents_reads_text_files(tmp_path):
    document = tmp_path / "python.txt"
    document.write_text(
        "Python data structures",
        encoding="utf-8"
    )

    documents = load_documents(tmp_path)

    assert documents == {
        "python.txt": "Python data structures"
    }