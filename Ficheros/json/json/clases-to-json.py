import json
from io import open

""" class Persona:
    Nombre:'Juan carlos'
    Edad: 35
    Sexo: 'Masculino'

persona = Persona()
p = json.dumps(persona)
print(p) """

class Laptop:
    def __init__(self, name, procesor, ram, hdd, cost):
        self.name = name
        self.procesor = procesor
        self.ram = ram
        self.hdd = hdd
        self.cost = cost

Laptop1 = Laptop('Asus','i5',8,1024,1000.00)
Laptop1 = Laptop('Lenovo','i7',16,2048,2000.00)

jsonStr = json.dumps(Laptop1.__dict__,indent=4, sort_keys=True)
print (jsonStr)

with open('laptop.json','w') as archivo:
    json.dump(Laptop1.__dict__,archivo, indent=4, sort_keys=)
