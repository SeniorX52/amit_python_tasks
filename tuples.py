tuple1 = ("Hello", "Mostafa", "Abdelaziz")
tuple1 += ("Abdo","Noaman")
# To make any modifications in tuple convert it to list
list1 = list(tuple1)
list1[0] = "Yaaa"
tuple1 = tuple(list1)
print(tuple1)  # ('Yaaa', 'Mostafa', 'Abdelaziz', 'Noaman')


# Using Asterisk*
greet, first_name, *last_name=tuple1
print(greet) # Yaaa
print(first_name) # Mostafa
print(last_name) # ['Abdelaziz', 'Abdo', 'Noaman']

greet, *middle_name,last_name=tuple1
print(greet) # Yaaa
print(middle_name) # ['Mostafa', 'Abdelaziz', 'Abdo']
print(last_name) # Noaman