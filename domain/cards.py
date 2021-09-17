from tkinter.constants import NO
from domain.player import Player

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
    
    def get_data(self):
        data = {
            "name" : self.name,
            "type" : self.type,
            "value" : self.value,
            "bonus" : self.bonus
        }
        return data


class Escape(Card):

    def victory(self, to_compare: Card):
        if to_compare.get_type() != self.get_type():
            return False
        return True


class Color(Card):

    def __init__(self, name, color, value, bonus=0):
        self.name = name
        self.type = type(self).__name__ + ':' + color[0].upper() + color[1:].lower()
        self.color = color
        self.value = value
        self.bonus = bonus
    
    def get_color(self):
        return self.color
    
    def victory(self, to_compare: Card):
        if to_compare.get_type() == self.get_type() and self.get_value() < to_compare.get_value() or 'Escape' not in to_compare.get_type:
            return False
        return True

    def get_data(self):
        data = {
            "name" : self.name,
            "type" : self.type,
            "color" : self.color,
            "value" : self.value,
            "bonus" : self.bonus
        }
        return data
        

class Black(Card):

    def victory(self, to_compare: Card):
        less_priorities = [
            "Escape",
            "Color"
        ]
        for priority in less_priorities:
            if priority in to_compare.get_type() or to_compare.get_type() == self.get_type() and self.get_value() > to_compare.get_value():
                return True
        return False


class Pirate(Card):

    def victory(self, to_compare: Card):
        if 'SkullKing' not in to_compare.get_type() and to_compare.get_type() != self.get_type():
            return True
        return False


class ScaryMary(Card):

    def set_type(self, type):
        self.type = type + ':' + self.get_type()

    def victory(self, to_compare: Card):
        if 'Pirate' in self.get_type():
            if 'SkullKing' not in to_compare.get_type() and to_compare.get_type() != self.get_type():
                return True
        return False


class Mermaid(Card):

    def get_bonus(self, kill: bool):
        self.bonus += 50

    def victory(self, to_compare: Card):
        if 'Pirate' not in to_compare.get_type() and to_compare.get_type() != self.get_type():
            return True
        return False


class SkullKing(Card):
    
    def get_bonus(self, kills: int):
        self.bonus += kills * 30
    
    def victory(self, to_compare: Card):
        if 'Mermaid' not in to_compare.get_type() and to_compare.get_type() != self.get_type():
            return True
        return False


class PlayedCards:

    def __init__(self):
        self.cards = []
    
    def play_card(self, player: Player, card: Card):
        self.cards.append({"card" : card, "player" : player})
    
    def check(self):
        pirates = {"card" : None, "present" : False}
        mermaids = {"card" : None, "present" : False}
        skullKing = {"card" : None, "present" : False}

        winner = self.cards[0]

        if 'Pirate' in winner["card"].get_type():
            pirates["card"] = winner
            pirates["present"] = True

        elif 'Mermaid' in winner["card"].get_type():
            mermaids["card"] = winner
            mermaids["present"] = True

        elif 'SkullKing' in winner["card"].get_type():
            skullKing["card"] = winner
            skullKing["present"] = True

        for card in self.cards:
            if 'Pirate' in card["card"].get_type():
                if card["card"].victory(winner["card"]):
                    winner = card
                    pirates["card"] = winner
                    pirates["present"] = True

            elif 'Mermaid' in card["card"].get_type():
                if card["card"].victory(winner["card"]):
                    winner = card
                    mermaids["card"] = winner
                    mermaids["present"] = True

            elif 'SkullKing' in card["card"].get_type():
                if card["card"].victory(winner["card"]):
                    winner = card
                    skullKing["card"] = winner
                    skullKing["present"] = True
            else:
                if card["card"].victory(winner["card"]):
                    winner = card
        
        if pirates["present"] and mermaids["present"] and skullKing["present"]:
            winner = mermaids["card"]

        elif pirates["present"] and skullKing["present"]:
            winner = skullKing["card"]

        elif pirates["present"] and mermaids["present"]:
            winner = pirates["card"]

        elif skullKing["present"] and mermaids["present"]:
            winner = mermaids["card"]
        
        return winner
    
    def get_data(self):
        return self.cards