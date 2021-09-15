from pprint import pprint

class Prueba:

    def __init__(self, datos: list):
        self.datos = datos
    
    def get(self):
        return self.datos
    
    def put(self, dato):
        self.datos.append(dato)

datos = [
    "Toni",
    "Laura",
    "Pere"
]
print("========== Fase 1 ==========")
p1 = Prueba(datos[:])
pprint(p1.get())

p2 = Prueba(datos[:])
pprint(p2.get())

p3 = Prueba(p2.get())
pprint(p3.get())

print("========== Fase 2 ==========")

p1.put("Marc")
pprint(p1.get())
pprint(p2.get())
pprint(p3.get())

print("========== Fase 3 ==========")

p2.put("Pau")
pprint(p1.get())
pprint(p2.get())
pprint(p3.get())