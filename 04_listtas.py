## LISTAS ##

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [29, 28, 23, 30, 30, 59, 86]
print(my_list)

my_other_list = [29, 1,58 ,"Lucy", "Hernanndez"]

print(type(my_other_list))
print(type(my_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-3])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_other_list[-1])
print(my_other_list.count(30))
print(my_list.count(30))
#print(my_other_list[4]) Index error
#print(my_other_list[-1]) Index error 

#age, tall, name, surname = my_other_list
#print(name)

name, tall, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[-1]
print(age)

print(my_list + my_other_list)
#print(my_list - my_other_list)

my_other_list.append("LucyMaria")
print(my_other_list)

my_other_list.insert(1,"Verde")
print(my_other_list)

my_other_list[1] = "rojo"
print(my_other_list)

my_other_list.remove("rojo")
print(my_other_list)

my_list.remove(30)
print(my_list)

my_list.pop()
print(my_list)

print(my_list.pop())
print(my_list)

print(my_list.pop(2))
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

"""
del my_list[2]
print(my_list)
"""

my_new_list = my_list.copy
print(my_new_list)

my_list.clear
print(my_list)

"""
my_new_list.reverse()
print(my_new_list)
"""

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:2])

my_list = "hola python"
print(my_list)
print(type(my_list))

