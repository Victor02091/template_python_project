"""
Generate the code reference pages and navigation.

This script is responsible for:
1. Copying the root README.md to the docs.
2. Scanning the source code and generating virtual reference pages.
3. Copying Jupyter notebooks to the docs.
"""

from pathlib import Path

import mkdocs_gen_files

PROJECT_ROOT = Path(__file__).parent.parent
SRC_DIR = PROJECT_ROOT / "src"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
README_PATH = PROJECT_ROOT / "README.md"


def copy_readme() -> None:
    """Copies the root README.md to 'docs/readme.md'."""
    if not README_PATH.exists():
        print(f"Warning: README not found at {README_PATH}")
        return

    content = README_PATH.read_text(encoding="utf-8")

    with mkdocs_gen_files.open("readme.md", "w") as fd:
        fd.write(content)
        # Allows the "Edit this page" button to work correctly
        mkdocs_gen_files.set_edit_path("readme.md", "../README.md")


def build_reference_docs() -> None:
    """Scans src/ for .py files and generates the code reference."""
    nav = mkdocs_gen_files.Nav()

    if not SRC_DIR.exists():
        print(f"Warning: Source directory not found at {SRC_DIR}")
        return

    # 1. Iterate over all Python files
    for path in sorted(SRC_DIR.rglob("*.py")):
        module_path = path.relative_to(SRC_DIR).with_suffix("")
        doc_path = path.relative_to(SRC_DIR).with_suffix(".md")
        full_doc_path = Path("reference", doc_path)

        parts = tuple(module_path.parts)

        # Skip __main__.py
        if parts[-1] == "__main__":
            continue

        # Handle __init__.py (turn folder into a page)
        if parts[-1] == "__init__":
            parts = parts[:-1]
            doc_path = doc_path.with_name("index.md")
            full_doc_path = full_doc_path.with_name("index.md")

        # Add to Navigation
        nav[parts] = doc_path.as_posix()

        # Create the virtual markdown file with the '::: import_path' directive
        with mkdocs_gen_files.open(full_doc_path, "w") as fd:
            ident = ".".join(parts)
            fd.write(f"::: {ident}")

        mkdocs_gen_files.set_edit_path(full_doc_path, path)

    # 2. Generate the Reference Landing Page (index.md)
    # This prevents the "Reference" link in the menu from 404ing
    with mkdocs_gen_files.open("reference/index.md", "w") as fd:
        fd.write(
            "# Code Reference\n\nSelect a module from the sidebar"
            " to view details."
        )
    nav["Overview"] = "index.md"

    # 3. Write the Navigation structure to SUMMARY.md
    # This file is read by the 'literate-nav' plugin
    with mkdocs_gen_files.open("reference/SUMMARY.md", "w") as nav_file:
        nav_file.writelines(nav.build_literate_nav())


def copy_notebooks() -> None:
    """Copies all .ipynb files from notebooks/ to docs/notebooks/."""
    if not NOTEBOOKS_DIR.exists():
        return

    for nb_path in NOTEBOOKS_DIR.rglob("*.ipynb"):
        # Calculate relative path to keep folder structure
        # (e.g. notebooks/tutorial/1.ipynb)
        rel_path = nb_path.relative_to(NOTEBOOKS_DIR)
        dest_path = Path("notebooks") / rel_path

        # Read binary content
        content = nb_path.read_bytes()

        # Write to virtual docs
        with mkdocs_gen_files.open(dest_path, "wb") as fd:
            fd.write(content)


def main() -> None:
    """
    Main function to orchestrate the generation of reference docs
    and copying files.
    """
    copy_readme()
    build_reference_docs()
    copy_notebooks()


main()
