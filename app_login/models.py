from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, func
from flask_login import UserMixin
from flask_bcrypt import Bcrypt
from datetime import datetime

db = SQLAlchemy()
bcrypt = Bcrypt()

'''
# ALTERACAO UPDATE
python -m flask db migrate -m "Comente alteracao"
python -m flask db upgrade
'''

class Usuarios(UserMixin, db.Model):
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    permissao = Column(Integer)
    password_hash = Column(String(255), nullable=False)

    def set_password_hash(self, password):
        self.password_hash = bcrypt.generate_password_hash(password=password).decode("utf-8")

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<Usuario {self.nome}>'
    
def seed_usuario_master():
    """Adiciona um usuário master se ele não existir."""
    usuario_master = Usuarios.query.filter_by(email="admin@exemplo.com").first()
    
    if not usuario_master:
        senha_hash = bcrypt.generate_password_hash("123mudar#@")
        usuario_master = Usuarios(
            nome="Admin Master",
            email="admin@exemplo.com",
            permissao=1,
            password_hash=senha_hash
        )
        db.session.add(usuario_master)
        db.session.commit()
        print("Usuário master criado com sucesso.")
    else:
        print("Usuário master já existe.")
        