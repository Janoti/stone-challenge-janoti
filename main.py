# Desafio Stone Devops SRE
# API
import os

from flask import Flask, jsonify, abort, request

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))


users = [ # Array of dictionaries. Memory Database of users
     {
      'name': 'User 1',
      'sobrenome': 'Sobrenome 1',
      'cpf': '11111111111',
      'email': 'user1@yahoo.com.br',
      'data_nasc': '09/05/1985'
      },
      {
      'name': 'User 2',
      'sobrenome': 'Sobrenome 2',
      'cpf': '22222222222',
      'email': 'user2@yahoo.com.br',
      'data_nasc': '10/06/1985'
      },
      {
      'name': 'User 3',
      'sobrenome': 'Sobrenome 3',
      'cpf': '33333333333',
      'email': 'user3@yahoo.com.br',
      'data_nasc': '13/08/1985'
      }
]


@app.route("/users")
def get_users():
    return jsonify({'users': users})


@app.route("/users/<string:cpf>", methods=['GET'])
def search_cpf(cpf):
    user = [user for user in users if user['cpf'] == cpf]
    if len(user) == 0:
        abort(404)
    return jsonify({'user': user[0]})


@app.route("/users", methods=['POST'])
def insert_user():
    if not request.json:
        abort(400)
    payload = request.get_json(force=True)
    user = {
        'nome': payload['nome'],
        'sobrenome': payload['sobrenome'],
        'cpf': payload['cpf'],
        'email': payload['email'],
        'data_nasc': payload['data_nasc']
    }
    users.append(user)
    return jsonify({'users': user}), 201


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)
