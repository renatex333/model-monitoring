# ML Project Essentials: Documentation, Logging, Monitoring, Tracking and Data Management

This repository brings together practical tutorials and examples covering essential practices for building robust and maintainable Machine Learning systems. It focuses on five key pillars: efficient documentation, comprehensive logging, continual model monitoring, centralized experiment/data tracking, and uncomplicated data management.

## Overview

In modern Machine Learning workflows, simply building a model is not enough. Ensuring reproducibility, facilitating collaboration, debugging issues efficiently, monitoring performance degradation, and managing both experiments and data are crucial for success. This repository provides foundational knowledge and hands-on examples in:
- **Documentation:** Ensuring clarity, transferability, and ease of use for ML systems.
- **Logging:** Enabling effective debugging, tracking execution, and monitoring system health.
- **Monitoring:** Guaranteeing models remain performant and relevant in production by tracking resources, metrics, and data drift.
- **Tracking:** Managing experiment parameters, models, artifacts, and training metrics for reproducibility and consistency using MLflow.
- **Data Management:** Managing datasets, dealing with different storages, and automating preprocessing tasks using DVC.

## Included Tutorials

Below is an overview of the tutorials included in this repository:

* **[documentation-tutorial](./documentation-tutorial/)**: Learn the importance of documentation in ML for clarity, knowledge transfer, and collaboration. This tutorial covers different documentation types and guides you through using Sphinx to generate professional documentation automatically from your Python code and docstrings, including setup and basic usage.

* **[logging-tutorial](./logging-tutorial/)**: Understand the vital role of logging in ML for tracking execution, debugging, and monitoring production systems. This tutorial covers why logging is crucial for feedback loops and introduces Python's `logging` library, explaining how to use different logging levels (DEBUG, INFO, WARNING, etc.) effectively.

* **[ml-model-monitoring](./ml-model-monitoring/)**: Delve into the critical aspects of monitoring deployed ML models. This project covers monitoring model performance using key metrics for classification and regression. Explore concepts like ground truth evaluation and the importance of detecting data/input drift to ensure models remain effective.

* **[tracking-tutorial](./tracking-tutorial/)**: Explore essential techniques for tracking and managing ML experiments with MLflow, such as logging parameters, metrics, and artifacts, providing an easy way to monitor and track ML experiments with minimal changes to your existing code.

* **[ml-data-management](./ml-data-management/)**: This tutorial covers comparing data formats for efficiency, using DVC (Data Version Control) for versioning datasets and building reproducible pipelines.
