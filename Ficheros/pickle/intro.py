import pickle
#Guardad lo qu queramos en colecciones
l=[1,2,3,4,5]
fichero = open('fichero.pckl', 'wb')
pickle.dump(l,fichero)
fichero.close()

fichero = open('fichero.pckl','rb')
lFichero = pickle.load(fichero)
print(lFichero)
fichero.close()