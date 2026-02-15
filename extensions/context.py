import subprocess
from pathlib import Path

from jinja2.ext import Extension


class GitInfoExtension(Extension):
    """
    Jinja2 extension to retrieve git user, email, and remote URL.
    """

    def __init__(self, environment):
        super().__init__(environment)

        # 1. User Info
        environment.globals["git_user_name"] = self._get_git_config("user.name")
        environment.globals["git_user_email"] = self._get_git_config("user.email")
        environment.globals["current_folder_name"] = Path.cwd().name

        # 2. Remote Repository Info
        remote_url = self._get_git_config("remote.origin.url")
        web_url = self._parse_git_url(remote_url)

        environment.globals["git_remote_url"] = web_url
        environment.globals["git_repo_name"] = (
            web_url.split("/")[-1] if web_url else None
        )

    def _get_git_config(self, key):
        """Run git config command to get values."""
        try:
            result = subprocess.run(
                ["git", "config", "--get", key],
                capture_output=True,
                text=True,
            )
            val = result.stdout.strip()
            return val if val else None
        except (subprocess.CalledProcessError, FileNotFoundError):
            return None

    def _parse_git_url(self, url):
        """Converts SSH or Git URLs to HTTPS web URLs."""
        if not url:
            return None

        # Clean whitespace
        url = url.strip()

        # Handle SSH (git@github.com:user/repo.git) -> https://github.com/user/repo
        if url.startswith("git@"):
            url = url.replace(":", "/")
            url = url.replace("git@", "https://")

        # Handle SSH with protocol (ssh://git@github.com/...)
        elif url.startswith("ssh://"):
            url = url.replace("ssh://git@", "https://")

        # Remove .git suffix if present
        if url.endswith(".git"):
            url = url[:-4]

        return url
