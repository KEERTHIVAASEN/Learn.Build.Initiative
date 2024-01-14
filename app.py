from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "admin": generate_password_hash("secret")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/admin')
@auth.login_required
def admin():
    return "Hello, Admin!"

if __name__ == '__main__':
    app.run(debug=True)