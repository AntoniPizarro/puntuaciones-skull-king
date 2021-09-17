from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
from pprint import pprint

from domain.maze import Maze
from domain.cards import PlayedCards
from domain.player import Player
from service.db import Data_Base as db

DB = "skull_king"
HOST = "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.4uubd.mongodb.net/" + DB + "?retryWrites=true&w=majority"
PORT = 5505

app = Flask(__name__)
CORS(app)

maze = Maze()
player_list = []

# GET
@app.route("/", methods=["GET"])
def ping():
    '''
    'Bienvenida
    '''
    return "Skull King API REST"

@app.route("/users/add", methods=["POST"])
def new_user():
    '''
    'Registra un nuevo usuario
    '''
    data = request.get_json()
    pprint(data)
    if db.add_document(HOST, DB, "users", data):
        return jsonify({
            "new_user" : "Usuario registrado correctamente"
        })
    else:
        return jsonify({
            "new_user" : "Ha ocurrido un error"
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=PORT)