from io import open

texto = 'Hola Juan Carlos \n Te apuesto a que nunca habias creado un archivo de esta manera'

# Ruta donde se va a guardcar el archivo

fichero = open('hola1.txt', 'w')

# escribimos en el archivo
fichero.write(texto)

# cerramos el archivo

fichero.close()
