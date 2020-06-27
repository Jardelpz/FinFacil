from app import db
from model.divida import Divida


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    divida = db.relationship(Divida)
    name = db.Column(db.String(98))
    email = db.Column(db.String(60))
    senha = db.Column(db.String(12))
    cpf = db.Column(db.String(11))
    renda = db.Column(db.Float)
    economiza = db.Column(db.Integer)

    def __init__(self, name, email, senha, renda, economiza, cpf):
        self.name = name
        self.email = email
        self.senha = senha
        self.renda = renda
        self.economiza = economiza
        self.cpf = cpf