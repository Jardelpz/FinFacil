from app import db


class Divida(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(98))
    preco = db.Column(db.Float)
    data_vencimento = db.Column(db.String(29))
    is_pago = db.Column(db.Boolean, default=False)

    def __init__(self, name, preco, data_vencimento, is_pago, user_id):
        self.name = name
        self.preco = preco
        self.data_vencimento = data_vencimento
        self.is_pago = is_pago
        self.user_id = user_id