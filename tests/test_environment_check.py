import platform

from src.environment_check import build_environment_message


def test_build_environment_message() -> None:
    expected_message = (
        f"Credit Risk Early Warning is running on Python {platform.python_version()}."
    )

    assert build_environment_message() == expected_message
