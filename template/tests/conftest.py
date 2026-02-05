import pytest
from pytest import MonkeyPatch


@pytest.fixture(autouse=True)
def mock_env_vars(monkeypatch: MonkeyPatch) -> None:
    """
    Mock environment variables for all tests.
    monkeypatch ensures these are reset after tests finish.
    """
    monkeypatch.setenv("ENVIRONMENT", "local")
