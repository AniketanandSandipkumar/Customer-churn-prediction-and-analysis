from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import os
import webbrowser
import threading
from flask import Flask, render_template
from segmentation_utils import generate_segmentation_plots

app = Flask(__name__)
# Load model and scaler
model = pickle.load(open('models/churn_model.pkl', 'rb'))
scaler = pickle.load(open('models/scaler.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict_page():
    return render_template('predict.html')

@app.route('/segmentation')
def segmentation():
    generate_segmentation_plots()
    
    return render_template('segmentation.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')

@app.route('/predict_churn', methods=['POST'])
def predict_churn():
    try:
        # Get numeric fields
        cust_id = float(request.form['CustomerID'])
        age = float(request.form['Age'])
        tenure = float(request.form['Tenure'])
        usage = float(request.form['Usage Frequency'])
        support = float(request.form['Support Calls'])
        delay = float(request.form['Payment Delay'])
        spend = float(request.form['Total Spend'])
        last_interaction = float(request.form['Last Interaction'])

        # Get categorical fields
        gender = request.form['Gender']
        subscription = request.form['Subscription Type']
        contract = request.form['Contract Length']

        # Manual one-hot encoding in same order as training
        gender_encoded = [1, 0] if gender == 'Female' else [0, 1]
        sub_encoded = [
            1 if subscription == 'Basic' else 0,
            1 if subscription == 'Premium' else 0,
            1 if subscription == 'Standard' else 0
        ]
        contract_encoded = [
            1 if contract == 'Annual' else 0,
            1 if contract == 'Monthly' else 0,
            1 if contract == 'Quarterly' else 0
        ]

        # Combine all 16 features in exact order
        features = [
            cust_id, age, tenure, usage, support, delay,
            spend, last_interaction
        ] + gender_encoded + sub_encoded + contract_encoded

        # Scale and predict
        scaled = scaler.transform([features])
        prediction = model.predict(scaled)[0]
        result = "1! High Risk of Churn" if prediction == 1 else "0! Likely Retained"

        return jsonify({'result': result})

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
