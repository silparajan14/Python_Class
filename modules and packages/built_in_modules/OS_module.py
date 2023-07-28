#used to interact with the operating system
#os = operating system

#getcwd() : method used to get current working directory

import os

# cwd = os.getcwd()
# print(cwd)

#mkdir : method used to create directory named path with specified numeric mode(no need of assigning variable)
# os.mkdir(r"C:\code\luminar_class\newdirectory")  # r --> raw string ---> used to remove spcl characters from the path
# print("directory created successfully")

# right click on luminar_class > copy path reference > absolute path

#listdir : to get a list of all files and directories in a specific directory
# lst = os.listdir(r"C:\code\luminar_class")
# print(lst)

#rmdir : to remove empty directories
# os.rmdir(r"C:\code\luminar_class\newdirectory")  #empty directory we created earlier is deleted
# print("directory deleted successfully")

#remove() : to remove or delete a file path
# os.remove(r"C:\code\luminar_class\main.py")
# print("file removed successfully....!")

#to get system name :
#print(os.name)
#windows NT is a microsoft windows personal computer operating system
# N T : new technology




