from flask import Flask, request, jsonify
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('model/student_model.pkl')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input JSON data
        data = request.get_json()

        # Extract inputs from JSON
        attendance = float(data['attendance'])
        assignments = float(data['assignments'])
        test_scores = float(data['test_scores'])

        # Make prediction
        prediction = model.predict([[attendance, assignments, test_scores]])[0]

        # Map numerical grade back to letter grade
        grade_map = {4: 'A', 3: 'B', 2: 'C', 1: 'D', 0: 'F'}
        predicted_grade = grade_map.get(prediction, 'Unknown')

        # Return prediction as JSON
        return jsonify({'predicted_grade': predicted_grade})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
