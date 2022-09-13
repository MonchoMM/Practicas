import re

# Ejercicio 1
def caracteres_permitidos(string):
    return bool(re.search("[a-zA-Z0-9]",string))

# Ejercicio 2
def todos_caract_permitidos(string):
    return not bool(re.search("[^a-zA-Z0-9]",string))

# Ejercicio 3
def encontrar_patron(string):
    patron = "he*"
    if re.search(patron, string) is not None:
        return "Se encontró el patrón"
    else: 
        return"No se encontró patrón"

def encontrar_patron(string):
    patron = "he+"
    if re.search(patron, string) is not None:
        return "Se encontró el patrón"
    else: 
        return"No se encontró patrón"

#repito
def encontrar_patron(string):
    patron = "he{2,3}"
    if re.search(patron, string) is not None:
        return "Se encontró el patrón"
    else: 
        return"No se encontró patrón" 

# Ejercicio 4
def palabras_u(string):
    patron = "^[a-z]+_[a-z]+$"
    if re.search(patron, string) is not None:
        return "Se encontró el patrón"
    else: 
        return"No se encontró patrón" 

# Ejercicio 5
def numero_especifico(numero, string):
    if re.match(str(numero),string) is not None:
        return "Empieza con numero"
    else:
        return "No empieza con numero"

# Ejercicio 6
def frase_en_lista(frase, lista):
    for elem in lista:
        if re.search(elem,frase) is  None:
            return "String no se encuentra en la frase"
    else:
        return "Todos los strings en la frase"
print(frase_en_lista("hola mundo", ["hola","casa"]))

def solo (string):
    bool(re.search("[a-zA-Z0-9]",string)) #le falta, no se como poner espacios y que no tenga mas cosas

# Ejercicio 7
# Ejercicio 8
# Ejercicio 9
# Ejercicio 10
# Ejercicio 11
# Ejercicio 12
# Ejercicio 13
# Ejercicio 14
# Ejercicio 15