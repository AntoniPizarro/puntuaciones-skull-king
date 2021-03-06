from domain.cards import Card
from domain.player import Player
from domain.cards import Card, Color, Escape, Black, Pirate, ScaryMary, Mermaid, SkullKing
from random import shuffle

class Maze:

    def __init__(self):
        self.cards = []
        colores = [
            "Azul",
            "Amarillo",
            "Rojo"
        ]
        
        for color in colores:
            for i in range(13):
                self.cards.append(Color("Palo " + color, color, i + 1))
        
        for i in range(13):
            self.cards.append(Black("Bandera Negra", i + 1))
        
        for i in range(5):
            self.cards.append(Escape("Bandera Blanca", 0))

        for i in range(5):
            self.cards.append(Pirate("Pirata", 0))

        for i in range(2):
            self.cards.append(Mermaid("Sirena", 0))

        for i in range(1):
            self.cards.append(ScaryMary("Scary Mary", 0))

        for i in range(1):
            self.cards.append(SkullKing("Skull King", 0))
    
    def get_shuffled(self):
        shuffle(self.cards)
    
    def distribute(self, players: list, cards: int):
        self.get_shuffled()

        for i in range(cards):
            for player in players:
                player.add_card(self.cards.pop(0))

    def add_card(self, card: Card):
        self.cards.append(card)
    
    def get_data(self):
        return self.cards