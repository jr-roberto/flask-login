from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask_login import UserMixin

db = SQLAlchemy()

'''
# ALTERACAO UPDATE
python -m flask db migrate -m "Comente alteracao"
python -m flask db upgrade
'''

class Usuarios(UserMixin, db.Model):
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    idade = Column(Integer, nullable=True)  # Nova coluna adicionada
    permissao = Column(Integer)

    def __repr__(self):
        return f'<Usuario {self.nome}>'
    
    