# Ejercicio 1
#Utilizando todo lo que sabes sobre cadenas, listas, sus métodos internos... Transforma este texto:
#un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo
# que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son 
# vuestras mentes -dijo el maestro """

texto = """un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro """
texto1 = texto.replace('#','.\n -')
texto2 = texto1.capitalize()
texto3 = texto2.replace('a.','a...')
texto4 = texto3.replace('-m','-M')
texto5 = texto4.replace('-l','-L')
texto6 = texto5.replace('-n','-N')
texto7 = texto6.replace('-dijo el maestro','-dijo el \n maestro')
print (texto7)

