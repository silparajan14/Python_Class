#zero division error :
#eg :
# a  = int(input("enter num : "))
# b  = int(input("enter num : "))
# c = a/b
# print(c)
#when we enter 0 as b, we get "ZeroDivisionError: division by zero"
#syntax :
# try :
#     #body of try block
#     # we do our operations here
# except:
#     #if there is any exception occurs in try block,
#                # the except block execute

# try :
#     a = int(input("enter num : "))
#     b = int(input("enter num : "))
#     c = a / b
#     print(c)
# except:
#     print("cannot divide by zero! please input another value")

#solve quadratic eqn using exception handling:
# try :
#     a = int(input("Enter a : "))
#     b = int(input("Enter b : "))
#     c = int(input("Enter c : "))
#     x = ((-b)+((b**2 - 4*a*c)**0.5))/ (2*a)
#     y = ((-b)-((b**2 - 4*a*c)**0.5))/ (2*a)
#     print("x = ",x)
#     print("y = ",y)
# except:
#     print("cannot divide by zero! please input another value")
#here "a" only cannot be zero as we are diving by "a" only

#value error:
# try :
#     a = int(input("Enter a : "))
#     b = int(input("Enter b : "))
#     c = a/b
#     print(c)
# except:
#     print("please input correct data type")
#if instead of entering int for "a" we enter str or float we get msg

#index error:
# li =["a","b","c"]
# try:
#     position = int(input("enter index position : "))
#     print(li[position])
# except:
#     print("index out of range.please enter valid value")

#file not found error:
import os
# try :
#     li = os.listdir(r"C:\code\luminar_class\BigData_Q")  #here last S of QS is removed to check
#     print(li)
# except:
#     print("directory not found")

#another method using "f"
# import os
# try :
#     a = input("enter directory name: ")
#     li = os.listdir(rf"C:\code\luminar_class\{a}") #using "f"
#     print(li)
# except:
#     print("directory not found")
# #f : formatted string literals

#exceptions with arguments :
# an exception can have arguments that gives additional information abt problem
# the content of exceptions that vary by the types of exceptions occur
# try :
#     a = int(input("Enter a : "))
#     b = int(input("Enter b : "))
#     c = a/b
#     print(c)
# except ZeroDivisionError as e :  #e is just a variable
#     print(e)
#     #this gives inbuilt msgs
#   OR
# try :
#     a = int(input("Enter a : "))
#     b = int(input("Enter b : "))
#     c = a/b
#     print(c)
# except ZeroDivisionError :
#     print("cannot divide by 0")
# #this is only for zero division error

#for more than 1
# try :
#     a = int(input("Enter a : "))
#     b = int(input("Enter b : "))
#     c = a/b
#     print(c)
# except ZeroDivisionError as e :  #e is just a variable
#     print(e)
# except ValueError as e:
#     print(e)

#finally keyword : it is a block that execute either with try block or with except block.
# try:
#     a = int(input("enter num : "))
#     print(a)
# except ValueError as e:
#     print(e)
# finally:
#     print("program completed")

# #raise keyword : it is a keyword that is used to raise the exceptions and stops the execution of program
# try:
#     age = int(input("enter age : "))
#     if age<18:
#         raise Exception
#     else:
#         print("success")
# except Exception:
#     print("age less than 18")

# try:
#     age = int(input("enter age : "))
#     if age <= 0 :
#         raise Exception
#     else:
#         print("success")
# except Exception:
#     print("please enter positive value")













