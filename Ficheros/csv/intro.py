import csv
""" contactos1 = [['Juan Carlos','Experto en Python', 'jcptorres@hotmail.com'],
['Manuel','Experto en Python', 'manuel@hotmail.com'],
['Alma','Experto en Java', 'alma@hotmail.com']]

with open('contactos1.csv', 'w',newline='\n') as csvfile:
    wr = csv.writer(csvfile, delimiter=',')
    for contacto in contactos1:
        wr.writerow(contacto) """

with open('contactos1.csv', newline='\n') as csvfile:
    wr = csv.reader(csvfile, delimiter=',')
    for nombre, titulo, email in wr:
        print(nombre, titulo, email)