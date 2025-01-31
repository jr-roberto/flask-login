from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user
from models import User, db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"message": "User already exists"}), 400

    user = User(username=data["username"])
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created successfully"})

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()
    if user and user.check_password(data["password"]):
        login_user(user)
        return jsonify({"message": "Login successful"})
    return jsonify({"message": "Invalid credentials"}), 401

@auth_bp.route("/logout")
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully"})
