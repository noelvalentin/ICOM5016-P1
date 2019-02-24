from flask import Flask, jsonify, request
from handler.users import UserHandler
# Import Cross-Origin Resource Sharing to enable
# services on other ports on this machine or on other
# machines to access this app
from flask_cors import CORS, cross_origin

# Activate
app = Flask(__name__)
# Apply CORS to this app
CORS(app)

@app.route('/')
def greeting():
    return 'Hello, this is the Photo Messaging DB App!'

@app.route('/PhotoMessagingApp/users', methods=['GET', 'POST'])
def getAllUsers():
    return UserHandler().getAllUsers()

if __name__ == '__main__':
    app.run()
