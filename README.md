# 🐍 Python Automation Suite with Pytest

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pytest](https://img.shields.io/badge/pytest-%23ffffff.svg?style=for-the-badge&logo=pytest&logoColor=white&color=0A9EDC)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E3.svg?style=for-the-badge&logo=githubactions&logoColor=white)

## 📋 Project Overview
This repository showcases a professional automation framework built with **Python** and **Pytest**. It is designed for scalable end-to-end testing, featuring clean code practices, modular configuration, and automated execution through CI/CD pipelines.

## 🚀 Key Features
- **Modular Design:** Utilizes `conftest.py` for shared fixtures and reusable test logic.
- **CI/CD Integration:** Automated test execution via **GitHub Actions** on every push or pull request.
- **Reporting:** Integrated with detailed test logging and status reporting.
- **Cross-Platform:** Designed to run seamlessly across different environments.

## 🛠 Tech Stack
- **Development OS:** Windows
- **CI/CD OS:** Ubuntu (Latest) 🐧
- **Language:** Python 3.x
- **Testing Framework:** Pytest
- **Web Automation:** Playwright (Chromium) 🎭
- **CI/CD:** GitHub Actions

## 🔧 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone ```

2. **Create a virtual environment (Recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## 🧪 Running Tests
Execute all tests:
```bash
pytest -v
```
Run specific test files:
```bash
pytest tests/test_example.py
```

## 🤖 CI/CD Workflow
The project includes a GitHub Action workflow that automatically triggers on push to the main branch.

It performs the following steps:

- **Environment Setup:** Configures Python 3.x runner.

- **Dependency Management:** Installs all required packages from requirements.txt.

- **Automated Testing:** Executes the full test suite using Pytest.

- **Status Reporting:** Provides immediate feedback on build stability directly within GitHub.

## 📊 Reporting & Analytics
The suite generates a detailed **HTML Report** after each execution, including:
- **Test Summary:** Total execution time, pass/fail ratio, and environment metadata.
- **Detailed Logs:** Step-by-step breakdown of every test scenario.
- **Data-Driven Insights:** Clear visualization of parametrized test cases (e.g., multiple login credentials).

**To generate the report locally:**
```bash
pytest --html=reportes/report.html --self-contained-html
```
