from io import open

fichero = open ('hola1.txt', 'r')

fichero.seek(0) #manejar la posición del puntero
print (fichero.read(7)) # read y el número x en parentesis indico que el cursos lea x números de caracteres

fichero.seek(0)
fichero.seek(len(fichero.readline()))

print(fichero.read())
