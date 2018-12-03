import os

from flask import Flask, jsonify, request

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/teste', methods=['POST'])
def testar():
    request_data = request.get_json()
    resposta = {
        "teste": request_data['teste']
    }
    return jsonify(resposta), 201

if __name__ == '__main__':
    app.run(port=5000)
