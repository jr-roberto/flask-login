from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config
from models import db, Usuarios
from datetime import timedelta

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = "dev"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

db.init_app(app)
migrate = Migrate(app, db)  # Adicionando suporte a migrações

# Configuração do Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(user_id):
    return Usuarios.query.get(user_id)

from routes.auth import auth
app.register_blueprint(auth)

if __name__=="__main__":
    app.run(debug=True, port=2025)
