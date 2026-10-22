
from fastapi.testclient import TestClient

from src.app.main import app


def test_health_endpoint():
    with TestClient(app) as client:
        response = client.get("/health")

        assert response.status_code == 200
        assert response.json() == {"status": "ok"}


def test_predict_valid_input():
    with TestClient(app) as client:
        response = client.post(
            "/predict",
            json={
                "tenure_months": 18,
                "monthly_fee": 88.34,
                "contract": "one-year",
                "internet_service": "fiber",
                "support_calls": 5,
            },
        )

        assert response.status_code == 200
        assert "churn_probability" in response.json()


def test_predict_rejects_missing_field():
    with TestClient(app) as client:
        response = client.post(
            "/predict",
            json={
                "tenure_months": 18,
                "monthly_fee": 88.34,
                "contract": "one-year",
                "internet_service": "fiber",
            },
        )

        assert response.status_code == 422


def test_predict_rejects_negative_tenure():
    with TestClient(app) as client:
        response = client.post(
            "/predict",
            json={
                "tenure_months": -1,
                "monthly_fee": 88.34,
                "contract": "one-year",
                "internet_service": "fiber",
                "support_calls": 5,
            },
        )

        assert response.status_code == 422


def test_prediction_is_deterministic():
    customer = {
        "tenure_months": 18,
        "monthly_fee": 88.34,
        "contract": "one-year",
        "internet_service": "fiber",
        "support_calls": 5,
    }

    with TestClient(app) as client:
        first_response = client.post("/predict", json=customer)
        second_response = client.post("/predict", json=customer)

        assert first_response.status_code == 200
        assert second_response.status_code == 200
        assert (
            first_response.json()["churn_probability"]
            == second_response.json()["churn_probability"]
        )
