from flask import Flask, jsonify, request, abort

import os

from classes.usuario import Usuario

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/usuario", methods=["POST"])
def criar_usuario():
    if not request.json or not 'nome' in request.json:
        abort(400)

    usuario = {
        "nome": request.json["nome"],
        "fotos": request.json["fotos"]
    }

    # usu = Usuario(usuario)

    resposta = jsonify({"task": usuario})
    return resposta, 201

if __name__ == '__main__':
    app.run(port=5000)
