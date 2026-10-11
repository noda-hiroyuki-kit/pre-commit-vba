# Copyright (c) 2026 Noda Hiroyuki
"""Run Pinact with GitHub CLI authentication."""

import os
import shutil
import subprocess
import sys


def main() -> int:
    """Authenticate Pinact and return its exit code."""
    gh = shutil.which("gh")
    pinact = shutil.which("pinact")
    if gh is None or pinact is None:
        sys.stderr.write("GitHub CLI and Pinact must be installed and on PATH.\n")
        return 1

    auth = subprocess.run(  # noqa: S603
        [gh, "auth", "token"], capture_output=True, text=True, check=False
    )
    if auth.returncode != 0:
        sys.stderr.write("Failed to obtain GitHub CLI authentication.\n")
        sys.stderr.write(auth.stderr)
        return auth.returncode
    token = auth.stdout.strip()
    if not token:
        sys.stderr.write("GitHub CLI returned an empty authentication token.\n")
        return 1

    result = subprocess.run(  # noqa: S603
        [pinact, "run", "--min-age", "10", "--update"],
        env=dict(os.environ, PINACT_GITHUB_TOKEN=token),
        check=False,
    )
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
