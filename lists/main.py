my_list = ["String", 10, 14.5, True]
print (my_list)

# Get element
first_element = my_list[0]
print(first_element)

# Updaate element
my_list[-1] = False
print (my_list)

# Sublist
# [start:end]
# [start:] obtenemos los ultimos elementos de la lista
# [:end] obtenemos los primeros elementos de la lista
# [start:end:skip] para solo obtener los saltos necesarios
sub_list = my_list[0:2]
print (sub_list)

# Add elements to end of list
my_list.append('MongoDB')
print(my_list)

# Get list length
print(len(my_list))

# Insert with inde reference
my_list.insert(2, 'Rails')
print(my_list)

#Etend list
my_second_list = ["Docker", 'Jenkings']
my_list.extend(my_second_list)
print(my_list)

# Remove elements
my_list.remove('MongoDB')
print(my_list)

del my_list[4]
print(my_list)

#Remove all elements on my list
my_list.clear()
print(my_list)
