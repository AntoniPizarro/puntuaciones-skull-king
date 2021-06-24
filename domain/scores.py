from domain.player import Player

class Scores:

    def __init__(self, players, rounds=10):
        '''
        Players: Lista con todos los jugadores de la partida(2-6)
        Rounds: Número de rondas de la partida (10 por defecto)
        '''
        self.players = []
        for player in players:
            self.players.append(Player(player))
        self.rounds = [1, rounds]
    
    def get_rounds(self):
        return self.rounds

    def pass_round(self):
        if self.rounds[0] != self.rounds[1]:
            self.rounds[0] += 1
    
    def player_pass_round(self, player_name, score, wins, bonus=0):
        for player in self.players:
            if player.get_name() == player_name:
                player.pass_round(self.rounds[0], score, wins, bonus)
    
    def finish_game(self):
        res = {}
        for player in self.players:
            res[player.get_name()] = player.get_total_score()
        
        return res