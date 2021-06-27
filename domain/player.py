import math

class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.rounds = {}
    
    def get_name(self):
        return self.name

    def pass_round(self, round, wins, bonus=0):
        '''
        round: ronda actual
        wins: bazas ganadas en la ronda
        bonus: bonus total de la ronda (0 por defecto)
        '''
        self.rounds[round]["wins"] = wins
        self.rounds[round]["bonus"] = bonus
        self.rounds[round]["score"] = math.sqrt((wins - self.rounds[round]["bet"]) ** 2)
    
    def bets(self, bet, round):
        '''
        bet: apuesta de la ronda
        round: ronda actual
        '''
        self.rounds[round]["bet"] = bet
    
    def get_total_score(self):
        '''
        Obtiene la puntuación total actual del jugador
        '''
        score = 0
        for round in self.rounds:
            score += self.rounds[round]["score"] + self.rounds[round]["bonus"]
        
        return score