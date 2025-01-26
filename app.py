import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the JSON file
with open('q-vercel-python.json') as f:
    data = json.load(f)

# Enable CORS
from flask_cors import CORS
CORS(app)

# Define the API endpoint
@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    if not names:
        return jsonify({'error': 'No names provided'}), 400
    
    marks = [student['marks'] for student in data if student['name'] in names]
    return jsonify({'marks': marks})

if __name__ == '__main__':
    app.run(debug=True)
