import shutil
import subprocess


def main():
    # 1. Check for uv
    if not shutil.which("uv"):
        print(
            "❌ 'uv' tool not found. Please install it: curl -LsSf https://astral.sh/uv/install.sh | sh"
        )
        return

    print("🚀 Initializing environment with uv...")

    # 2. Run sync
    # check=True will raise an error if it fails
    subprocess.run(["uv", "sync"], check=True)

    print("✅ Done! Activate with: source .venv/bin/activate")


if __name__ == "__main__":
    main()
