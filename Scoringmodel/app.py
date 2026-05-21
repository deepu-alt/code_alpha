from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("credit_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    income = float(request.form["income"])
    debt = float(request.form["debt"])
    credit_history = float(request.form["credit_history"])
    loan_amount = float(request.form["loan_amount"])
    missed_payments = float(request.form["missed_payments"])

    features = np.array([[income,
                          debt,
                          credit_history,
                          loan_amount,
                          missed_payments]])

    # Prediction
    prediction = model.predict(features)[0]

    # Probability Score
    probability = model.predict_proba(features)[0][1] * 100

    if prediction == 1:
        result = "Creditworthy ✅"
    else:
        result = "High Credit Risk ❌"

    return render_template(
        "index.html",
        prediction_text=result,
        score=round(probability, 2)
    )

if __name__ == "__main__":
    app.run(debug=True)