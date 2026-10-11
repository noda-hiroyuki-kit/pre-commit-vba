# Copyright (c) 2026 Noda Hiroyuki
"""Tests for the authenticated Pinact runner."""
# ruff: noqa: S101, S105

import subprocess
from unittest.mock import patch

import pytest

from scripts.pinact import main


@pytest.mark.parametrize("exit_code", [0, 2, 3])
def test_pinact_exit_code_and_authentication(exit_code: int) -> None:
    """Pass the token only to Pinact and preserve its exit code."""
    with (
        patch("scripts.pinact.shutil.which", side_effect=["gh", "pinact"]),
        patch(
            "scripts.pinact.subprocess.run",
            side_effect=[
                subprocess.CompletedProcess([], 0, "test-token\n", ""),
                subprocess.CompletedProcess([], exit_code),
            ],
        ) as run,
    ):
        assert main() == exit_code
    assert run.call_args.args[0] == ["pinact", "run", "--min-age", "10"]
    assert run.call_args.kwargs["env"]["PINACT_GITHUB_TOKEN"] == "test-token"


@pytest.mark.parametrize(
    ("returncode", "stdout", "stderr"),
    [(1, "", "Not authenticated\n"), (0, "", "")],
)
def test_authentication_failure(
    returncode: int, stdout: str, stderr: str, capsys: pytest.CaptureFixture[str]
) -> None:
    """Report authentication failures without running Pinact."""
    with (
        patch("scripts.pinact.shutil.which", side_effect=["gh", "pinact"]),
        patch(
            "scripts.pinact.subprocess.run",
            return_value=subprocess.CompletedProcess([], returncode, stdout, stderr),
        ) as run,
    ):
        assert main() == 1
    run.assert_called_once()
    assert capsys.readouterr().err


def test_missing_executable(capsys: pytest.CaptureFixture[str]) -> None:
    """Report missing tools without attempting a subprocess."""
    with (
        patch("scripts.pinact.shutil.which", return_value=None),
        patch("scripts.pinact.subprocess.run") as run,
    ):
        assert main() == 1
    run.assert_not_called()
    assert "must be installed" in capsys.readouterr().err
