import random

def inicio():
    print(""" 
    _____________________________
    Iniciemos:
    _____________________________

    El Jugador1 debe de capturar:
    0 para elegir Piedra
    1 para elegir Papel y
    2 para elegir Tijera,
            
    Depues le tocara al Jugador2 o a la PC capturar una opción y
    Por último se deplegara al ganador""")

def opcion1():
    print (inicio())
    entradajug1 = int(input("Jugador1 selecciona la opción >>> "))
    if entradajug1 in range(3):
        if entradajug1 == 0:
            print("Jugador 1 eligio Piedra")
        elif entradajug1 == 1:
            print("Jugador 1 eligio Papel")
        elif entradajug1 == 2:
            print("Jugador 1 eligio Tijera")
    else:
        print('La opción del jugador 1 no es valida')
    
    pc = random.randrange(0,3)
    if pc == 0:
        print("PC eligio Piedra")
    elif pc == 1:
        print("PC eligio Papel")
    elif pc == 2:
        print("PC eligio Tijera")

    if entradajug1 == 1 and pc == 0:
            print ('Papel envuelve a Piedra, gana Papel')
    elif entradajug1 == 1 and pc == 1:
            print ('Papel es igual a Papel, nadie gana')
    elif entradajug1 ==1 and pc == 2:
            print ('Papel es cortado por Tijera, gana Tijera')
    elif entradajug1 == 0 and pc == 0:
            print ('Piedra es igual a Piedra, nadie gana')
    elif entradajug1 == 0 and pc == 2:
            print ('Piedra destruye Tijera, gana Piedra')
    elif entradajug1 == 0 and pc == 1:
            print ('Piedra es envuelto por Papel, gana Papel')
    elif entradajug1 == 2 and pc == 2:
            print ('Tijera es igual a Tijera, nadie gana')
    elif entradajug1 ==2 and pc == 1:
            print ('Tijera corta Papel, gana Tijera')
    elif entradajug1 ==2 and pc== 0:
            print ('Tijera es destruida por Piedra, gana Piedra')


def opcion2():
    print (inicio())
    entradajug1 = int(input("Jugador 1 selecciona la opcion >>> "))
    if entradajug1 in range(3):
        if entradajug1 == 0:
            print("Jugador 1 eligio Piedra")
        elif entradajug1 == 1:
            print("Jugador 1 eligio Papel")
        elif entradajug1 == 2:
            print("Jugador 1 eligio Tijera")
    else:
        print('La opción del jugador 1 no es valida')
    
    entradajug2 = int(input("Jugador 2 selecciona la opcion >>> "))
    if entradajug2 in range(3):
        if entradajug2 == 0:
            print("Jugador 2 eligio Piedra")
        elif entradajug2 == 1:
            print("Jugador 2 eligio Papel")
        elif entradajug2 == 2:
            print("Jugador 2 eligio Tijera")

    if entradajug1 == 1 and entradajug2 == 0:
            print ('Papel envuelve a Piedra, gana Papel')
    elif entradajug1 == 1 and entradajug2 == 1:
            print ('Papel es igual a Papel, nadie gana')
    elif entradajug1 ==1 and entradajug2 == 2:
            print ('Papel es cortado por Tijera, gana Tijera')
    elif entradajug1 == 0 and entradajug2 == 0:
            print ('Piedra es igual a Piedra, nadie gana')
    elif entradajug1 == 0 and entradajug2 == 2:
            print ('Piedra destruye Tijera, gana Piedra')
    elif entradajug1 == 0 and entradajug2 == 1:
            print ('Piedra es envuelto por Papel, gana Papel')
    elif entradajug1 == 2 and entradajug2 == 2:
            print ('Tijera es igual a Tijera, nadie gana')
    elif entradajug1 ==2 and entradajug2 == 1:
            print ('Tijera corta Papel, gana Tijera')
    elif entradajug1 ==2 and entradajug2== 0:
            print ('Tijera es destruida por Piedra, gana Piedra')

def intro():
    print ("""
    _____________________________________________
    Bienvenido al juego de Piedra, Papel o Tijera
    _____________________________________________

    Elige una opción:
    1. jugar vs la computadora
    2. jugar vs otro participante
    0. Salir
    """)

    entrada_usuario = int(input("Seleccione una opcion: "))
    if entrada_usuario in range(3):
        if entrada_usuario == 0:
            print("Adios! Vuelva pronto")
        elif entrada_usuario == 1:
            print (opcion1())
        elif entrada_usuario == 2:
            print (opcion2())
            

print (intro())