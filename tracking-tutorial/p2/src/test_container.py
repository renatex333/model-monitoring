import requests

# Create two records in dataframe_split format
# See more:
# - https://docs.databricks.com/en/machine-learning/model-serving/score-model-serving-endpoints.html
# - https://mlflow.org/docs/latest/models.html
data = {
    "dataframe_split": {
        "index": [0, 1],
        "columns": [
            "standardscaler__CreditScore",
            "standardscaler__Age",
            "standardscaler__Tenure",
            "standardscaler__Balance",
            "standardscaler__NumOfProducts",
            "standardscaler__HasCrCard",
            "standardscaler__IsActiveMember",
            "standardscaler__EstimatedSalary",
            "onehotencoder__Geography_Germany",
            "onehotencoder__Geography_Spain",
            "onehotencoder__Gender_Male",
        ],
        "data": [
            [
                0.7034400277211882,
                -0.7630345384131269,
                1.3849932562860656,
                -1.3317392101122278,
                0.7223895363269841,
                0.6490271882799827,
                1.0671385552841972,
                0.7424225974664149,
                0,
                0,
                1,
            ],
            [
                -0.31813189579236545,
                -1.5202590849095197,
                -0.32807215528511574,
                -1.3317392101122278,
                -0.7700253680702854,
                0.6490271882799827,
                -0.9370854375453458,
                0.7870485912430844,
                0,
                0,
                1,
            ],
        ],
    }
}

# Make request
resp = requests.post("http://localhost:8080/invocations", json=data)

# Print predictions
print(f"Status code: {resp.status_code}")
print(f"Response: {resp.text}")