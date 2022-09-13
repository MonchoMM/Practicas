#Ejercicio 1
#Escribir un programa que imprima la longitud de un string el cual se lee por teclado.

#Primero sacar longitud de string,

"""
def imprimir_longitud (palabra):
    longitud = len (palabra)
    print (longitud)

imprimir_longitud ("ramon")
"""

#Ejercicio 2
# Realizar un programa donde se imprima la 5ta 
# y 6ta letra de un string pasado por teclado en mayuscula (Asegurarse de que el string tenga la cantidad de caracteres suficientes).

"""
def quinta_sexta(palabra):
    #rentirngir palbras con menos de 6.
    longitud = len(palabra)
    if (longitud > 5):
        #Consguir 5ta y 6ta letra.
        quinta = palabra[4].upper()
        sexta = palabra[5].upper()
        print(quinta)
        print(sexta)
    else:
        print("invalid word")    


quinta_sexta("mariano") """

#Ejercicio 3
#Escribir un programa que pregunte el nombre y apellido al usuario y lo salude.
"""
def pregunta():
    nombre = input('Teclear nombre completo: ')
    print (f"saludos {nombre}")
    
"""

#Ejercicio 4
#Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales en mayusculas

"""
def pregunta():
    nombre = input('Teclear nombre: ')
    apellido = input('Teclear apellido: ')
    primera_N = nombre[0].upper()
    primera_A  = apellido[0].upper()
    nombre[0] = primera_N
    apellido[0] = primera_A
    print(nombre)
    print(apellido)

pregunta()
"""
#Ejercicio 5
#Realizar un programa que lea tres numeros por teclado y calcule el promedio de ellos.
"""
def lector():
    numero1 = int(input('Numero 1: '))
    numero2 = int(input('Numero 2: '))
    numero3 = int(input('Numero 3: '))
    promedio = (numero1+numero2+numero3)/3

    print(promedio)
lector() """

#Ejercicio 6
#Dada una cierta cantidad de minutos (ingresada por teclado) hacer un programa que muestre cuantas horas y minutos son. Por ejemplo 150 minutos son 2 horas y 30 minutos.

"""
def contador():
    minutos = int(input('cuantos minutos: '))
    hora = minutos/60
    resto = minutos%60  #el porcentaje sirve para ver el resto o lo que sobra
    
    print (f"Son {hora} horas y {resto} minutos ")
    

contador()    
"""

#Ejercicio 7
#Un comerciante, el cual tiene un sueldo base, recibe un 10% extra por comision por cada venta que realiza. 
# Realizar un programa que devuelva el dinero que recibira por comision luego de 4 ventas y el total de dinero que ganara ese mes, 
# teniendo en cuenta estas ventas y su sueldo base.
"""
def total_dinero():
    sueldo = 1000
    comision = (1000*10)/100
    cuatro_comision = (comision)*4
    total_sueldo = int(cuatro_comision) + int(sueldo)

    print(total_sueldo)
total_dinero() 
"""

#Ejercicio 8
#Escribir un programa para calcular la nota final de un estudiante, 
# teniendo en cuenta que por cada respuesta correcta el estudiante suma 4 puntos, 
# por cada incorrecta se le resta 1 punto y si la respuesta esta en blanco no se le suma ni se le resta.


"""

def nota_final():
    respuestas_correcta = int(input('Cuantas correctas: '))
    respuestas_incorrecta = int(input('Cuantas incorrectas: '))
    respuestas_blanco = int(input('Cuantas en blanco: '))
    contador = 4*respuestas_correcta - respuestas_incorrecta
    
    print (contador)    

nota_final()

"""