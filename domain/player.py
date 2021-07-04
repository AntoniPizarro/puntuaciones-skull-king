import math

class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.rounds = {}
    
    def get_name(self) -> str:
        return self.name

    def pass_round(self, round, wins, bonus=0):
        '''
        round: ronda actual
        wins: bazas ganadas en la ronda
        bonus: bonus total de la ronda (0 por defecto)

        '''
        self.rounds[round]["wins"] = wins
        self.rounds[round]["bonus"] = bonus
        if self.rounds[round]["bet"] == wins:
            self.rounds[round]["score"] = 20 * wins + self.rounds[round]["bonus"]
        else:
            self.rounds[round]["score"] = -10 * int(math.sqrt((wins - self.rounds[round]["bet"]) ** 2))
    
    def bets(self, bet, round):
        '''
        bet: apuesta de la ronda
        round: ronda actual

        '''
        if round not in self.rounds:
            self.rounds[round] = {}
        self.rounds[round]["bet"] = bet
    
    def get_total_score(self) -> int:
        '''
        Obtiene la puntuación total actual del jugador

        '''
        score = 0
        for round in self.rounds:
            score += self.rounds[round]["score"] + self.rounds[round]["bonus"]
        
        return score