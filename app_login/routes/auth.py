from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from models import db, Usuarios
from flask_login import login_user, logout_user

auth = Blueprint('auth',__name__, url_prefix="/auth")

@auth.route("/create", methods=["GET", "POST"])
def create():

    if request.method == "POST":
        user=Usuarios(**request.form.to_dict())
        db.session.add(user)
        db.session.commit()

    return render_template("create.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
    
    if request.method == "POST":
        data = request.form

        user = Usuarios.query.filter_by(email=data["email"]).first()

        if user:
            login_user(user=user)
            return jsonify({"message": "Usuario conectado com sucesso!"})

        return redirect(url_for("auth.login"))

    return render_template("login.html")


