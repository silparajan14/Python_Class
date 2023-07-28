#Dictionary : in python it is a collection of key value pairs
#changable , ie, mutable
#represent using { }
#duplicates are not allowed
#syntax :
#dict = {'key1': 'value1','key2': 'value2',.........}
person = {
    'name' : 'alex',
    'age' : 24,
    'phn' : 125345621
}
# print(person)
# print(len(person))
# print(type(person))

# #access keys (only) :
# print(person.keys())
#
# #access values (only) :
# print(person.values())

#dict iteration :
#for getting only values
# for i in person.values():
#     print(i)

#for getting only keys
# for i in person:
#     print(i)

#iterating both
#i = keys, j = values
# for i,j in person.items():
#     print(i,j)

#accessing items :
# x = person['name']
# print(x)

#from user
# key = input("Enter the key : ")
# x = person[key]
# print(x)

#get method : get()
# x = person.get('name')
# print(x)

#update() :
# person.update({'age': '26'})
# print(person)

#from user : we can add new key and values or update existing keys and values(numbers will be stored as str)
# key = input("enter the field to update : ")
# value = input("Enter the new value : ")
# person.update({key:value})
# print(person)

#updating without using update function(numbers will be stored as int)
# person['age'] = 25
# print(person)

#to add new keys and values
# person['height'] = 155
# print(person)

#pop() : to remove a pair of data using keys
# person.pop('age')
# print(person)

#popitem() : to remove a pair from last position of a dictionary

#clear() : clearing only keys and values
# person.clear()
# print(person)

#work
# dict = {}
# n = int(input("Enter the number of key value pairs : "))
# for i in range(n):
#     key = input("Enter the key : ")
#     value = input("Enter the value : ")
#     dict.update({key:value})
# print(dict)

#create a empty dict name employee.By user input add keyvalue pairs : emp_name, id, salary, designation.print the dict
#itterate the dictionary ,print type of each values
# employee = {}
# n = int(input("Enter the number of key value pairs : "))
# for i in range(n):
#     key = input("Enter the key : ")
#     value = input("Enter the value : ")
#     if(value.isdigit()):
#         employee.update({key:int(value)})
#     elif(value.isalpha()):                     #input cannot contain space as it is spcl character
#         employee.update({key:value})
#     else:
#         employee.update({key:float(value)})
# print(employee)
# for i in employee.values():
#     print(type(i))

# input can contain space as it is spcl character
# employee = {}
# n = int(input("Enter the number of key value pairs : "))
# for i in range(n):
#     key = input("Enter the key : ")
#     value = input("Enter the value : ")
#     if(value.isdigit()):
#         employee.update({key:int(value)})
#     elif(value.isalpha()) or ' ' in value:
#         employee.update({key:value})
#     else:
#         employee.update({key:float(value)})
# print(employee)
# for i in employee.values():
#     print(type(i))






