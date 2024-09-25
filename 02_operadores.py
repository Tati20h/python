###OPERADORES

print(3 + 4)
print(8 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 2)
print(10 // 3)
print(3 ** 2)

print("hola "  +   "python "  +  "¿Que tal? " )
print("hola " + str(5))
print("hola " * 5)
print("hola " * (2 ** 3))

my_float = 2.5 *2
print("Adios " * int(my_float))
 
 ##OPERADORES COMPARATIVOS## 
 #Operadores con enteros 
 
print(3 < 4)
print(3 > 4)
print(4 <= 4)
print(3 >= 4)
print(3 != 4) 
print(3 == 4)

# Operadores con cadenas de texto
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

### Operadores Lógicos ###

# Basada en el Álgebra de Boole https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4))