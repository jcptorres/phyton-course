import suma
import resta
import multiplicacion
import division


print("\n")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Salir")
print("\n")

while True:
    opcion = int(input("Ingrese la opcion que desea realizar >>> "))
    if opcion == 1:
        suma.operador1
        suma.operador2
        print (suma.suma())
    elif opcion == 2:
        suma.operador1
        suma.operador2
        print (resta.resta())
    elif opcion == 3:
        suma.operador1
        suma.operador2
        print (multiplicacion.multiplicar())
    elif opcion == 4:
        suma.operador1
        suma.operador2
        print (division.division())
    elif opcion == 5:
        break
    else:
        print("\n")
        print("La opcion ingresada no es valida")
        print("\n")

