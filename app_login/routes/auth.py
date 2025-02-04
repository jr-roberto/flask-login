from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
from models import db, Usuarios
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth',__name__, url_prefix="/auth", template_folder="../templates/auth/")

@auth.route("/registro", methods=["GET", "POST"])
@login_required
def registro():

    if request.method == "POST":
        data=request.form

        if Usuarios.query.filter_by(email=data["email"]).first():
            flash("Este usuario ja existe no sistema!","warning"); return redirect(url_for("auth.registro"))

        user=Usuarios(**data)
        user.set_password_hash(password=data["password_hash"])
        db.session.add(user)
        db.session.commit()

        flash("Usuario cadastrado com sucesso!","success"); return redirect(url_for("auth.registro"))

    return render_template("create.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
    
    if request.method == "POST":
        data = request.form
        user = Usuarios.query.filter_by(email=data["email"]).first()

        if user and user.check_password(data["password"]):
            login_user(user=user)
            return jsonify({"message": "Usuario conectado com sucesso!"})

        flash("Dados incorretos verifique e tente novamente.","warning")

    return render_template("login.html")

@auth.route("/logout", methods=["GET", "POST"])
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
