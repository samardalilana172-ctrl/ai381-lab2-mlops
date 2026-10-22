
from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT_DIR / "churn_v2.csv"
MODEL_PATH = ROOT_DIR / "model.joblib"

NUMERIC_FEATURES = [
    "tenure_months",
    "monthly_fee",
    "support_calls",
]

CATEGORICAL_FEATURES = [
    "contract",
    "internet_service",
]

FEATURES = NUMERIC_FEATURES + CATEGORICAL_FEATURES
TARGET = "churn"


def train_model():
    df = pd.read_csv(DATA_PATH)

    X = df[FEATURES]
    y = df[TARGET]

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), NUMERIC_FEATURES),
            (
                "cat",
                OneHotEncoder(handle_unknown="ignore"),
                CATEGORICAL_FEATURES,
            ),
        ]
    )

    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", LogisticRegression(max_iter=1000)),
        ]
    )

    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)

    print(f"Model saved to: {MODEL_PATH}")


if __name__ == "__main__":
    train_model()
