from main import display_menu, run_cli, create_search_engine
from src.search_engine import SearchEngine

def test_display_menu_shows_available_options(capsys):
    display_menu()

    output = capsys.readouterr().out

    assert "DSA Search Engine" in output
    assert "1. Search documents" in output
    assert "2. Ranked search" in output
    assert "3. Top-K search" in output
    assert "4. Autocomplete" in output
    assert "5. Exit" in output

def test_run_cli_exits_when_user_selects_five(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "5")

    run_cli()

    output = capsys.readouterr().out

    assert "Goodbye!" in output

def test_run_cli_handles_invalid_option(monkeypatch, capsys):
    user_inputs = iter(["9", "5"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(user_inputs)
    )

    run_cli()

    output = capsys.readouterr().out

    assert "Invalid option. Please try again." in output

def test_run_cli_searches_documents(monkeypatch, capsys):
    engine = SearchEngine()

    engine.add_document(
        "doc1",
        "Python data structures"
    )

    engine.add_document(
        "doc2",
        "Java programming"
    )

    user_inputs = iter([
        "1",
        "python",
        "5"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(user_inputs)
    )

    run_cli(engine)

    output = capsys.readouterr().out

    assert "doc1" in output

def test_run_cli_performs_ranked_search(monkeypatch, capsys):
    engine = SearchEngine()

    engine.add_document(
        "doc1",
        "Python algorithms data"
    )

    engine.add_document(
        "doc2",
        "Python programming"
    )

    user_inputs = iter([
        "2",
        "python algorithms",
        "5"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(user_inputs)
    )

    run_cli(engine)

    output = capsys.readouterr().out

    assert "doc1 - Score: 2" in output
    assert "doc2 - Score: 1" in output

def test_run_cli_performs_top_k_search(monkeypatch, capsys):
    engine = SearchEngine()

    engine.add_document(
        "doc1",
        "Python algorithms data"
    )

    engine.add_document(
        "doc2",
        "Python programming"
    )

    engine.add_document(
        "doc3",
        "Algorithms data structures"
    )

    user_inputs = iter([
        "3",
        "python algorithms",
        "2",
        "5"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(user_inputs)
    )

    run_cli(engine)

    output = capsys.readouterr().out

    assert "doc1 - Score: 2" in output
    assert "doc2 - Score: 1" in output

def test_run_cli_performs_autocomplete(monkeypatch, capsys):
    engine = SearchEngine()

    engine.add_document(
        "doc1",
        "Python pytest pytorch"
    )

    engine.add_document(
        "doc2",
        "Java programming"
    )

    user_inputs = iter([
        "4",
        "py",
        "5"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(user_inputs)
    )

    run_cli(engine)

    output = capsys.readouterr().out

    assert "python" in output
    assert "pytest" in output
    assert "pytorch" in output

def test_create_search_engine_loads_documents(tmp_path):
    document = tmp_path / "python.txt"
    document.write_text(
        "Python data structures",
        encoding="utf-8"
    )

    engine = create_search_engine(tmp_path)

    result = engine.search("python")

    assert result == {"python.txt"}

def test_main_creates_engine_and_runs_cli(monkeypatch):
    calls = {
        "create_search_engine": False,
        "run_cli": False
    }

    fake_engine = object()

    def fake_create_search_engine(directory):
        calls["create_search_engine"] = True
        return fake_engine

    def fake_run_cli(engine):
        assert engine is fake_engine
        calls["run_cli"] = True

    monkeypatch.setattr(
        "main.create_search_engine",
        fake_create_search_engine
    )

    monkeypatch.setattr(
        "main.run_cli",
        fake_run_cli
    )

    from main import main

    main()

    assert calls["create_search_engine"] is True
    assert calls["run_cli"] is True