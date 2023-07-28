#user defined exception : in python users can define custom exceptions by creating a new class.
#this exception class has to be derived , either directly or indirectly
#from the built-in exception class. most of the built-in exceptions are also derived from this class

#exception :already build-in class
#define python user-defined exceptions:
# class Error(Exception):  #main exception parent class
#     pass
# class ZeroError(Error): #child class
#     pass
# try:
#     num = int(input("enter num : "))
#     if num==0:
#         raise ZeroError
# except ZeroError:
#     print("input value is zero,try again!")

# #work:
# input :abc = succes
#  : 123 = numbererror :please input a string not numbers
#  : abc123 = alphanumericerror : please input a string not alphanumberic
# :.@ = specialcharactererror : please input a valid string not character
# # class Error(Exception):
# #     pass  ?
# class NumberError(Exception):
#     pass
# class AlphaNumericError(Exception):
#     pass
# class SpecialCharError(Exception):
#     pass
# try:
#     str = input("enter string : ")
#     if str.isalpha() :
#         print("success")
#     elif str.isdigit():
#         raise NumberError
#     elif str.isalnum():
#         raise AlphaNumericError
#     else:
#         for i in str:
#             if i in ['@','*','.','#']:
#                 raise SpecialCharError
# except NumberError:
#     print("please input a string not numbers")
# except AlphaNumericError:
#     print("please input a string not alphanumberic")
# except SpecialCharError:
#     print("please input a valid string not character")









