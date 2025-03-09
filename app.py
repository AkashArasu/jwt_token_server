from flask import Flask
from getstream import Stream
import json

app = Flask(__name__)

@app.route('/')
def generate_token(request):
    client = Stream(api_key="y8h5754fwgma", api_secret="zg87h9juqaqk8gxn6mrk3a5hkgkyxvh7rkkjke9wcufwxc9ukub6vp75qnymkrwp", timeout=3.0)

    # user_id = request.args.get('user_id')
    
    user_id = request.user.id

    token = client.create_token(user_id)
    return json.dumps({"token": token})

if __name__ == '__main__':
    app.run(debug=True)