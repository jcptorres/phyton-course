import json

# data

datos=[{"nombre":"Juan Carlos", "Edad":"23", "Carrera": "Contador"},
{"nombre":"Eduardo", "Edad":"43", "Carrera": "Clavadista"},
{"nombre":"Juan Carlos", "Edad":"23", "Carrera": "Diseñador"}]

# Parse o envio

data2= json.dumps(datos, ensure_ascii=False).encode('utf-8')
print (data2.decode('utf-8'))
