# AI381 Lab 2 – Container and CI

![MLOps CI](https://github.com/samardalilana172-ctrl/ai381-lab2-mlops/actions/workflows/ci.yml/badge.svg)

## Project Overview

This project packages a Customer Churn Prediction model as a FastAPI service using Docker.

The project includes automated testing, Docker image building, security scanning with Trivy, and publishing to GitHub Container Registry (GHCR) using GitHub Actions.

## Technologies

- Python 3.13
- FastAPI
- Scikit-learn
- Docker
- Pytest
- Ruff
- GitHub Actions
- Trivy
- GitHub Container Registry (GHCR)

## Project Structure

```text
src/
  app/
    main.py
  train/
    train.py
tests/
  test_api.py
Dockerfile
requirements.txt
model.joblib
README.md
```

## Run with Docker

Start the service with one command:

```bash
docker run -d --name ai381-churn-api -p 8000:8000 ghcr.io/samardalilana172-ctrl/ai381-lab2-mlops:610d32cb3dcebfe76a16bb877930979f4f5c0627
```

The API will be available at:

`http://localhost:8000`

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Check service health |
| POST | `/predict` | Predict customer churn probability |

Interactive API documentation:

`http://localhost:8000/docs`

### Example Prediction Request

```json
{
  "tenure_months": 12,
  "monthly_fee": 70.0,
  "contract": "Month-to-month",
  "internet_service": "Fiber optic",
  "support_calls": 2
}
```

### Example Response

```json
{
  "churn_probability": 0.427
}
```

The probability value depends on the input data.

## Run Tests Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the tests:

```bash
python -m pytest -v
```

Run linting:

```bash
ruff check src tests
```

## Docker and Security

The Dockerfile uses:

- Multi-stage build.
- Non-root application user.
- Pinned Python base image.
- Docker HEALTHCHECK.

Trivy is used to scan the Docker image for HIGH and CRITICAL vulnerabilities with available fixes.

## Continuous Integration

GitHub Actions automatically:

1. Runs Ruff linting and Pytest on every Pull Request.
2. Builds the Docker image on pushes to `main`.
3. Scans the image using Trivy.
4. Publishes the image to GHCR using the commit SHA as its tag.

## Published Docker Image

`ghcr.io/samardalilana172-ctrl/ai381-lab2-mlops`

Image tag:

`610d32cb3dcebfe76a16bb877930979f4f5c0627`

Image Digest:

`sha256:dbd165f7ecd4599e323e40b6ea481611810d74b8c8058ac9c66e371514687c1b`

## Repository

https://github.com/samardalilana172-ctrl/ai381-lab2-mlops