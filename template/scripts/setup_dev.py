import shutil
import subprocess
import sys


def main():
    # 1. Check if 'uv' is installed
    uv_path = shutil.which("uv")
    if not uv_path:
        print("⚠️  'uv' is not installed. Skipping dependency installation.")
        print("ℹ️  Install it later: curl -LsSf https://astral.sh/uv/install.sh | sh")
        return

    print("🚀 Initializing environment with uv...")

    try:
        # 2. Run uv sync (shell=False is safer cross-platform)
        subprocess.run(["uv", "sync"], check=True, shell=False)
        print("✅ Dependencies installed successfully!")
        print(
            "👉 Activate with: source .venv/bin/activate (Mac/Linux) or .venv\\Scripts\\activate (Win)"
        )
    except subprocess.CalledProcessError:
        print("❌ 'uv sync' failed. Please check your pyproject.toml.")
        sys.exit(1)


if __name__ == "__main__":
    main()
