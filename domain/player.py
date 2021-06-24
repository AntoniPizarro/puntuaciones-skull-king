class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.rounds = {}
    
    def get_name(self):
        return self.name

    def pass_round(self, round, score, wins, bonus=0):
        '''
        round: ronda actual
        score: puntuación total de la ronda
        wins: bazas ganadas en la ronda
        bonus: bonus total de la ronda (0 por defecto)
        '''
        self.rounds[round]["score"] = score
        self.rounds[round]["wins"] = wins
        self.rounds[round]["bonus"] = bonus
    
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
            score += round["score"] + round["bonus"]
        
        return score