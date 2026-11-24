
from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("superkart_model.joblib")

@app.route("/")
def home():
    return "SuperKart Sales Forecast API is running"

@app.route("/v1/predict", methods=["POST"])
def predict():

    data = request.get_json()

    df = pd.DataFrame([data])

    prediction = model.predict(df)

    return jsonify(
        {
            "Predicted_Product_Store_Sales_Total": float(prediction[0])
        }
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
