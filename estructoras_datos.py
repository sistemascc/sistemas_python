# acceso indice
#            0, 1, 2, 3
secuencia = [1, 3, 5, 7]
print(secuencia[2])
secuencia [2] = 10
print(secuencia [2])

# add elemento

secuencia.append(22)
print(secuencia[-1])


# Eliminar elemento
valor_eliminado = secuencia.pop(4)
print(secuencia, " ", valor_eliminado)


paises = [
    "España",
    "Ecuador",
    "México",
    "Peru",
    "Colombia",
    "venezuela"
]

#Recorrer una lista python

for elemento in paises:
    print(elemento)
print("#################   TUPLAS ##########")

# Tubla () (es inmutable, no se puede cambiar)
claves = ("123", "541")
for item in claves:
    print(item)
print("############## TUPLAS ##############")


"""
claves = ("123") en Versiones viejas se tiene que poner la , por error
print(claves[0])
"""

print("########### Diccionarios #############")

dict_country = {
"es": "España",
"ec": "Ecuador",
"mx": "México",
"pe": "Peru",
"co": "Colombia",
"ve": "Venezuala"
}

print( dict_country.get("mx"))

for key, value in dict_country.items():
    print(key, ": ", value)

## Para imprimir todas las claves que contiene el diccionario
print(dict_country.keys())


## Para imprimir todos los valores
print((dict_country.values()))

### Estructuras de control##

if "ec" in dict_country.keys():
    print(">>", dict_country.get("ec"))

res= {
    'warning': "Mensaje de aleta",
    'values': {
        "id": 158,
        "nombre": "XXGFTX NAME",
        "prince": 1245.58,
        "taxes": {
            "vat_1": 0.21,
            "vat_2": 0.4,
        },
    },
}
"""
for key, value in res.items():
    print(key, ": ", value)
    if "values" == key:
        print(value['id'])
"""
for key, value in res.items(): ### imprimir multiples valores en cadena de texto###
    print(key, ": ", value)
    if "values" == key:
        print("id: {} - name: {}".format(value.get("id"), value.get("name")))










