# Data Versioning in Machine Learning

Managing data is a crucial part of every machine learning (ML) project lifecycle. In addition to source code and experiment results, ensuring that data is versioned correctly is key to reproducibility, traceability, and scalability.

## Importance of Data in ML

A well-known phrase in the ML field highlights the importance of data:

> "More data beats clever algorithms, but better data beats more data."

This phrase underscores the significant impact that high-quality data can have on a model’s performance. In ML projects, it's not just about finding the most revolutionary methods—sometimes, improving the data itself through feature engineering or acquiring more relevant data can lead to the most substantial performance gains.

However, we rarely start with the best version of our data. Just as we iterate on model parameters and algorithms, we must also iterate on the data itself: adding new features, gathering more data, and exploring new data sources. With the growing complexity of data and experiments, keeping track of these changes becomes difficult. 

This is where **data versioning** comes in, and tools like **DVC (Data Version Control)** help manage large datasets and track changes effectively throughout the project.

## Data Version Control (DVC)

DVC is an open-source version control system for machine learning projects, offering a Git-like experience for managing data, models, and experiments. Unlike Git, which is optimized for versioning code, DVC handles large datasets efficiently and integrates seamlessly with existing workflows.

### Why Not Use Git for Data Versioning?

While it's possible to version datasets (like CSV or Parquet files) with Git, it's not ideal. Git is designed for text-based files and does not offer efficient storage or versioning for large binary files like datasets. DVC provides a more suitable solution for data-heavy projects, allowing for efficient data tracking without bloating your Git repository.

### Installing DVC

To start using DVC, install it via pip with support for S3:

```bash
pip install "dvc[s3]"
```

Initialize DVC in your repository:

```bash
dvc init
```

### Managing Data with DVC

Download and track datasets easily with DVC. In this example, the destination path is `data/data.csv`:

```bash
dvc get-url <url> data/data.csv
```

After adding the data, track it with DVC:

```bash
dvc add data/data.csv
```

After adding data, commit the tracking file:

```bash
git add data/data.csv.dvc data/.gitignore
git commit -m "Track data.csv with DVC"
git push
```

Only the tracking file goes to GitHub—not the actual data, ensuring your repository stays lightweight.

### Remote Storage with DVC

DVC supports remote storage solutions such as local folders, S3 buckets, and more. To configure a local folder as remote storage:

```bash
mkdir /home/user/dvcstore
dvc remote add -d myremote /home/user/dvcstore
```

Upload your data to the remote storage:

```bash
dvc push
```

#### Restoring Data

To restore deleted data from your remote storage, run:

```bash
dvc pull
```

### Versioning with Git and DVC

One of the key advantages of using DVC is its seamless integration with Git, allowing you to version both your source code and datasets together. This ensures that each version of your model is tied to the exact version of the data used, making it easier to reproduce results and maintain the project’s history.

Just as you would version your code with Git, you can also manage data versioning with DVC. Here’s how to do it:

1. **Tagging Your Versions**:  
   Use Git tags to label different stages of your project. For example, you can tag a version when you're ready to release or when you've made a significant change to your model or data:

    ```bash
    git tag -a v0.0.0 -m "Release version 0.0.0"
    ```

2. **Modifying Data and Committing Changes**:  
   After updating your data (e.g., adding new data or making modifications), use DVC to commit the changes. This ensures that the new version of the data is tracked while keeping your Git repository lightweight:

    ```bash
    dvc commit data/data.csv
    dvc push
    ```

3. **Committing Changes to Source Code**:  
   As with any Git workflow, commit your source code changes alongside the data:

    ```bash
    git add .
    git commit -m "Updated model and data for version 1"
    git push
    ```

4. **Creating a New Tag for the Updated Version**:  
   Once the code and data are pushed, create a new tag to mark this version:

    ```bash
    git tag -a v0.0.1 -m "Release version 0.0.1"
    ```

5. **Switching Between Versions**:  
   With Git and DVC working together, you can easily switch between different versions of your project. When checking out a previous Git tag, DVC will automatically sync the corresponding data version as well:

    ```bash
    git checkout v0.0.0
    dvc checkout  # Restores the data associated with this version

    git checkout v0.0.1
    dvc checkout  # Syncs the data for the newer version
    ```

By using this approach, you can maintain version control over both your code and data, ensuring that your entire machine learning pipeline is reproducible. DVC enables you to treat data like code, making it easy to collaborate on large datasets without overwhelming Git with heavy files.

## Using DVC with S3

DVC can be configured to use an Amazon S3 bucket for storing data, which provides scalability, durability, and facilitates collaboration across data science teams.

1. **Create an S3 bucket**:  
   First, create an S3 bucket using the AWS CLI:

    ```bash
    export AWS_PROFILE=mlops

    aws s3api create-bucket --bucket <your-s3-bucket-name> --region <your-region> --create-bucket-configuration LocationConstraint=<your-region>
    ```

2. **Configure DVC to use the S3 bucket as remote storage**:  
   Set up DVC to use your S3 bucket as the default remote storage for data and models:

    ```bash
    dvc remote add myremote s3://<your-s3-bucket-name>
    dvc remote default myremote
    ```

3. **Push data to the S3 bucket**:  
   After configuring the remote, push your data to the S3 bucket:

    ```bash
    dvc push
    ```

4. **Check the contents of your S3 bucket**:  
   You can verify whether the data was successfully uploaded to the S3 bucket by listing the objects in the bucket:

    ```bash
    aws s3api list-objects --bucket <your-s3-bucket-name>
    ```

5. **Deleting the S3 bucket and its contents**:  
   If you need to remove the S3 bucket and its contents, follow these steps:

    - First, delete all objects stored in the bucket:

      ```bash
      aws s3 rm s3://<your-s3-bucket-name> --recursive
      ```

    - Then, delete the bucket itself:

      ```bash
      aws s3api delete-bucket --bucket <your-s3-bucket-name>
      ```

By using S3 as a remote for DVC, you gain access to scalable and secure storage, making it easier to manage large datasets efficiently. Furthermore, you can easily maintain and clean up your S3 storage when needed.

## References

- [DVC Documentation](https://dvc.org/doc)
- [AWS CLI Documentation](https://docs.aws.amazon.com/cli/latest/)
