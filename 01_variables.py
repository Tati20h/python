# variables

my_string_variable = "Hello World"
print(my_string_variable)

my_integer_variable = 10
print(my_integer_variable)

my_float_variable = 10.5
print(my_float_variable)

my_boolean_variable = True
print(my_boolean_variable)

#concatenación de variables en un print
print(my_string_variable, my_integer_variable, my_boolean_variable)
print("Este este es el valor de :", my_boolean_variable)


my_integer_to_str_variable = str(my_integer_variable)
print(my_integer_to_str_variable)
print(type(my_integer_to_str_variable))

#funciones del sistema 

print(len(my_string_variable))

#Variables en una sola linea 

name, submane, alias, age = "Lucy","Hernández","la Tufis" ,29
print("Mi nombre es :",name,submane,".Tengo",age ," años de edad " ,"y mi alias es:",alias)

#input
""""
first_name = input('whatsn is your name:')
age = input('how old are you?')


print(first_name)
print(age)
"""
#Cambiamos su tipo 
name= 29
age="Lucy"

print(name)
print(age)

#¿Forzamps el tipo?
Address : str = "Mi direccion"
Address = "234"

print(type(Address))