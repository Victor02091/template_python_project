# Modern Python Project Template

A production-ready Python project template powered by **uv**.

This template provides a batteries-included setup with modern tooling, strict linting, automatic formatting, and CI/CD integration, all configured to work out of the box.

## ✨ Features

* **Package Manager:** [uv](https://github.com/astral-sh/uv) (blazing fast replacement for pip/poetry).
* **Linter & Formatter:** [Ruff](https://github.com/astral-sh/ruff) (configured for strict imports and formatting).
* **Pre-commit:** Automatic hooks to ensure code quality before every commit (optional).
* **Testing:** Pytest with configuration ready.
* **CI/CD:** GitLab CI pipeline (optional).
* **Containerization:** Dockerfile included (optional).
* **Editor:** VS Code settings (extensions, tests, and linting) pre-configured.

## 🛠️ Requirements

You **do not** need to install Python manually. The package manager `uv` handles Python versions automatically.

You only need:
1.  **Git**
2.  **uv**

### How to install uv

**On Linux / macOS:**

    curl -LsSf https://astral.sh/uv/install.sh | sh

**On Windows:**

    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

*More info on the [official website](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_1).*

## 📦 Installation

This template is built with **Copier**. You can install Copier globally using `uv` (recommended).

**Important:** This template uses custom extensions. You must install Copier with the `copier-template-extensions` plugin.

    uv tool install copier --with copier-template-extensions

## 🚀 Usage

To generate a new project from this template, run the following command in your terminal:

    copier copy --trust https://bitbucket.org/faelfassi/python_project_mpdata_template.git $(pwd)

### Updating an existing project
If you have already generated a project and want to pull the latest updates from the template:

    copier update --trust