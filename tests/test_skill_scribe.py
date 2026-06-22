import pytest
from skill_scribe import CodeAnalysisEngine, CodeAnalysisResult

def test_fetch_latest_commit():
    engine = CodeAnalysisEngine([])
    repo_url = "https://github.com/example/repo"
    latest_commit = engine.fetch_latest_commit(repo_url)
    assert latest_commit == "latest_commit"

def test_parse_and_score_code():
    engine = CodeAnalysisEngine([])
    code = "example_code"
    results = engine.parse_and_score_code(code)
    assert isinstance(results, CodeAnalysisResult)
    assert results.score == 0.5
    assert results.metrics == {"metric1": 0.2, "metric2": 0.3}

def test_store_results_in_diagnostics_table():
    engine = CodeAnalysisEngine([])
    results = CodeAnalysisResult(0.5, {"metric1": 0.2, "metric2": 0.3})
    engine.store_results_in_diagnostics_table(results)
    # No assertion, just checking that it runs without errors

def test_analyze_code():
    engine = CodeAnalysisEngine([])
    repo_url = "https://github.com/example/repo"
    results = engine.analyze_code(repo_url)
    assert isinstance(results, CodeAnalysisResult)
    assert results.score == 0.5
    assert results.metrics == {"metric1": 0.2, "metric2": 0.3}

def test_analyze_code_with_empty_repo_url():
    engine = CodeAnalysisEngine([])
    repo_url = ""
    with pytest.raises(SystemExit):
        engine.analyze_code(repo_url)
