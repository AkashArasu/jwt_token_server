from flask import Flask
from getstream import Stream
import os
from dotenv import load_dotenv
import json
from flask_cors import CORS

load_dotenv()
app = Flask(__name__)


# Option 2: Allow only specific origins (more secure)
CORS(app, resources={r"/get-token/*": {"origins": "https://akasharasu.github.io"}})


@app.route('/')
def home():
    return "Hello World"

@app.route('/get-token/<user_id>', methods=['GET'])
def generate_token(user_id):

    client = Stream(api_key=os.getenv("API_KEY_NAME"), api_secret=os.getenv("API_SECRET_NAME"), timeout=3.0)
    token = client.create_token(user_id)
    return json.dumps({"token": token})

if __name__ == '__main__':
    app.run(debug=True)