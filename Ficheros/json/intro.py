""" import requests

response =requests.get('https://api.github.com')

print(response)

print(response.json())

response1 = requests.get('https://api.github.com/user/emails')
print(response1)
print(response.json()) """

import json

contactos = [('Juan Carlos','Experto en Python', 'jcptorres@hotmail.com'),
('Manuel','Experto en Python', 'manuel@hotmail.com'),
('Alma','Experto en Java', 'alma@hotmail.com')]

data=[]
for nombre, puesto,email in contactos:
    data.append({'nombre':nombre,'puesto':puesto,'email':email})

    with open('contactos.json','w') as fichero:
        json.dump(data,fichero)


