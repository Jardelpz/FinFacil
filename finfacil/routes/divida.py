from app import app, db
from flask import request, jsonify, json
from model.divida import Divida
from model.user import User


@app.route('/divida', methods=['POST'])
def post_divida():
    email = request.args['email']
    user = User.query.filter(User.email == email).first()
    if user is not None:
        name = request.json['name']
        preco = request.json['preco']
        data_vencimento = request.json['data_vencimento']
        user_id = user.id
        divida = Divida(name, preco, data_vencimento, False, user_id)
        result = {
            'id': divida.id,
            'name': divida.name,
            'pago': divida.is_pago,
            'data_vencimento':divida.data_vencimento,
            'preco': divida.preco,
            'user': divida.user_id
        }

        db.session.add(divida)
        db.session.commit()

        return jsonify(result)
    else:
        return "Não foi possível cadastrar"


@app.route('/divida', methods=['GET'])
def lista_divida():
    email = request.args['email']
    user = User.query.filter(User.email == email).first()
    dividas = Divida.query.filter(Divida.user_id == user.id, Divida.is_pago == False).all()
    result = []
    for divida in dividas:
        data = {
            "name": divida.name,
            "preco": divida.preco,
            "data_vencimento": divida.data_vencimento,
            "is_pago": divida.is_pago,
            "id": divida.id
        }
        result.append(data)
    return jsonify(result)

@app.route('/divida/pagar', methods=['GET'])
def pagar():
    id = request.args['id']
    divida = Divida.query.get(id)
    divida.is_pago = True
    #db.session.delete(divida)
    db.session.commit()
    return f"Divida de {divida.preco} paga com sucesso!"


@app.route('/divida/soma', methods=['GET'])
def soma():
    email = request.args['email']
    user = User.query.filter(User.email == email).first()
    economiza = user.economiza
    renda = user.renda
    dividas = Divida.query.filter(Divida.user_id == user.id).all()
    total = 0
    for d in dividas:
        total = total + d.preco
    liquido = renda - total
    porcentagem = renda * economiza/100
    atingiu = ""
    if liquido > porcentagem:
        atingiu = f"Você está atingindo sua meta de {economiza}%"
    else:
        atingiu = f"Você não atingiu sua meta de {economiza}%"
    data = {
        "total": total,
        "msg": atingiu
    }
    return jsonify(data)

#Fins de teste
@app.route('/lista', methods=['GET'])
def lista_dividas():
    dividas = Divida.query.all()
    result = []
    for divida in dividas:
        data = {
            "name": divida.name,
            "preco": divida.preco,
            "data_vencimento": divida.data_vencimento,
            "is_pago": divida.is_pago
        }
        result.append(data)
    return jsonify(result)
