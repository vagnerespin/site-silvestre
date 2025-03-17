from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Local(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200))

class Especie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_comum = db.Column(db.String(100), nullable=False)
    nome_cientifico = db.Column(db.String(150))
    descricao = db.Column(db.String(300))
    imagem_url = db.Column(db.String(200))
    local_id = db.Column(db.Integer, db.ForeignKey('local.id'), nullable=False)

class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
