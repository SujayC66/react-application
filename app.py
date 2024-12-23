from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='build', static_url_path='')
CORS(app)  # Allow cross-origin requests

@app.route('/')
def serve_react():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello! My Name is Sujay."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
