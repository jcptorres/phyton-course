# Ejercicio 1
# Utilizando todo lo que sabes sobre cadenas, listas, sus métodos internos... Transforma este texto:
# un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro
#
#
# en este otro:
#
#    Un día que el viento soplaba con fuerza...
#    - Mira como se mueve aquella banderola -dijo un monje.
#    - Lo que se mueve es el viento -respondió otro monje.
#    - Ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro.


texto = 'un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro'

lineas = texto.split('#')


for l, linea in enumerate(lineas):
    
    lineas[l] = linea.capitalize()
    if l == 0:
        lineas[l] = lineas[l] + '...'
    else:
        lineas[l] = '- ' + lineas[l] + '.'

for linea in lineas:
    print(linea)

