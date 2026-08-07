from flask import Flask, request, jsonify
from data.usuarios import usuarios, proximo_id

app = Flask(__name__)

app.config["JSON_SORT_KEYS"] = False

# Rota inicial
@app.route("/")
def inicio():
    return "Olá, API Connect!"


# GET - Listar todos os usuários
@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify(usuarios), 200


# POST - Cadastrar usuário
@app.route("/usuarios", methods=["POST"])
def cadastrar_usuario():
    global proximo_id

    dados = request.get_json()

    # Validação
    if not dados or not dados.get("nome") or not dados.get("email"):
        return jsonify({
            "error": "Os campos nome e e-mail são obrigatórios."
        }), 400

    novo_usuario = {
        "id": proximo_id,
        "nome": dados["nome"],
        "email": dados["email"]
    }

    usuarios.append(novo_usuario)
    proximo_id += 1

    return jsonify({
        "data": novo_usuario
    }), 201


# GET - Buscar usuário por ID
@app.route("/usuarios/<int:id>", methods=["GET"])
def buscar_usuario(id):
    for usuario in usuarios:
        if usuario["id"] == id:
            return jsonify(usuario), 200

    return jsonify({
        "error": "Usuário não encontrado."
    }), 404


# PUT - Atualizar usuário
@app.route("/usuarios/<int:id>", methods=["PUT"])
def atualizar_usuario(id):
    dados = request.get_json()

    if not dados or not dados.get("nome") or not dados.get("email"):
        return jsonify({
            "error": "Os campos nome e e-mail são obrigatórios."
        }), 400

    for usuario in usuarios:
        if usuario["id"] == id:
            usuario["nome"] = dados["nome"]
            usuario["email"] = dados["email"]

            return jsonify({
                "data": usuario
            }), 200

    return jsonify({
        "error": "Usuário não encontrado."
    }), 404


# DELETE - Remover usuário
@app.route("/usuarios/<int:id>", methods=["DELETE"])
def remover_usuario(id):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuarios.remove(usuario)

            return jsonify({
                "mensagem": "Usuário removido com sucesso."
            }), 200

    return jsonify({
        "error": "Usuário não encontrado."
    }), 404


if __name__ == "__main__":
    app.run(debug=True)