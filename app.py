import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the JSON file
try:
    with open('q-vercel-python.json') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: JSON file not found")
    data = []

# Enable CORS
from flask_cors import CORS
CORS(app)

# Define the API endpoint
@app.route('/api', methods=['GET'])
def get_marks():
    try:
        names = request.args.getlist('name')
        if not names:
            return jsonify({'error': 'No names provided'}), 400
        
        marks = [student['marks'] for student in data if student['name'] in names]
        return jsonify({'marks': marks})
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
