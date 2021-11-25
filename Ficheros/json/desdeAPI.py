import requests
import json

response = requests.get('https://api.github.com')

print(response)

""" print(response.json()) """
inp = response.json()
print(inp)
data=[]
for d,e in inp.items():
    data.append({'name':d,'value':e})

with open('github.json','w') as f:
    json.dump(data,f)


    