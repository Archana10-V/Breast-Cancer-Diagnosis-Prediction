# Breast Cancer Diagnosis Prediction

A Machine Learning project for breast cancer diagnosis prediction using Python, Scikit-learn, Flask, Swagger UI, and Docker.

## Project Overview

This project uses a trained Machine Learning model to predict a breast cancer diagnosis category based on 30 numerical input features.

The Flask REST API allows users to submit feature values and receive a prediction through a JSON response. Swagger UI provides interactive API documentation and lets users test the endpoints directly from their browser.

**Prediction categories:**

* **Benign**
* **Malignant**

> **Disclaimer:** This project is for educational purposes only. Its predictions are not medical advice and must not be used as a substitute for professional medical diagnosis.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Flask
* Flasgger / Swagger UI
* Docker
* Git and GitHub

## Project Structure

```text
Breast-Cancer-Diagnosis-Prediction/
├── app.py
├── train.py
├── breast_cancer.csv
├── model.pkl
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

## How It Works

1. Load and prepare the breast cancer dataset.
2. Train a Machine Learning model using `train.py`.
3. Save the trained model as `model.pkl`.
4. Load the model in the Flask application.
5. Send numerical feature values to the `/predict` endpoint.
6. Receive the predicted diagnosis category in JSON format.
7. Use Swagger UI to explore and test the API.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Archana10-V/Breast-Cancer-Diagnosis-Prediction.git
```

### 2. Navigate to the project folder

```bash
cd Breast-Cancer-Diagnosis-Prediction
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment on Windows

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

Ensure that `requirements.txt` includes Flask, Scikit-learn, and Flasgger, along with the other dependencies required by the project.

### 6. Train the model if required

```bash
python train.py
```

If a compatible `model.pkl` is already included, retraining may not be necessary.

### 7. Start the Flask application

```bash
python app.py
```

The API runs on port `5000` by default.

## Swagger UI Documentation

After starting the Flask application, open:

**Local Swagger URL:** http://127.0.0.1:5000/apidocs/

Swagger UI allows users to inspect endpoints, enter JSON input, execute requests, and view API responses.

## API Endpoints

| Method | Endpoint   | Description                                               |
| ------ | ---------- | --------------------------------------------------------- |
| GET    | `/`        | Checks whether the API is running                         |
| POST   | `/predict` | Predicts a diagnosis category using 30 numerical features |

### Example API Response

```json
{
  "predicted_diagnosis": "Benign"
}
```

The response shown is an example; actual predictions depend on the input and trained model.

The `/predict` endpoint requires all 30 feature names expected by the model. Use numerical values and the exact feature names documented in the API.

## Run with Docker

Docker lets users run the application in a container without manually setting up the Python environment.

### 1. Pull the Docker image

```bash
docker pull archxna/breast-cancer-api:v2
```

### 2. Run the container

```bash
docker run -d --name breast-cancer-v2 -p 5002:5000 archxna/breast-cancer-api:v2
```

### 3. Open the API

API health check:

http://localhost:5002/

Swagger UI:

http://localhost:5002/apidocs/

These local URLs work on the computer running the container. To access Swagger over the internet, the API must be deployed to a publicly accessible hosting service.

## Docker Hub

**Docker Hub Repository:**

https://hub.docker.com/r/archxna/breast-cancer-api

**Image:** `archxna/breast-cancer-api:v2`

## GitHub Repositories

This project is maintained in separate GitHub repositories by the contributors.

### 1. Archana

* GitHub Profile: https://github.com/Archana10-V
* Project Repository: https://github.com/Archana10-V/Breast-Cancer-Diagnosis-Prediction

### 2. Maria Josephine

* GitHub Profile: https://github.com/mariajosephine-gif
* Project Repository: https://github.com/mariajosephine-gif/Breast-Cancer-Diagnosis-Prediction

Both repositories contain individual copies of the Breast Cancer Diagnosis Prediction project.

## Learning Outcomes

This project demonstrates practical experience with:

* Machine Learning model training and prediction
* Python application development
* REST API development using Flask
* Interactive API documentation using Swagger UI
* Docker image creation and containerization
* Version control and source-code hosting with Git and GitHub

## Future Improvements

* Add a user-friendly web frontend.
* Deploy the API to a public hosting platform.
* Improve error handling and input validation.
* Evaluate the model using suitable test data and metrics.
* Add automated tests and continuous integration.

## Disclaimer

This project is intended for educational and demonstration purposes only. It is not clinically validated and must not be used to diagnose disease or guide treatment decisions.
