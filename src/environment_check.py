import platform


def build_environment_message() -> str:
    """Build a message that identifies the project and Python version."""
    return f"Credit Risk Early Warning is running on Python {platform.python_version()}."


if __name__ == "__main__":
    print(build_environment_message())
