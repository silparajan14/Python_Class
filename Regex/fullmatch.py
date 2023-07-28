import re

# #fullmatch() : match = True, else = False
#
# name = input("enter the name : ")
# rule = "[A-Za-z\s]+"               #\s : for space as name will contain space between first and second name
# match = re.fullmatch(rule,name)
# if match :
#     print("valid name")
# else:
#     print("not valid")

#name with limit 10 :
# name = input("enter the name : ")
# rule = "[A-Za-z]{10}+"
# match = re.fullmatch(rule,name)
# if match :
#     print("valid name")
# else:
#     print("not valid")

#name : min=3, max=8
# name = input("enter the name : ")
# rule = "[A-Za-z]{3,8}+"
# match = re.fullmatch(rule,name)
# if match :
#     print("valid name")
# else:
#     print("not valid")

#rule : name should start with upper case,others lower only,space included.total limit = 10
# name = input("enter the name : ")
# rule = "^[A-Z][a-z\s]{9}"           #{9} belongs to [a-z\s] only. already one letter will be taken from ^[A-Z]
# match = re.fullmatch(rule,name)
# if match :
#     print("valid name")
# else:
#     print("not valid")

#name shld only start with A,B,or C. followed by lower case. numbers can or cannot be included.
# name = input("enter the name : ")
# rule = "^[ABC][a-z]+[0-9]*"  #* any times
# match = re.fullmatch(rule,name)
# if match :
#     print("valid name")
# else:
#     print("not valid")

#name shld only start with A,B,or C. followed by lower case. numbers can or cannot be included.if comes only apper 2 times
# name = input("enter the name : ")
# rule = "^[A-C][a-z]+([0-9]{1,2}|[^0-9])"  #[^0-9] = except, note:donot put extra spaces in between "|"
# match = re.fullmatch(rule,name)
# if match :
#     print("valid name")
# else:
#     print("not valid")

#(condition 1 | condition 2) can be given in this format.

#phn number validation(donot put int(input) as regex deals with only strings)
# name = input("enter the phn_num : ")
# rule = "[0-9]{10}+"
# match = re.fullmatch(rule,name)
# if match :
#     print("valid name")
# else:
#     print("not valid")

#should start with +, first 2 num shld start with "91", range : 10 without +91, first digit starts with "9876"
# name = input("enter the phn_num : ")
# rule = "^[+][9][1][6-9][0-9]{9}"
# match = re.fullmatch(rule,name)
# if match :
#     print("valid name")
# else:
#     print("not valid")

#email validation :
#abc@gmail.com
#abc123@gmail.com
#abc_123@gmail.com (numbers at first not valid,eg:123abc@gmail.com not valid)
# gmail = input("enter the gmail : ")
# rule = "^[a-z]+[_]?[0-9]*[@][g][m][a][i][l][.][c][o][m]"
# match = re.fullmatch(rule,gmail)
# if match :
#     print("valid name")
# else:
#     print("not valid")

# #username : input, dob : ,email :,password :    wrong?
# username = input("enter username : ")
# rule1 = "[a-z0-9]+"
# match1 = re.fullmatch(rule1,username)
#
# dob = input("enter dob : ")
# rule2 = "(^[0]?[1-9]|[1-3][1-9])[/]([0][1-9]|[1][0-2])[/][1-9][0-9]{3}"
# match2 = re.fullmatch(rule2,dob)
#
# email = input("enter email id : ")
# rule3 = "^[a-z]+[_]?[0-9]*[@][g][m][a][i][l][.][c][o][m]"
# match3 = re.fullmatch(rule3,email)
#
# password = input("enter password : ")
# rule4 = "[a-zA-Z0-9]{8,15}"
# match4 = re.fullmatch(rule4,password)
#
# if match1 and match2 and match3 and match4 :
#     print('\n'"Reg success"'\n')
#     print("login page\n")
#     print("username : ",username)
#     print("password : ",password)
#     print("login success")
# else:
#     print("Reg failed")

# #enter like this :
# enter username : silpa123
# enter dob : 14/02/1997
# enter email id : silpa123@gmail.com
# enter password : silpa1234
#
# Reg success
#
# login page
#
# username :  silpa123
# password :  silpa1234
# login success

# findall :
import re
# to search patterns :
# str = "this is my paragraph"
# pattern = "[A-Za-z]+"
# x = re.findall(pattern,str)
# print(x)

# to search words :
# str = "this is my paragraph"
# word = input("enter the word to search : ")
# x = re.findall(word,str)
# print(x)

#condition :str as input, pattern without number, if not "word not found"
# str = input("enter your string : ")
# pattern = "[A-Za-z]+"
# x = re.findall(pattern,str)
# if len(x) != 0:
#     print(x)
# else:
#     print("word not found!")

# str = "my first number is 12345 and my second number is 2345"
# pattern = '\D+'   #numbers kalayum
# x =re.findall(pattern,str)
# print(x)
#
# str = "my first number is 12345 and my second number is 2345"
# pattern = '\d+'   #alphabets kalayan
# x =re.findall(pattern,str)
# print(x)

# str = "my first number is 12345 and my second number is 2345"
# pattern = '\s+'   #space kittan
# x =re.findall(pattern,str)
# print(x)

# str = "my first number is 12345 and my second number is 2345"
# pattern = '\w+'  #ella words including numbers um kittan
# x =re.findall(pattern,str)
# print(x)

#search method(): it returns the span(position) and the object.
# str = "hello welcome"
# word = input("enter word : ")
# x = re.search(word,str)
# print(x)

#split() :
# text = "the_rain_in_spain"
# x = re.split("_",text)
# print(x)

# text = "the rain in spain"
# x = re.split("\s",text)     #for space use "\s"
# print(x)

# text = "arun and arjun are students"                       #check difference in each case!
# a = re.split('\s',text,1)  #only 1 splitting occures
# print(a)
# b = re.split('\s',text,2)
# print(b)
# c = re.split('\s',text,3)
# print(c)
# d = re.split('\s',text,4)
# print(d)

#sub() : substitution
# a = "hello welcome to python"
# x = re.sub("\s","#",a)         #working : search for spaces(\s), replace it with "#", in string "a"
# print(x)

# a = "hello welcome to python"
# x = re.sub("\s","#",a,1)   #only replace first space only
# print(x)

# b = "hello welcome to python"
# x = re.sub("\s","#",b,2)   #only replace first and second space with "#" only
# print(x)











































