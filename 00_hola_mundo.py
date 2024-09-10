print("Hola mundo gay")
print(type("Hola mundo gay"))

"""
# Este es un comentario de una sola línea


Este es un comentario
de varias líneas


# Indentación


 En Python, la indentación (espacios o tabulaciones al inicio de una línea)
 se utiliza para delimitar bloques de código. 
 A diferencia de otros lenguajes que utilizan llaves o palabras clave,
 Python utiliza la indentación para determinar el alcance de las declaraciones.

#Por ejemplo: 

if condition:
    # Bloque de código si la condición es verdadera
    
    instrucción1
    instrucción2

else:

    # Bloque de código si la condición es falsa

    instrucción3
    instrucción4


#Tipos de datos básicos
Enteros (int)
"""
print(type(5))
"""
edad = 25
cantidad = 100


Flotantes (float)
"""
print(type(1.5))
"""
precio = 100.50
peso = 80.5

Booleanos (bool)

"""
print(type(True))
"""
es_mayor = True
es_menor = False


 #Variables 
 #Declaración y asignación de variables

nombre = "Juan"
edad = 25
altura = 1.75
es_estudiante = True

a = b = c = 10


   #Normas para nombrar variables

   1. Las variables deben comenzar con una letra o un guión bajo (_).

   2. Las variables no pueden comenzar con un número.

   3. Las variables solo pueden contener caracteres alfanuméricos y guiones bajos (_).   

#  ejemplo 
"""
print(type("Hola mundo gay"))

"""

edad
nombre_completo
total_ventas
_contador
 
#Aritméticos
 """
print(type(1+5j))
"""
Suma (+): suma dos valores.
Resta (-): resta el segundo valor del primero.
Multiplicación (*): multiplica dos valores.
División (/): divide el primer valor por el segundo y devuelve un resultado de tipo flotante.
División entera (//): divide el primer valor por el segundo y devuelve un resultado de tipo entero (se descarta la parte decimal).
Módulo (%): devuelve el resto de la división entre el primer valor y el segundo.
Exponenciación (**): eleva el primer valor a la potencia del segundo.

#Ejemplos:

a = 10
b = 3

suma = a + b   # 13
resta = a - b    # 7
multiplicacion = a * b    # 30
division = a / b   # 3.333333333
división_entera = a // b   # 3
modulo = a % b   # 1
exponenciacion = a ** b   # 1000
 
#De comparación


Igual a (==): devuelve True si ambos valores son iguales.
Diferente de (!=): devuelve True si los valores son diferentes.
Mayor que (>): devuelve True si el primer valor es mayor que el segundo.
Menor que (<): devuelve True si el primer valor es menor que el segundo.
Mayor o igual que (>=): devuelve True si el primer valor es mayor o igual que el segundo.
Menor o igual que (<=): devuelve True si el primer valor es menor o igual que el segundo.
Ejemplos:

a = 10
b = 3

igual = a == b   # False
diferente = a != b   # True
mayor que = a > b   # True
menor que = a < b   # False
mayor o igual = a >= b   # True
menor o igual = a <= b   # False


#Lógicos

AND (and): devuelve True si ambas condiciones son verdaderas.
OR (or): devuelve True si al menos una de las condiciones es verdadera.
NOT (not): invierte el valor de una condición, devuelve True si la condición es falsa y False si la condición es verdadera.
Ejemplo:

a = 10
b = 3


resultado_and = (a > 5) and (b < 5)   # True
resultado_or = (a > 15) or (b < 5)   # True
resultado_not = not (a > 5)   # False

 #Estructuras de control   
 #Estructuras condicionales    
 
 IF
La estructura if se utiliza para ejecutar un bloque de código si una condición es verdadera. La sintaxis básica es la siguiente:

if condicion:

   # Bloque de código a ejecutar si la condición es verdadera
   instrucciones
Ejemplo:

edad = 18


if edad >= 18:
   print ("Eres mayor de edad.")
En este ejemplo, si la variable edad es mayor o igual a 18, se ejecutará el bloque de código dentro del if y se imprimirá el mensaje "Eres mayor de edad."

 

IF-ELSE
La estructura if-else nos permite especificar un bloque de código alternativo que se ejecutará si la condición del if es falsa. La sintaxis básica es la siguiente:

edad = 15


if edad >= 18:
   print ("Eres mayor de edad.")

else:
   print ("eres menor de edad.")
En este ejemplo, si la variable edad es mayor o igual a 18, se ejecutará el bloque de código dentro del if y se imprimirá el mensaje "Eres mayor de edad." De lo contrario, se ejecutará el bloque de código dentro del else y se imprimirá el mensaje "Eres menor de edad."

 

IF-ELIF-ELSE
La estructura if-elif-else nos permite especificar múltiples condiciones y bloques de código alternativos. La sintaxis básica es la siguiente:

if condicion1:

   # Bloque de código a ejecutar si la condicion1 es verdadera
   instrucciones

elif condicion2:

   # Bloque de código a ejecutar si la condicion2 es verdadera
   instrucciones

else:

   # Bloque de código a ejecutar si ninguna condición anterior es verdadera
   #instrucciones
#Ejemplo:
"""

calificacion = 85


if calificacion >= 90:
   print ("Excelente")

elif calificacion >= 80:
   print ("Muy bueno")

elif calificacion >= 70:
   print ("Bueno")

else:
   print ("Necesita mejorar"),


edad = 20


if edad < 18:
   print ("Eres mennor de edad.")

elif edad >= 18 and edad < 60:
    print ("Eres unn adulto")

elif edad > 15:
    print("Mayor de 15 años")

elif edad == 60:
    print("Feliz 60 años")

else:
    print("Eres adulto mayor")        

"""
#Bucles/loops

 """
#For

#for variable in secuencia:

    # Bloque de código a repetir
    #instrucciones
#Ejemplo:

frutas = ["manzana", "banana", "naranja"]


for fruta in frutas:
    print(fruta)

#En este ejemplo, el bucle for itera sobre la lista frutas. En cada iteración, la variable fruta toma el valor de un elemento de la lista, y se ejecuta el bloque de código dentro del bucle. En este caso, se imprime cada fruta en una línea separada.
 
#While

#while condicion:

    # Bloque de código a repetir
    #instrucciones
#Ejemplo:
print("Numeros del 1 al 5 multiplocapds por 2 con Blucle for ")
for numero in range(1, 6):
    print(numero * 2)
         
         
print("Numeros del 1 al 5 multiplocapds por 2 con Blucle while ")
contador = 1
while contador <= 5:
    print(contador * 2)
    contador += 1

#While

contador = 0


while True:

    print(contador)
    contador += 1


    if contador == 5:
        break
    
#Continue
for i in range(10):

    if i % 2 == 0:
        continue
    print(i)
    
#Pass
for i in range(5):
    pass


#Estructuras de datos
#Listas

"""
frutas = ["manzana", "banana", "naranja"]
Para acceder a los elementos de una lista, utiliza el índice del elemento entre corchetes. Los índices comienzan desde 0.

print(frutas[0])  # Imprime "manzana"
print(frutas[1])  # Imprime "banana"
print(frutas[2])  # Imprime "naranja"
También puedes acceder a los elementos desde el final de la lista utilizando índices negativos. El índice -1 representa el último elemento, -2 representa el penúltimo, y así sucesivamente.

print(frutas[-1])  # Imprime "naranja"
print(frutas[-2])  # Imprime "banana"
print(frutas[-3])  # Imprime "manzana"


"""

frutas = ["manzana", "banana", "naranja"]


frutas.append("pera")
print(frutas)  # Imprime ["manzana", "banana", "naranja", "pera"]


frutas.insert(1, "uva")
print(frutas)  # Imprime ["manzana", "uva", "banana", "naranja", "pera"]


frutas.remove("banana")
print(frutas)  # Imprime ["manzana", "uva", "naranja", "pera"]


fruta_eliminada = frutas.pop(2)
print(frutas)  # Imprime ["manzana", "uva", "pera"]
print(fruta_eliminada)  # Imprime "naranja"


frutas.sort()
print(frutas)  # Imprime ["manzana", "pera", "uva"]


frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "manzana"]


#Listas de comprensión

#nueva_lista = [expresion for elemento in secuencia if condicion]
#Ejemplo:

numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(cuadrados)  # Imprime [4, 16]


 #Diccionarios
"""
Creación y acceso
Para crear un diccionario, utiliza llaves y separa las claves y valores con dos puntos.

persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

Para acceder a los valores de un diccionario, utiliza la clave correspondiente entre corchetes:

print(persona["nombre"])  # Imprime "Juan"
print(persona["edad"])    # Imprime 25
print(persona["ciudad"])  # Imprime "Madrid"
También puedes utilizar el método get() para obtener el valor de una clave. Si la clave no existe, devuelve un valor predeterminado (por defecto, None).

#Métodos de diccionarios

keys(): devuelve una vista de todas las claves del diccionario.
values(): devuelve una vista de todos los valores del diccionario.
items(): devuelve una vista de todos los pares clave-valor del diccionario.
update(otro_diccionario): actualiza el diccionario con los pares clave-valor de otro diccionario.
Ejemplo:
"""
persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}


print(persona.keys())    # Imprime dict_keys(["nombre", "edad", "ciudad"])
print(persona.values())  # Imprime dict_values(["Juan", 25, "Madrid"])
print(persona.items())   # Imprime dict_items([("nombre", "Juan"), ("edad", 25), ("ciudad", "Madrid")])


persona.update({"profesion": "Ingeniero"})
print(persona) 
# Imprime {"nombre": "Juan", "edad": 25, "ciudad": "Madrid", "profesion": "Ingeniero"}


#Conjuntos (set)
frutas = {"manzana", "banana", "naranja"}


frutas.add("pera")
print(frutas)  # Imprime {"manzana", "banana", "naranja", "pera"}


frutas.remove("banana")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}


frutas.discard("uva")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}


frutas.clear()
print(frutas)  # Imprime set()

#FUNCIONNNES
#Definición y llamada de funciones
#Para definir una función en Python, utilizamos la palabra clave def seguida del nombre de la función y paréntesis. 

def saludo():
    print("¡Hola, mundo!")

saludo()

#Parámetros y argumentos

def saludo(nombre):
    print(f"¡Hola, {nombre}!")

saludo("Juan")  # Imprime "¡Hola, Juan!"
saludo("María")  # Imprime "¡Hola, María!"

#Valores de retorno
def suma(a, b):
    return a + b


resultado = suma(3, 4)
print(resultado)  # Imprime 7   

#Funciones anónimas (lambda)

cuadrado = lambda x: x ** 2
print(cuadrado(5))  # Imprime 25


#Alcance de las variables (local vs. global)

variable_local = 10
def funcion():
    print(variable_local)  # Accesible dentro de la función


variable_global = 20

def funcion2():
    print(variable_global)  # Accesible desde cualquier lugar

funcion()  # Imprime 10
funcion2()  # Imprime 20
print(variable_global)  # Imprime 20
print(variable_local)  # Genera un error, la variable no está definida en este alcance.

#Funciones definidas por el usuario

def calcular_media(*numeros):
    suma = sum(numeros)
    cantidad = len(numeros)
    media = suma / cantidad
    return media

print("Media:", calcular_media(10, 20, 30, 40))


def sumar_3(x):
    return x + 3

sumar = lambda x: x + 3

print ("Sumarle 3 a un numero", sumar(5))


#Documentación de funciones (docstrings)


def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.


    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.


    Returns:
        float: El área del rectángulo.
    """
    return base * altura
#Funciones con número variable de argumentos

def suma_variable(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


print(suma_variable(1, 2, 3))  # Imprime 6
print(suma_variable(4, 5, 6, 7))  # Imprime 22

# Manejo de errores y excepciones
#Error de sintaxis (SyntaxError)
#Error de nombre (NameError
#Error de tipo (TypeError)
#Error de índice (IndexError)

#Manejo de excepciones

#Try

try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")


#Except

try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")
except ValueError:
    print("Error: Valor inválido")


#Finally
"""
try:
    # Código que puede generar una excepción
    archivo = open("archivo.txt", "r")
    # Realizar operaciones con el archivo
except FileNotFoundError:
    print("Error: Archivo no encontrado")
finally:
    archivo.close()  # Cerrar el archivo siempre, incluso si ocurre una excepción
"""
#Excepciones personalizadas    
"""
def funcion():
    # Código que puede generar una excepción personalizada
    if condicion:
        raise Exception("Descripción del error")


try:
    funcion()
except Exception as e:
    print(f"Error: {str(e)}")

    """

# Entradas/salidas
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")


print("Hola, " + nombre + "!")
print("Tienes " + edad + " años.")


edad = int(input("Ingresa tu edad: "))


if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

#Salida de datos
nombre = "Juan"
edad = 25


print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")

#Lectura y escritura de archivos
"""
archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()
"""
#Escritura de archivos

archivo = open("datos.txt", "w")
archivo.write("Hola, mundo!")
archivo.close()

#Importar módulos

import math


resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0

from math import sqrt


resultado = sqrt(25)
print(resultado)  # Imprime 5.0

#Funciones y clases de módulos estándar
import random
import datetime


numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime un número entero aleatorio entre 1 y 10


fecha_actual = datetime.datetime.now()
print(fecha_actual)  # Imprime la fecha y hora actual

#Creación de módulos propios
#Crear y utilizar módulos personalizados

import  mi_modulo 

mi_modulo.saludar("Juan")  # Imprime "Hola, Juan!"
resultado = mi_modulo.calcular_suma(5, 3)
print(resultado)  # Imprime 8


import operaciones
import utilidades


resultado = operaciones.sumar(5, 3)
utilidades.imprimir_mensaje(f"El resultado de la suma es: {resultado}")


nombre = utilidades.obtener_nombre_usuario()
utilidades.imprimir_mensaje(f"Hola, {nombre}!")


(not True) or (False and True) 