











""" class Persona: #definir como se va a llamar la clase
    def inicializar(self,nombre):
        self.nom= nombre
    def mostrar(self):
        print('Nombre:',self.nom)

persona1 = Persona()
persona1.inicializar('Juan Carlos')
persona1.mostrar() """

""" class Muffin:
    def __init__(self,sabor,cobertura):
        self.sabor = sabor
        self.cobertura = cobertura
    
       
    def __str__(self):
        return f'sabor: {self.sabor} \ncobertura: {self.cobertura}'

chocolate = Muffin ('chocolate','glaseado de fresa')
print (chocolate) """

""" class Ticket:
    def __init__(self,numero_ticket,subtotal,iva,total):
        self.numtic = numero_ticket
        self.subt = subtotal
        self.iva = iva
        self.total = total
    
    def __str__(self):
        return f'Número de Ticket: {self.numtic} \n Subtotal: {self.subt} \n IVA: {self.iva} \n Total: {self.total}'

concierto = Ticket ('A509', 1000,160,1160)
print (concierto) """

""" 
class Mascota:
    def __init__(self,tipo,nombre,nacimiento,fechavacuna,tipovacuna,numregistro,idregistro):
        self.tipo = tipo
        self.nombre = nombre
        self.nacimiento = nacimiento
        self.fechavacuna = fechavacuna
        self.tipovacuna = tipovacuna
        self.numregistro = numregistro
        self.idregistro = idregistro

    def __str__(self):
        return f'Tipo de Mascota: {self.tipo} \nNombre de Mascota: {self.nombre} \nFecha de Nacimiento: {self.nacimiento} \nFecha de Vacunación: {self.fechavacuna} \nTipo de Vacuna {self.tipovacuna} \nNúmero de registro: {self.numregistro} \nID Registro: {self.idregistro}'

mascota = Mascota ('Perro','Archie','2 de Nov 2020','15 de Marzo 2021','Rabia',123500,'CDMX15890')
print (mascota)
 """

# Clase 17Nov21

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'{self.name} is {self.age} years old'
    def sound(self,sound):
        self.sound=sound
        return f'{self.name} says{self.sound}'
    

dog = Dog('Archie',12)
info = dog.info()
print (info)



class Dog:
    specie = 'Canis familiaris'

    def __init__