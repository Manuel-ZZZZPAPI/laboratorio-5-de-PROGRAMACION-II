from flask import Flask, request, jsonify
from db import create_user, get_all_users, get_user, update_user, delete_user

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"mensaje": "API REST con Flask"})


#GET /users-obtener todos

@app.route("/users", methods=["GET"])
def users_list():
    usuarios = get_all_users()
    return jsonify(usuarios), 200


#GET /users/<id>-obtener uno
@app.route("/users/<int:user_id>", methods=["GET"])
def users_get(user_id):
    usuario = get_user(user_id)
    if usuario:
        return jsonify(usuario), 200
    return jsonify({"error": "Usuario no encontrado"}), 404


#POST /users-crear usuario
@app.route("/users", methods=["POST"])
def users_post():
    data = request.get_json()

    try:
        nuevo = create_user(data)
        return jsonify(nuevo), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


#PUT /users/<id>-actualizar usuario

@app.route("/users/<int:user_id>", methods=["PUT"])
def users_put(user_id):
    data = request.get_json()

    try:
        actualizado = update_user(user_id, data)
        if actualizado:
            return jsonify(actualizado), 200
        else:
            return jsonify({"error": "Usuario no encontrado"}), 404
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


#DELETE /users/<id>-eliminar usuario

@app.route("/users/<int:user_id>", methods=["DELETE"])
def users_delete(user_id):
    eliminado = delete_user(user_id)
    if eliminado:
        return jsonify({"mensaje": "Usuario eliminado"}), 200
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404


#EJECUCIÓN DEL SERVIDOR
if __name__ == "__main__":
    app.run(debug=True)
