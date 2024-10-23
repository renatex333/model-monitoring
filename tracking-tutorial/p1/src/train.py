"""
This module contains functions to preprocess and train the model
for bank consumer churn prediction.
"""

import sys
import mlflow
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.utils import resample
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
)

def rebalance(data):
    """
    Resample data to keep balance between target classes.

    The function uses the resample function to downsample the majority class to match the minority class.

    Args:
        data (pd.DataFrame): DataFrame

    Returns:
        pd.DataFrame): balanced DataFrame
    """
    churn_0 = data[data["Exited"] == 0]
    churn_1 = data[data["Exited"] == 1]
    if len(churn_0) > len(churn_1):
        churn_maj = churn_0
        churn_min = churn_1
    else:
        churn_maj = churn_1
        churn_min = churn_0
    churn_maj_downsample = resample(
        churn_maj, n_samples=len(churn_min), replace=False, random_state=1234
    )

    return pd.concat([churn_maj_downsample, churn_min])

def preprocess(df):
    """
    Preprocess and split data into training and test sets.

    Args:
        df (pd.DataFrame): DataFrame with features and target variables

    Returns:
        ColumnTransformer: ColumnTransformer with scalers and encoders
        pd.DataFrame: training set with transformed features
        pd.DataFrame: test set with transformed features
        pd.Series: training set target
        pd.Series: test set target
    """
    filter_feat = [
        "CreditScore",
        "Geography",
        "Gender",
        "Age",
        "Tenure",
        "Balance",
        "NumOfProducts",
        "HasCrCard",
        "IsActiveMember",
        "EstimatedSalary",
        "Exited",
    ]
    cat_cols = ["Geography", "Gender"]
    num_cols = [
        "CreditScore",
        "Age",
        "Tenure",
        "Balance",
        "NumOfProducts",
        "HasCrCard",
        "IsActiveMember",
        "EstimatedSalary",
    ]
    data = df.loc[:, filter_feat]
    data_bal = rebalance(data=data)
    X = data_bal.drop("Exited", axis=1)
    y = data_bal["Exited"]

    test_size = 0.3
    mlflow.log_param("test_size", test_size)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=1912
    )
    col_transf = make_column_transformer(
        (StandardScaler(), num_cols),
        (OneHotEncoder(handle_unknown="ignore", drop="first"), cat_cols),
        remainder="passthrough",
    )

    X_train = col_transf.fit_transform(X_train)
    X_train = pd.DataFrame(X_train, columns=col_transf.get_feature_names_out())

    X_test = col_transf.transform(X_test)
    X_test = pd.DataFrame(X_test, columns=col_transf.get_feature_names_out())

    return col_transf, X_train, X_test, y_train, y_test

def train_regression(X_train, y_train):
    """
    Train a logistic regression model.

    Args:
        X_train (pd.DataFrame): DataFrame with features
        y_train (pd.Series): Series with target

    Returns:
        LogisticRegression: trained logistic regression model
    """
    max_iter = 1000
    mlflow.log_param("max_iter", max_iter)
    log_reg = LogisticRegression(max_iter=max_iter)
    log_reg.fit(X_train, y_train)
    # Infer signature (input and output schema)
    signature = mlflow.models.signature.infer_signature(
        X_train, log_reg.predict(X_train)
    )

    # Log model
    mlflow.sklearn.log_model(
        log_reg,
        "model",
        signature=signature,
        registered_model_name="churn-log-reg-model",
        input_example=X_train.iloc[:3],
    )
    return log_reg

def train_kneighbors(X_train, y_train):
    """
    Train a KNeighborsClassifier model.

    Args:
        X_train (pd.DataFrame): DataFrame with features
        y_train (pd.Series): Series with target

    Returns:
        KNeighborsClassifier: trained KNeighborsClassifier model
    """
    param_grid = {"n_neighbors": [3, 5, 7, 9, 11]}
    grid_search = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5, scoring="accuracy")
    grid_search.fit(X_train, y_train)

    best_params = grid_search.best_params_
    best_score = grid_search.best_score_

    mlflow.log_param("best_n_neighbors", best_params['n_neighbors'])
    mlflow.log_metric("best_cv_accuracy", best_score)

    best_knn = grid_search.best_estimator_
    # Infer signature (input and output schema)
    signature = mlflow.models.signature.infer_signature(
        X_train, best_knn.predict(X_train)
    )

    # Log model
    mlflow.sklearn.log_model(
        best_knn,
        "model",
        signature=signature,
        registered_model_name="churn-knn-model",
        input_example=X_train.iloc[:3],
    )
    return best_knn

def main(run_name: str, model_type: str, experiment_name: str = "churn-exp"):
    mlflow.set_experiment(experiment_name)
    with mlflow.start_run():
        mlflow.set_tag("mlflow.runName", run_name)

        df = pd.read_csv("data/Churn_Modelling.csv")
        col_transf, X_train, X_test, y_train, y_test = preprocess(df)

        if model_type == "regression":
            model = train_regression(X_train, y_train)
        elif model_type == "kneighbors":
            model = train_kneighbors(X_train, y_train)
        else:
            raise ValueError(f"Invalid model type: {model_type}")

        y_pred = model.predict(X_test)
        print(f"Accuracy score: {accuracy_score(y_test, y_pred):.2f}")
        print(f"Precision score: {precision_score(y_test, y_pred):.2f}")
        print(f"Recall score: {recall_score(y_test, y_pred):.2f}")
        print(f"F1 score: {f1_score(y_test, y_pred):.2f}")
        mlflow.log_metric("accuracy", accuracy_score(y_test, y_pred))
        mlflow.log_metric("precision", precision_score(y_test, y_pred))
        mlflow.log_metric("recall", recall_score(y_test, y_pred))
        mlflow.log_metric("f1", f1_score(y_test, y_pred))
        
        conf_mat = confusion_matrix(y_test, y_pred, labels=model.classes_)
        conf_mat_disp = ConfusionMatrixDisplay(
            confusion_matrix=conf_mat, display_labels=model.classes_
        )
        fig, ax = plt.subplots()
        conf_mat_disp.plot(ax=ax)
        fig.savefig("confusion_matrix.png")
        mlflow.log_artifact("confusion_matrix.png")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python train.py <run_name> <model_type> [experiment_name]")
        print("model_type: regression or kneighbors")
        sys.exit(1)
    if len(sys.argv) > 3:
        run_name = sys.argv[1]
        model_type = sys.argv[2]
        experiment_name = sys.argv[3]
        main(run_name=run_name, model_type=model_type, experiment_name=experiment_name)
    elif len(sys.argv) == 3:
        run_name = sys.argv[1]
        model_type = sys.argv[2]
        main(run_name=run_name, model_type=model_type)
    
