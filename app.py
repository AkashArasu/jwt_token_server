from flask import Flask
from getstream import Stream
import os
from dotenv import load_dotenv
import json

load_dotenv()
app = Flask(__name__)


@app.route('/')
def home():
    return os.getenv("API_KEY_NAME") + " " + os.getenv("API_SECRET_NAME")

@app.route('/get-token', methods=['GET'])
def generate_token(request):
    client = Stream(api_key=os.getenv("API_KEY_NAME"), api_secret=os.getenv("API_SECRET_NAME"), timeout=3.0)

    # user_id = request.args.get('user_id')
    
    user_id = request.user.id

    token = client.create_token(user_id)
    return json.dumps({"token": token})

if __name__ == '__main__':
    app.run(debug=True)