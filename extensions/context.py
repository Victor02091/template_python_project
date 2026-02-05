import subprocess
from pathlib import Path

from jinja2.ext import Extension


class GitInfoExtension(Extension):
    """
    Jinja2 extension to retrieve git user and email from the system configuration.
    """

    def __init__(self, environment):
        super().__init__(environment)

        # Add variables to the Jinja context
        environment.globals["git_user_name"] = self._get_git_config("user.name")
        environment.globals["git_user_email"] = self._get_git_config("user.email")
        environment.globals["current_folder_name"] = Path.cwd().name

    def _get_git_config(self, key):
        """Run git config command to get values."""
        try:
            # Run git config --get <key>
            # capture_output=True and text=True are standard in Py 3.7+
            result = subprocess.run(
                ["git", "config", "--get", key],
                capture_output=True,
                text=True,
                check=True,
            )
            return result.stdout.strip()
        except (subprocess.CalledProcessError, FileNotFoundError):
            # Fallback if git is not installed or config is missing
            return None
