from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the pre-trained Random Forest model
with open('random_forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('templates/final.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user inputs from the form
    data = request.json['input_data']
    
    # Ensure the input data is a list
    if not isinstance(data, list):
        return jsonify({'error': 'Invalid input format. Expected a list of values.'}), 400

    # Make predictions using the loaded model
    try:
        input_data = np.array(data).astype('float32')
        input_data = input_data.reshape(1, -1)
        prediction = model.predict(input_data)
        predicted_score = prediction[0]
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    # Render the modified HTML template with the predicted score
    return render_template('templates/final.html', predicted_score=predicted_score)

if __name__ == '__main__':
    app.run(debug=True)
