### STRING

my_string = "Mi String"
my_other_string = "Mi otro String"

print(len(my_string)) 
print(len(my_other_string)) 

print( my_string + "" + my_other_string)

my_new_string = "Este es un string\ncon salto de linea"
print(my_new_string)

my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)

my_scape_string = "\tEste es un string\nescapado"
print(my_scape_string)

#FORMATEO
apellido,name,age = "Hernández","Lucy",29

print("Mi nombre es {} {} , y mi edad es {}" .format(name, apellido, age))
print("Mi nombre es %s %s , y mi edad es %d" %(name, apellido, age ))

print("Mi nombre es " + name + " " + apellido + "y mi edad es" + str(age))

print(f"Mi nombre es {name} {apellido}, y mi edad es {age}")

#DESMPAQUEETADO DE CARACTEERES 
languaje = "python"
a, b, c, d, e, f = languaje
print(a)
print(e)

# Division
languaje_slice = languaje[1:3]
print(languaje_slice)

languaje_slice = languaje[1:]
print(languaje_slice)

#Reverse 

reverse_languaje = languaje[:: -1]
print(reverse_languaje)