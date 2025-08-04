from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the model
try:
    model = joblib.load('model.pkl')
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract form data
        gender = int(request.form.get('gender', 0))
        age = float(request.form.get('age', 0))
        hypertension = int(request.form.get('hypertension', 0))
        heart_disease = int(request.form.get('heart_disease', 0))
        ever_married = int(request.form.get('ever_married', 0))
        work_type = int(request.form.get('work_type', 0))
        residence_type = int(request.form.get('residence_type', 0))
        avg_glucose_level = float(request.form.get('avg_glucose_level', 0))
        bmi = float(request.form.get('bmi', 0))
        smoking_status = int(request.form.get('smoking_status', 0))

        # Format the input for the model
        sample_input = [gender, age, hypertension, heart_disease, ever_married,
                        work_type, residence_type, avg_glucose_level, bmi, smoking_status]

        # Prediction
        prediction = model.predict([sample_input])
        result = "Stroke" if prediction[0] == 1 else "No Stroke"
        
        return render_template('index.html', prediction=result)

    except Exception as e:
        print(f"Error in prediction: {e}")
        return render_template('index.html', error="Error making prediction. Check input values.")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)


