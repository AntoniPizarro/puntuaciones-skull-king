from domain.player import Player
from pprint import pprint

p1 = Player("Toni")
p2 = Player("Laura")
players = [p1, p2]
print("Players:")
for p in players:
    print(p.get_name())
    p.new_round()
print("===========")

p1.bet_round(1, 1) # Ronda 1 : Apuesta 1
p2.bet_round(1, 1) # Ronda 1 : Apuesta 1

p1.wins_round(1, 1) # Ronda 1 : Gana 1          +20
p2.wins_round(1, 0) # Ronda 1 : No gana nada    -10

p1.score_round(1) # Ronda 1: Calcular puntos
p2.score_round(1) # Ronda 1: Calcular puntos


for p in players:
    p.new_round()

p1.bet_round(2, 2) # Ronda 2 : Apuesta 2
p2.bet_round(2, 0) # Ronda 2 : Apuesta 0

p1.wins_round(2, 1) # Ronda 2 : Gana 1          -10
p2.wins_round(2, 1) # Ronda 2 : Gana 1          -20

p1.score_round(2) # Ronda 2: Calcular puntos
p2.score_round(2) # Ronda 2: Calcular puntos


for p in players:
    p.new_round()

p1.bet_round(3, 2) # Ronda 3 : Apuesta 2
p2.bet_round(3, 2) # Ronda 3 : Apuesta 2

p1.wins_round(3, 1) # Ronda 3 : Gana 1          -10
p2.wins_round(3, 2) # Ronda 3 : Gana 2          40

p1.score_round(3) # Ronda 3: Calcular puntos
p2.score_round(3) # Ronda 3: Calcular puntos

p1_name = p1.get_name()
p2_name = p2.get_name()
for p in players:
    p.calculate_total_score()
p1_score = p1.total_score()
p2_score = p2.total_score()

print("Scores:")
print(p1_name + ": " + str(p1_score)) # Toni: 0
print(p2_name + ": " + str(p2_score)) # Laura: 10