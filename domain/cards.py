from player import Player

class Card:

    def __init__(self, name, value, bonus=0):
        self.name = name
        self.type = type(self).__name__
        self.value = value
        self.bonus = bonus
    
    def get_name(self):
        return self.name
    
    def get_type(self):
        return self.type
    
    def get_value(self):
        return self.value
    
    def get_bonus(self):
        return self.bonus


class Escape(Card):
    pass


class Color(Card):
    def __init__(self, name, color, value, bonus=0):
        self.name = name
        self.type = type(self).__name__ + ':' + color[0].upper() + color[1:].lower()
        self.color = color
        self.value = value
        self.bonus = bonus
    
    def get_color(self):
        return self.color
        


class Black(Card):
    pass


class Pirate(Card):
    pass


class Mermaid(Card):
    def get_bonus(self, kill: bool):
        self.bonus += 50


class SkullKing(Card):
    
    def get_bonus(self, kills: int):
        self.bonus += kills * 30


class PlayedCards:

    def __init__(self):
        self.cards = []
        self.priorities = [
            "Escape",
            "Color",
            "Black",
            "Mermaid",
            "Pirate",
            "SkullKing"
        ]
    
    def play_card(self, player: Player, card: Card):
        self.cards.append({"card" : card, "player" : player})
    
    def check(self):
        pirates = False
        mermaids = False
        skull_king = False
        winner = self.cards[0]
        for card in self.cards:
            if self.priorities.index(card["card"].get_type()) > winner["card"].get_type():
                winner = {"card" : card["card"], "player" : card["player"]}
            elif self.priorities.index(card["card"].get_type()) == winner["card"].get_type():
                if 'Color' in winner["card"].get_type() and winner["card"].get_value() < card["card"].get_value():
                    winner = {"card" : card["card"], "player" : card["player"]}
