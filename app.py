from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))


@app.route("/")
def home():
    return "Breast Cancer Diagnosis Prediction API Running"


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    features = [
        data["radius_mean"],
        data["texture_mean"],
        data["perimeter_mean"],
        data["area_mean"],
        data["smoothness_mean"],
        data["compactness_mean"],
        data["concavity_mean"],
        data["concave points_mean"],
        data["symmetry_mean"],
        data["fractal_dimension_mean"],
        data["radius_se"],
        data["texture_se"],
        data["perimeter_se"],
        data["area_se"],
        data["smoothness_se"],
        data["compactness_se"],
        data["concavity_se"],
        data["concave points_se"],
        data["symmetry_se"],
        data["fractal_dimension_se"],
        data["radius_worst"],
        data["texture_worst"],
        data["perimeter_worst"],
        data["area_worst"],
        data["smoothness_worst"],
        data["compactness_worst"],
        data["concavity_worst"],
        data["concave points_worst"],
        data["symmetry_worst"],
        data["fractal_dimension_worst"]
    ]

    prediction = model.predict([features])

    if prediction[0] == "M":
        diagnosis = "Malignant"
    else:
        diagnosis = "Benign"

    return jsonify({
        "predicted_diagnosis": diagnosis
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
