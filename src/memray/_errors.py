from typing import Any


class PensieveError(Exception):
    """Exceptions raised in this package."""


class PensieveCommandError(PensieveError):
    """Exceptions raised from this package's CLI commands."""

    def __init__(self, *args: Any, exit_code: int) -> None:
        super().__init__(*args)
        self.exit_code = exit_code
