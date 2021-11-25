import csv

contactos = ('Juan Carlos','Experto en Python', 'jcptorres@hotmail.com'),
""" ('Manuel','Experto en Python', 'manuel@hotmail.com'),
('Alma','Experto en Java', 'alma@hotmail.com'))

with open('contactos2.csv','w',newline='\n')as f:
    campos = ['nombre','profesion','email']
    writer = csv.DictWriter(f,fieldnames=campos)
    writer.writeheader()
    for nombre,profesion,email in contactos:
        writer.writerow({'nombre':nombre,'profesion':profesion,'email':email}) """
    
with open('contactos.csv',newline='\n') as f:
    reader = csv.DictReader(f)
    for contacto in reader:
        print(contacto['nombre'],contacto['email'],contacto['profesion'])
