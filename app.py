from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

from flask import send_from_directory

@app.route('/')
def serve_react():
    return send_from_directory('build', 'index.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello! My Name is Sujay."})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
