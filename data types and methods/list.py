#list is a sequence data type
#it is a collection of elements
#mutable : means changeable
#any data type collection (any data type can be collected in a list)
#represented using [ ] brackets

# li = ['a','b',1,2,1.2,1.5]
# print(li)
#
# #len() :
# #print(len(li))
#
# #append() : insert to the end position of a list
# li.append('c')  #here update happens
# print(li)       #then we print the updated list
#
# #insert() : method used to add elements using index positions[any position as we need]
# #syntax : insert('position','element')
# li.insert(4,'f')
# print(li)
#
# #extend() : used to insert a list of elements to another list
# # li.extend(['e','g',5,6])
# # print(li)
# #  OR
# li1 = ['e','g',5,6]
# li.extend(li1)
# print(li)
#
# #pop() : to delete last position
# li.pop()   #last element gone
# print(li)
#
# #pop(index_position) :
# li.pop(2)   #2nd postion gone
# print(li)
#
# #remove() : remove by specific element
# li.remove('a')   #(if there is more than 1 "a" then only the first "a" will be gone, not all "a")
# print(li)
#
# #count() : to count any specific element in the list
# #print(li.count('b'))
#
# #reverse() : to completely reverse the list
# li.reverse()
# print(li)
#
# #sort() : to arrange [only for same data types]
# alpha = ['b','c','a','e','d']
# alpha.sort()
# print(alpha)
# alpha.sort(reverse = True)
# print(alpha)
#
# num = [1,-1,2,6,67,1,78,0]
# num.sort()
# print(num)
# num.sort(reverse = True)
# print(num)
#
#
# names = ['amal','akhil','arjun']
# names.sort()
# print(names)
# names.sort(reverse = True)
# print(names)
#
# #according to ascii
# # A TO Z : 65 TO 90   ie, A = 65, B = 66 ... Z = 90
# # a to z : 97 - 122   ie, a = 97, b = 98 ... z = 122
# name = ['Amal','akhil','Arjun']
# name.sort()
# print(name)
# name.sort(reverse = True)
# print(name)
#
# #min() and max() :
# print(min(alpha))
# print(max(alpha))
#
# print(min(num))
# print(max(num))
#
# print(min(names))
# print(max(names))
#
# print(min(name))
# print(max(name))
#
# #clear() : to remove elements from list, not the list
# li.clear()
# print(li)

#list creation
#making a list from user's end
# li = []
# n = int(input("Enter the number of elements : "))
# for i in range(n):
#     element = input("Enter the element %d : "%(i+1))
#     li.append(element)
# print(li)

#create 3 empty list : name,age,email.
# (enter the number of employees)
# name = []
# age = []
# email = []
# n = int(input("Enter the number of employees : "))
# for i in range(n):
#     name_1 = input("Enter the name %d : "%(i+1))
#     name.append(name_1)
#     age_1 = input("Enter the age %d : "%(i+1))
#     age.append(age_1)
#     email_1 = input("Enter the email %d : "%(i+1))
#     email.append(email_1)
# print("Name : ",name)
# print("Age : ",age)
# print("Email : ",email)

#to get the type of elements from list
# li = []
# n = int(input("Enter the number of elements : "))
# for i in range(n):
#     element = input("Enter the element %d : "%(i+1))
#     li.append(element)
# print(li)
#
# for i in li:
#     print(type(i))

#work : to insert different types of data to same list!
# li = []
# n = int(input("Enter the number of elements : "))
# for i in range(n):
#     element = input("Enter element : ")
#     if(element.isdigit()):
#         li.append(int(element))
#     else:
#         li.append(element)
# print(li)

#including floats
# li = []
# n = int(input("Enter the number of elements : "))
# for i in range(n):
#     element = input("Enter element : ")
#     if(element.isdigit()):
#         li.append(int(element))
#     elif element.isalpha():
#         li.append(element)
#     else:
#         li.append(float(element))
# print(li)
# for i in li:
#     print(type(i))

#list slicing :
#create a list , use 4 slicing method
# list = ["a","b",1,2,3,4]
# print(list[0:5])
# print(list[2:])
# print(list[:4])
# print(list[:])
# print(list[::-1])

