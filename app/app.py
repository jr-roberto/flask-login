from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Configuração do banco de dados MySQL
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://admin:rS5mQ5CTc22MD02F@localhost/applogin"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Configuração do Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"

from models import User  # Importa o modelo para evitar erros
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Importando Blueprints
from blueprints.auth import auth_bp
from blueprints.dashboard import dashboard_bp

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(dashboard_bp, url_prefix="/dashboard")

if __name__ == "__main__":
    # Garante que a criação das tabelas ocorra dentro do contexto da aplicação
    with app.app_context() as a:
        db.create_all()

    app.run(debug=True, port=2025)
