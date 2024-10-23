# Machine Learning Model Monitoring

Welcome to this ML project! This repository focuses on monitoring machine learning models in production, covering key concepts like resource monitoring, performance metrics, ground truth evaluation, and data drift detection. It also includes a notebook with a study on data drift, providing practical insights into detecting shifts in input data to maintain model performance over time.

## Installing Dependencies

To install the project dependencies, use the `requirements.txt` file:

```sh
pip install -r requirements.txt
```

## MLOps Perspective: Monitoring Machine Learning Models

From an MLOps point of view, machine learning models need to be monitored at two levels:

- **Resource level**: We need to ensure the model is running correctly in the production environment. Here, we monitor CPU, RAM, storage, and check that requests are being processed at the expected rate without errors.
  
- **Performance level**: We monitor the model's performance to ensure it maintains its relevance over time. Changes in user behavior or data can lead to performance degradation as the patterns learned during training may no longer be valid.

### Importance of Performance Monitoring

As the world constantly changes, a static model may fail to capture new patterns emerging over time. It is crucial to monitor **performance metrics** and address **data drift** to ensure that the model remains aligned with the **business goals**. Always consult with business stakeholders to define meaningful thresholds for these metrics.

### Classification Performance Metrics

For classification problems, some key performance metrics are:

- **Accuracy**: Proportion of correctly classified instances out of the total instances.

  \( A = \frac{TP + TN}{TP + TN + FP + FN} \)

- **Precision**: Proportion of true positive predictions out of all positive predictions.

  \( P = \frac{TP}{TP + FP} \)

- **Recall (Sensitivity or True Positive Rate)**: Proportion of true positive predictions out of all actual positive instances.

  \( R = \frac{TP}{TP + FN} \)

- **Specificity**: Proportion of true negative predictions out of all actual negative instances.

  \( S = \frac{TN}{TN + FP} \)

- **F1 Score**: Combines precision and recall into a single metric.

  \( F = 2 \cdot \frac{P \cdot R}{P + R} \)

- **Area Under the ROC Curve (AUC-ROC)**: Measures the model's ability to distinguish between positive and negative instances across different thresholds.

### Regression Performance Metrics

For regression problems, we often use:

- **Mean Absolute Error (MAE)**: Average absolute difference between predicted and actual values.

  \( MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i| \)

- **Mean Squared Error (MSE)**: Average squared difference between predicted and actual values.

  \( MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 \)

- **Root Mean Squared Error (RMSE)**: Square root of MSE, providing the average magnitude of residuals. It is preferred instead of MSE as RMSE is in the same unit as the target variable.

  \( RMSE = \sqrt{MSE} \)

- **R-squared (Coefficient of Determination)**: Proportion of variance in the dependent variable predictable from the independent variables.

  \( R^2 = 1 - \frac{SSR}{SST} \)

  where SSR is the sum of squared residuals, and SST is the total sum of squares.

- **Mean Absolute Percentage Error (MAPE)**: Average percentage difference between predicted and actual values. It is often preferred instead of RMSE in situations where relative errors are more important than absolute errors. 

  \( MAPE = \frac{1}{n} \sum_{i=1}^{n} \left| \frac{y_i - \hat{y}_i}{y_i} \right| \times 100 \)

- **Adjusted R-squared**: Adjusts the R-squared value by penalizing the addition of unnecessary predictors, providing a more accurate measure of goodness of fit.

  \( \text{Adjusted } R^2 = 1 - \left[ \frac{(1 - R^2) \times (n - 1)}{n - p - 1} \right] \)

  where \( n \) is the sample size and \( p \) is the number of predictors.

### Ground Truth Evaluation

Ground Truth Evaluation involves monitoring model performance in production by comparing its performance on a separate test set (used during training) with its performance on the current production data. This process requires waiting for labeled events to occur in the production environment. For example, in a recommendation engine, we must wait for a customer to click on or purchase a recommended product.

Once new ground truth data is collected, the model’s performance is evaluated against predefined training metrics. If a significant disparity between the model’s current performance and the established metrics arises, it indicates that the model may be outdated and in need of retraining or updates.

However, Ground Truth Evaluation can be impractical when events or outcomes take a long time to materialize, making it challenging to obtain timely labeled data. For instance, in fraud detection, it may take months for a fraudulent claim to be identified, or in disease prediction models, it could take years for outcomes to occur. In cases where the target variable’s maturation time is lengthy, relying solely on Ground Truth Evaluation becomes inefficient for timely model monitoring.

### Data Drift

Given the limitations of Ground Truth Evaluation, a more practical approach is **data drift** or **input drift detection**. Rather than relying solely on ground truth labels, this method focuses on identifying changes in the input data itself, without needing explicit knowledge of the actual outcomes.

By comparing the distribution of features in the current production data with those from the training data, we can detect shifts in input data over time. This helps identify changes in the environment or user behavior that may impact model performance, providing a more proactive and efficient way to monitor machine learning models.

Detecting shifts in data patterns early through input feature comparison enables timely interventions, preventing significant performance degradation before it occurs.
