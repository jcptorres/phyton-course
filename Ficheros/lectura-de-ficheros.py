from io import open

#Ruta de donde quiero leer el fichero
fichero1 = open('hola1.txt', 'r')
fichero2 = open('phyton-course/Ficheros/hola.txt', 'r')
with open('phyton-course/Ficheros/hola.txt','r') as f3:
    for linea in f3:
        print(f'--{linea}')
#Lectura completa del fichero
textohola = fichero1.read()
textohola2 = fichero2.readlines()
# Cerrar fichero
fichero1.close()
fichero2.close()

print (textohola)
print (textohola2)
print (textohola2[2])