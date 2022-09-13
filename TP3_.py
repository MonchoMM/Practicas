from dataclasses import replace
import os, glob
from tkinter import Variable 

# Ejercicio 1
def cuantas_no (letra, archivo):
    contador = 0
    with open(archivo, "r") as file:
        for line in file:
            if line[0].upper() != str(letra).upper():
                contador += 1
    print ("Hay", contador, "linea en el archivo que no empiezan con", letra)

cuantas_no("h", "hi.txt")

# Ejercicio 2
def leer_n_lineas(archivo, lineas):
    variable = open(archivo, "r").readlines()[:lineas+1]
    print(*variable)

leer_n_lineas("hi.txt", 3)
    
# Ejercicio 3
def ultimas_lineas(archivo, ultimas):
     lineas = open(archivo, "r").readlines()[-ultimas:]
     print(*lineas)

ultimas_lineas("hi.txt", 2) 

# Ejercicio 4
def contar_palabras(arch):
    line = open(arch,"r").read()
    print("Tiene",len(line.split()),"palabras :)")

contar_palabras("hi.txt")

# Ejercicio 5
def reemplazar (arch1, arch2, letra):
    with open(arch1, "r") as file, open(arch2, "w") as file2:
        for line in file:
            file2.write(line.replace(letra, letra + "\n"))

reemplazar("hi.txt", "hi2.txt", "h")
   
# Ejercicio 6
def sacar_salto(arch1, arch2):
    with open(arch1, 'r') as file, open(arch2, 'w') as file2:
        variable = file.read()
        for elem in variable:
                if elem == '\n':
                    pass
                else:
                    file2.write(elem)

sacar_salto('hi.txt', 'hi2.txt')

# Ejercicio 7
def palabra_larga(archivo):
    file = open(archivo,"r")
    leer = file.read()
    dividir = leer.split()
    final = ""
    for palabra in dividir :
        if len(palabra) > len(final):
            final = palabra
    print("la palabra mas larga es", final, "con", len(final), "letras")

# Ejercicio 8
def agrupar(archivo1, archivo2, archivo3):
    with open(archivo1, 'r') as file, open(archivo2, 'r') as file2, open(archivo3, 'w') as file3:
        file3.write("archivo1 \n")
        file3.write(file.read())
        file3.write("\n \n archivo2 \n")
        file3.write(file2.read())

agrupar('hi.txt','hi2.txt','hi3.txt')        

# Ejercicio 9
def frecuencia(archivo):
    with open(archivo, 'r') as file:
        palabras = file.read()
        lista = palabras.split()
        dic = {}
        for palabra in lista:
            dic[palabra]=int(lista.count(palabra)) / int(len(lista))
        print(dic)

frecuencia('hi.txt')

# Ejercicio 10
def unir_txt(carpeta1, nombre):
    os.chdir(carpeta1)
    textos = glob.glob('*.txt')
    os.mkdir('Resuelto')
    with open('Resuelto/' + nombre, 'a') as salida:
        for archivo in textos:
            with open(archivo, 'r') as texto:
                salida.write(texto.read() + '\n')

unir_txt('ej 10', 'ejercicio.txt')