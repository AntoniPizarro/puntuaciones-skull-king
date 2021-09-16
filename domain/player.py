class Player:

    def __init__(self, name):
        self.data = {
            "name" : name,
            "scores" : {
                "rounds" : [],
                "total_score" : 0
            },
            "maze" : []
        }
        
    def get_name(self):
        return self.data["name"]

    def new_round(self):
        self.data["scores"]["rounds"].append({
            "bet" : 0,
            "wins" : 0,
            "bonus" : 0,
            "score" : 0
        })
    
    def total_score(self):
        return self.data["scores"]["total_score"]

    def calculate_total_score(self):
        rounds = self.data["scores"]["rounds"]
        score = 0
        for round in rounds:
            score += round["score"]
        
        self.data["scores"]["total_score"] = score
    
    def get_round(self, num):
        if num < 1 or len(self.data["scores"]["rounds"]) < 1:
            return False

        num -= 1
        round = self.data["scores"]["rounds"][num]

        return round

    def get_last_round(self):
        if len(self.data["scores"]["rounds"]) > 0:
            ind = len(self.data["scores"]["rounds"]) - 1
            return self.data["scores"]["rounds"][ind]
        return None

    def bet_round(self, num, bet):
        round = self.get_round(num)
        round["bet"] = bet
    
    def wins_round(self, num, wins):
        round = self.get_round(num)
        round["wins"] = wins
    
    def win_trick(self, num):
        round = self.get_round(num)
        round["wins"] += 1
    
    def bonus_round(self, num, bonus):
        round = self.get_round(num)
        round["bonus"] = bonus
    
    def score_round(self, num):
        round = self.get_round(num)
        bet = round["bet"]
        wins = round["wins"]
        bonus = round["bonus"]

        if bet == wins:
            if bet == 0:
                round["score"] = num * 10 + bonus
            else:
                round["score"] = bet * 20 + bonus
        else:
            if bet == 0:
                round["score"] = - num * 10
            else:
                round["score"] = - abs(bet - wins) * 10

    def add_card(self, card):
        self.data["maze"].append(card)
    
    def play_card(self, card):
        if card not in self.data["maze"]:
            return False
        ind = self.data["maze"].index(card)
        played = self.data["maze"].pop(ind)
        return played
    
    def get_maze(self):
        return self.data["maze"]
    