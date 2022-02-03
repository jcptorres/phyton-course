""" class Vehiculo:
    def __init__ (self,velocidad,kilometraje,modelo,marca):
        self.velocidad = velocidad
        self.kilometraje = kilometraje
        self.modelo = modelo
        self.marca = marca

    def capAsientos (self,asientos=4):
        return f'La capacidad de {self.marca} es de {asientos} pasajeros'
    def color (self,color='blanco'):
        return f'El color de {self.marca} es {color}'

    
class Autobus(Vehiculo,):
    def capAsientos (self,asientos=50):
        return super().capAsientos(asientos=50)

class Carro(Vehiculo):
    pass """

class Dispositvo:
    def __init__ (self,marca,modelo,pantalla,color,memoria,procesador,almacenamiento,touchscreen):
        self.marca=marca
        self.modelo=modelo
        self.pantalla=pantalla
        self.color=color
        self.memoria=memoria
        self.procesador=procesador
        self.almacenamiento=almacenamiento
        self.touchscreen=touchscreen
    
class Laptop(Dispositvo):
    pass
class Desktop(Dispositvo):
    pass
class Movil(Dispositvo):
    pass

samsung = Movil('GalaxyZ','Flip','6.7','plata','8G','SnapDragon 8000','120Gb','si')

print (samsung.touchscreen,samsung.marca,samsung.memoria,samsung.modelo)








""" mazda = Carro(120,1200,2020,'mazda')
print (mazda.velocidad,mazda.modelo,mazda.kilometraje,mazda.color()) """
    
    
    


""" vehiculox = Vehiculo (180, 10000)

print (f'La velocidad del vehiculox es {vehiculox.velocidad} y el kilometraje es {vehiculox.kilometraje}') """

""" vehiculo1 = Autobus(90,25000,2018,'Ford')
print (vehiculo1.velocidad,vehiculo1.modelo,vehiculo1.marca,vehiculo1.kilometraje)

autobusdeescuela = Autobus(100,12000,2020,'Ford')
print (autobusdeescuela.capAsientos()) """