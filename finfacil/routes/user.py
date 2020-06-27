from app import app, db
from flask import request, jsonify, json
from model.user import User


@app.route('/', methods=['GET'])
def helthy():
    return "Rota ok"


@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    #user = User.query.filter(User.email == email).first()
    user = User.query.get(id)
    result = {
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'cpf': user.cpf,
        'renda': user.renda,
        'economiza': user.economiza
    }

    return jsonify(result)


@app.route('/register', methods=['POST'])
def post_user():
    name = request.json['name']
    email = request.json['email']
    senha = request.json['senha']
    renda = request.json['renda']
    economiza = request.json['economiza']
    cpf = request.json['cpf']
    user = User(name, email, senha, renda, economiza, cpf)
    db.session.add(user)
    db.session.commit()
    retorno= jsonify("Usuário cadastrado")
    return retorno

@app.route('/login', methods=['POST'])
def login_user():
    email = request.json['email']
    senha = request.json['senha']
    user = User.query.filter(User.email == email, User.senha == senha).first()
    if user is not None:
        result = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'cpf': user.cpf,
            'renda': user.renda,
            'economiza': user.economiza
        }
        return jsonify(result)
    else:
        return "User not found"


@app.route('/user', methods=['PUT'])
def update_user():
    email = request.json['email']
    user = User.query.filter(User.email == email).first()
    user.name = request.json['name']
    user.senha = request.json['senha']
    user.renda = request.json['renda']
    user.economiza = request.json['economiza']
    #user.cpf = request.json['cpf']

    db.session.commit()

    return "Pessoa atualizada com sucesso"
