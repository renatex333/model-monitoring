# Data Versioning and Pipelines in Machine Learning

Effective data management is crucial, but equally important is ensuring that each step in a machine learning project is executed in a well-defined sequence. This sequential flow creates a structured and reproducible pipeline that enhances both project consistency and reliability.

![Directed Acyclic Graph](img/dag.png)
*Directed Acyclic Graph (DAG) exemplifying a ML Pipeline.*

In DVC, each step in this pipeline, represented as a node in a Directed Acyclic Graph (DAG), is referred to as a **stage**. Stages are responsible for processing data and executing code, producing outputs such as trained models, transformed datasets, or other relevant artifacts.

Stages are connected through dependencies, where the output of one stage serves as the input for the next. By defining these dependencies, DVC forms an interconnected and organized pipeline, enabling a smooth and traceable flow of data and transformations from one stage to the next. This setup ensures the repeatability of the entire ML workflow, making it easier to manage, debug, and reproduce results.

## Data Version Control (DVC)

DVC is an open-source version control system designed specifically for machine learning projects, providing a Git-like experience for managing data, models, and experiments. While Git is optimized for code versioning, DVC efficiently handles large datasets and seamlessly integrates with existing workflows.

### Installing DVC

To get started with DVC, install it via pip, with support for S3:

```bash
pip install "dvc[s3]"
```

Initialize DVC in your repository:

```bash
dvc init
```

### Managing Data with DVC

DVC simplifies the process of downloading and tracking datasets. For example, to download data to the path `data/bank.csv`, use:

```bash
dvc get-url <url> data/bank.csv
```

### Creating a Pipeline with DVC

A DVC pipeline is a sequence of **stages** (tasks) that are connected by dependencies, where the output of one stage becomes the input for another. Each stage represents a step in the ML workflow, such as data preprocessing or model training.

#### Step 1: Adding a Preprocessing Stage

Let's start by creating a preprocessing stage. This stage uses the script `src/preproc.py`, which processes `data/bank.csv` to produce `data/bank_preproc.parquet`. To define this stage, run:

```bash
dvc stage add --name preproc --deps src/preproc.py --deps data/bank.csv --outs data/bank_preproc.parquet python3 src/preproc.py
```

This command creates a `dvc.yaml` file at the repository’s root, containing the pipeline information. You can either edit this YAML file directly to manage the pipeline stages or continue using terminal commands like `dvc stage add`.

To run the pipeline and execute the `preproc` stage:

```bash
dvc repro
```

#### Step 2: Adding a Training Stage

Now, let’s add a training stage. This stage relies on `data/bank_preproc.parquet` (produced by the preprocessing stage) and `src/train.py`. The outputs from this stage include:
- `models/model.pickle`
- `models/ohe.pickle`
- `results/confusion_matrix.png`
- `results/model_test_metrics.csv`

Define the training stage by running:

```bash
dvc stage add --name train --deps src/train.py --deps data/bank_preproc.parquet --outs models/model.pickle --outs models/ohe.pickle --outs results/confusion_matrix.png --outs results/model_test_metrics.csv python3 src/train.py
```

Then, run the entire pipeline, including the training stage:

```bash
dvc repro
```

### Pipeline Dependency Management

DVC’s dependency tracking ensures that each stage only runs when necessary:
- If the `preproc` stage is modified, it will be rerun along with the `train` stage, which depends on its output.
- If only the `train` stage is modified, then only that stage will be executed, since it does not affect any subsequent stages.

This dependency management feature allows for efficient and optimized pipeline execution.

### Viewing the Pipeline as a DAG

You can visualize the structure of your pipeline using the following command:

```bash
dvc dag
```

This displays the pipeline as a Directed Acyclic Graph (DAG), illustrating each stage and its dependencies.

### Benefits of Using DVC for Data Versioning and Pipelines

DVC combines robust data versioning with pipeline management, providing data scientists a powerful framework for executing, reproducing, and auditing experiments. With DVC, you can easily:
- Track and version datasets, models, and artifacts.
- Create pipelines that ensure reproducibility.
- Manage dependencies across multiple stages of the ML workflow, automating the re-execution of only those parts of the pipeline that require updates.

Together, these features streamline experimentation, improve collaboration, and enhance the traceability of your ML workflows.

## References

- [DVC Documentation](https://dvc.org/doc)
