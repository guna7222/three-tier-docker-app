from models.user_model import create_user, get_user_by_email
from werkzeug.security import generate_password_hash, check_password_hash

def signup_user(data):
    email = data.get('email')
    password = generate_password_hash(data.get('password'))
    return create_user(email, password)

def login_user(data):
    user = get_user_by_email(data.get('email'))
    if user and check_password_hash(user['password'], data.get('password')):
        return {"message": "Login successful"}, 200
    return {"message": "Invalid credentials"}, 401