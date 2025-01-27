from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load the JSON data file
with open('data.json') as f:
    data = json.load(f)

# Enable CORS
@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# Define the API endpoint
@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = []
    for name in names:
        for student in data:
            if student['Name'] == name:
                marks.append(student['Marks'])
                break
        else:
            marks.append(None)
    return jsonify({'marks': marks})

if __name__ == '__main__':
    app.run(debug=True)
