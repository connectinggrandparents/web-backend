from flask import Flask, send_from_directory, abort, jsonify, request
import json
from datetime import datetime, timedelta
import random
import os
from mail.mail import send_mail

from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, support_credentials=True)



@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE,OPTIONS')
    return response



@app.route('/comment', methods=['OPTIONS'])
def comment_options():
    return '', 200

@app.route('/comment', methods=['POST'])
def comment():
  req = request.get_json()
  return {
      'response':
      send_mail(req.get('name', 'unknown'), req.get('surnames', 'unknown'),
                req.get('text', 'unknown'), 'connectinggrandparents@gmail.com')
  }


@app.route('/')
def index():
  return jsonify({'response': 'ok'})


if __name__ == "__main__":
  port = int(os.environ.get("PORT", 8080))  # Render la define automáticamente
  app.run(host="0.0.0.0", port=port)  # ← host correcto
