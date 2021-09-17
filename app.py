from flask import Flask, jsonify
from flask_cors import CORS
from pprint import pprint

from domain.maze import Maze
from domain.cards import PlayedCards
from domain.player import Player

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

@app.route("/player/add/<name>", methods=["GET"])
def new_user(name):
    '''
    'Bienvenida
    '''
    player_list.append(Player(name))
    for player in player_list:
        print(player.get_name())
    return jsonify(True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=PORT)