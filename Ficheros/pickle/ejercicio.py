import pickle

class Persona:
    def __init__(self,nombre):
        self.nombre = nombre
    def __str__(self):
        return self.nombre
#Crear la colección de objetos

nombres = ['Juan','Pedro','Ana','Maria']
personas = []

for nombre in nombres:
    p = Persona(nombre)
    personas.append(p)

f = open('personas.dat','wb')
pickle.dump(personas,f)
f.close()

f = open('perosnas.pckl','wb')
pickle.dump(personas,f)
f.close()

for p in personasf:
    print(p)

a = open('personas.pckl', 'wb')
personasa = pickle.load(a)
a.close


