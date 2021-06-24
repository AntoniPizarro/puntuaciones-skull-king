from domain.scores import Scores

jugadores = ["Toni","Laura","Pere"]
rondas = 3

tabla_puntuaciones = Scores(jugadores, rondas)
rounds = tabla_puntuaciones.get_rounds()
tabla_puntuaciones.pass_round()
rounds = tabla_puntuaciones.get_rounds()
tabla_puntuaciones.player_pass_round("Toni", 10, 3)