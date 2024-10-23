# Documentation in Machine Learning Projects

## Overview

In machine learning (ML) projects, proper documentation plays a crucial role in ensuring that data scientists and other team members can efficiently apply various ML methods and understand software systems, such as APIs in LightGBM or TensorFlow. Documentation serves as a guide to communicate software functionality and is essential for efficient development and collaboration.

## Importance of Documentation

Good documentation ensures that:
- **Users comprehend software functionality**: Whether it's an API or complex model training, clear documentation is essential for understanding how to use the tools effectively.
- **Software is transferable**: High turnover in data teams is common, and documentation helps ensure that knowledge about the software remains within the company, not just with the individuals who built it.
- **Collaboration is smooth**: Multiple people can work on ongoing projects, and good documentation facilitates this transition.

### Tailoring Documentation to the Audience

- **Less Knowledgeable Customers**: Focus on tutorial-style content, diagrams, and glossaries to introduce new concepts and make the product approachable.
- **Experienced Customers**: Provide more advanced examples and real-world scenarios to maximize the use of your product.

## Types of Documentation

### External Documentation

External documentation involves conveying information independent of the specific technologies used in the project, often in formats like Microsoft Office documents. 

- **Advantages**: Flexibility in choosing the format and tools.
- **Disadvantages**: Difficult to maintain up-to-date with the latest software version and prone to being lost or outdated.

**Tip!** Managers are not programmers! Tailor documentation to be understandable and accessible for non-technical stakeholders.

## Sphinx for Documentation

To generate and maintain high-quality documentation for ML projects, we will use **Sphinx**. Sphinx is a powerful documentation generator that allows you to create professional-grade documentation.

### Sphinx Basic Usage

## Usage

To install Sphinx, activate your virtual environment and run the following command:

```bash
pip install sphinx==7.2.6
```

Then, create a `docs` folder:

```bash
mkdir docs
cd docs
```

Quickstart the documentation with the following command:

```bash
sphinx-quickstart
```

### Configuration Details:
- **Project name**: MLearning
- **Author name(s)**: Your name!
- **Project release**: 0.0.1

Leave the rest of the settings as the default.

To generate the initial structure and build your documentation, run:

```bash
make html
```

If you're on Windows, run the `make.bat` script instead:

```bash
./make.bat html
```

Open the `_build/html/index.html` file to see the first version of your documentation.

### Enable Automatic Documentation Generation

Sphinx’s `autodoc` feature allows automatic extraction of docstrings from Python code. To enable this, follow these steps:

1. In the `docs/conf.py` file, replace the `extensions = []` line with:

```python
import sys
import os

sys.path.insert(0, os.path.abspath("../src"))

extensions = ["sphinx.ext.autodoc"]
```

2. In the `docs` folder, run the command to create reStructuredText for the Python modules.

3. Rebuild the documentation:

```bash
make html
```

### Viewing the Generated Documentation

Open the `_build/html/index.html` file to see the generated documentation.


## References

- [Sphinx Documentation](https://www.sphinx-doc.org/en/master/)

- [Comments in code: best practices and 4 mistakes to avoid](https://swimm.io/learn/code-collaboration/comments-in-code-best-practices-and-mistakes-to-avoid)