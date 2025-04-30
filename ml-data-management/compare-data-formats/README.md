# Comparing File Formats

This project is designed to compare the performance of different file formats—namely JSON, CSV, and Parquet—when reading data using the `pandas` library in Python. The experiment evaluates the time it takes to read data from each format over multiple iterations, aiming to highlight the differences in speed and efficiency between these formats.

## Overview

In this project, we explore the performance and characteristics of different data formats—JSON, CSV, and Parquet—commonly used in machine learning (ML) workflows. Each format offers unique advantages and drawbacks depending on the application, dataset size, and use case. 

### JSON

JSON (JavaScript Object Notation) is a widely-used, language-independent format that stores data in a human-readable format consisting of attribute-value pairs. It’s easy to understand and use, but JSON lacks advanced features like compression, making it slower and more storage-intensive for large datasets compared to other formats.

### CSV

CSV (Comma-Separated Values) is a simple and widely-supported format that stores tabular data in plain text. CSV files are lightweight but have limitations, such as no native support for complex data types, lack of metadata, and larger storage requirements. Moreover, CSV lacks compression, making it less efficient for handling large datasets. 

Common limitations of CSV in ML:
- Lack of standardized schema and support for advanced data types.
- No built-in compression, leading to higher storage needs.
- Performance overhead when dealing with large datasets.

### Parquet

Parquet is a columnar storage format designed for efficient data storage and processing. It offers better compression and faster query execution compared to row-based formats like CSV and JSON. Parquet’s columnar nature allows for selective reading of data, reducing memory usage and improving speed. This makes it especially useful in big data and ML scenarios, where datasets are large and frequent I/O operations occur.

Key benefits for ML:
- Reduced storage costs through built-in compression.
- Optimized query performance, especially for large datasets.
- Efficient for selective column reads, accelerating ML training and analysis.

### Key Steps:

1. **Loading Data**: The data is loaded from files in JSON, CSV, and Parquet formats.
2. **Performance Measurement**: For each file format, the loading time is measured over 1000 iterations to gather reliable performance metrics.
3. **Comparison**: The results are analyzed using descriptive statistics and visualized with a box plot for better insight.

## Project Structure

- **`data/`**: Contains the data files in JSON, CSV, and Parquet formats, as well as a file (`times.parquet`) for storing the recorded performance times.

- **`notebooks/`**: Jupyter notebooks with detailed steps for running the experiments and visualizing the results.

### Conclusion

Through this project, we compare the performance of JSON, CSV, and Parquet in terms of data loading times and processing efficiency. Parquet tends to offer the best performance in scenarios where storage efficiency and speed are critical, especially for large-scale ML tasks.

## References

- [Parquet File Format](https://parquet.apache.org/docs/file-format/)