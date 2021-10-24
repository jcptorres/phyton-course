class Juego:
    def __init__ (self,pi,pa,ti):
        self.pi = pi
        self.pa = pa
        self.ti = ti

        if jugador1== pa and jugador2 == pi:
            print ('Papel envuelve a Piedra, gana Papel')
        elif jugador1== pa and jugador2 == pa:
            print ('Papel es igual a Papel, nadie gana')
        elif jugador1==pa and jugador2== ti:
            print ('Papel es cortado por Tijera, gana Tijera')
        elif jugador1== pi and jugador2== pi:
            print ('Piedra es igual a Piedra, nadie gana')
        elif jugador1== pi and jugador2== ti:
            print ('Piedra destruye Tijera, gana Piedra')
        elif jugador1== pi and jugador2== pa:
            print ('Piedra es envuelto por Papel, gana Papel')
        elif jugador1== ti and jugador2 == ti:
            print ('Tijera es igual a Tijera, nadie gana')
        elif jugador1==ti and jugador2 == pa:
            print ('Tijera corta Papel, gana Tijera')
        elif jugador1==ti and jugador2== pi:
            print ('Tijera es destruida por Piedra, gana Piedra')

class Jugando:
    def __init__ (self,jugador1, jugadorjugador2):
        self.jugador1 = jugador1
        self.jugadorjugador2 = jugadorjugador2

def iniciar():
    print("_____________________________________________")
    print("Bienvenido al juego de Piedra, Papel o Tijera")
    print("_____________________________________________")
    print()
    print("Elige contra quien jugar:")
    print("1. jugar vs la computadora")
    print("2. jugar vs otro participante")
    print("0. Salir")
    print()


def intro():
    while True:
        iniciar()
        try:
            entrada_usuario = int(input("Seleccione una opcion: "))
            if entrada_usuario in range(3):
                if entrada_usuario == 0:
                    print("Adios! Vuelva pronto")
                    break
                    print()
                elif entrada_usuario == 1:
                    print("Usted eligió la opcion {} !\n".format(entrada_usuario))
                    break
                elif entrada_usuario == 2:
                    print(""" Iniciemos:
                    El Jugador1 debe de capturar:
                    1 para elegir Piedra
                    2 para elegir Papel y
                    3 para elegir Tijera,
                    Depues le tocara al jugador2 y
                    por último se deplegara al ganador""")
            else:
                print('Error, solo de aceptan numeros del 0 al jugador2')
        except ValueError:
            print("Error, ingrese solamente numeros")
                
print(intro())
