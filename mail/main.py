from flask import Flask, send_from_directory, abort, jsonify, request
import json
from datetime import datetime, timedelta
import random
import os
from mail import send_mail

from spam import send_verification
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/comment',methods=['POST'])
def comment():
  req = request.get_json()
  return {'response':send_mail(
    req.get('name','unknown'),
    req.get('surnames','unknown'),
    req.get('text','unknown'),
    'connectinggrandparents@gmail.com'
  )}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render la define automáticamente
    app.run(host="0.0.0.0", port=port)         # ← host correcto
