from tkinter import *

from domain.scores import Scores

# Declaración ventana
ventana = Tk()
ventana.geometry("1600x900")

# WIDGETS
# Entradas
ent_ronda_actual = Entry(ventana)

# Lanzamiento ventana
ventana.title("Skull King")
ventana.iconbitmap("./assets/img/skull_pirate.ico")

print("OK!")
ventana.mainloop()