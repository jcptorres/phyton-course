""" from suma import suma
from resta import resta
from multiplicacion import multiplicar
from division import division

# crear ciclo while para que el usuario pueda realizar mas operaciones
while True:
    print("\n")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("\n")
    opcion = int(input("Ingrese la opcion que desea realizar >>> "))
    if opcion == 1:
        operador1 = int(input("Ingrese el primer numero a sumar >>> "))
        operador2 = int(input("Ingrese el segundo numero a sumar >>> "))
        suma(operador1, operador2)
    elif opcion == 2:
        operador1 = int(input("Ingrese el primer numero a restar >>> "))
        operador2 = int(input("Ingrese el segundo numero a restar >>> "))
        resta(operador1, operador2)
    elif opcion == 3:
        operador1 = int(input("Ingrese el primer numero a multiplicar >>> "))
        operador2 = int(input("Ingrese el segundo numero a multiplicar >>> "))
        multiplicar(operador1, operador2)
    elif opcion == 4:
        operador1 = int(input("Ingrese el primer numero a dividir >>> "))
        operador2 = int(input("Ingrese el segundo numero a dividir >>> "))
        division(operador1, operador2)
    elif opcion == 5:
        break
    else:
        print("\n")
        print("La opcion ingresada no es valida")
        print("\n") """


# Modulo encargado de realizar operaciones matematicas

# importar todo el archivo con todo lo quentenga (funciones, clases, etc)
#  import suma

# importar unicamente la funcion que necesito

from suma import operacionSuma
from resta import operacionResta
from multiplicacion import operacionMultiplicacion
from division import operacionDivision

# crear ciclo while para que el usuario pueda realizar mas operaciones
while True:
    print("\n")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("\n")
    opcion = int(input("Ingrese la opcion que desea realizar >>> "))
    if opcion == 1:
        n1 = int(input("Ingrese el primer numero a sumar >>> "))
        n2 = int(input("Ingrese el segundo numero a sumar >>> "))
        operacionSuma(n1, n2)
    elif opcion == 2:
        n1 = int(input("Ingrese el primer numero a restar >>> "))
        n2 = int(input("Ingrese el segundo numero a restar >>> "))
        operacionResta(n1, n2)
    elif opcion == 3:
        n1 = int(input("Ingrese el primer numero a multiplicar >>> "))
        n2 = int(input("Ingrese el segundo numero a multiplicar >>> "))
        operacionMultiplicacion(n1, n2)
    elif opcion == 4:
        n1 = int(input("Ingrese el primer numero a dividir >>> "))
        n2 = int(input("Ingrese el segundo numero a dividir >>> "))
        operacionDivision(n1, n2)
    elif opcion == 5:
        break
    else:
        print("\n")
        print("La opcion ingresada no es valida")
        print("\n")