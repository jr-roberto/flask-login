from flask import Blueprint, jsonify
from flask_login import login_required, current_user

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
@login_required
def dashboard():
    return jsonify({"message": f"Welcome, {current_user.username}!"})
