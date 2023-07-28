#Abstraction :
# in python it is defined as a process of handling complexity by hiding unnecessary information from the user.
# this is one of the core concept of object-oriented programming(OOPs)

#what is ABC in Abstraction?
#   this module provides the infrastructure for defining abstract base classes.
#ABC : python has a module called abc (abstract base class) that
#           offers the necessary tools for crafting an abstract base class.

#python decorators : decorators can be extremely useful as they allow
#                    the extension of an existing fn,without any modification to the original fn source code

# we use '@' before any decorator ,ie, @decorator_name

#we are using below decorator :
#@abstractmethod : a decorator indicating abstract methods

#import ABC
from abc import ABC,abstractmethod

# class vechicle(ABC):   #to change class into abstract class we need to (ABC)
#     @abstractmethod
#     def wheel(self):   #abstract method don't have body, instead use 'pass' keyword
#         pass
# class car(vechicle):
#     def door(self):
#         print("4 doors")
#     def wheel(self):
#         print("4 wheels")
# obj = car()
# obj.door()
# obj.wheel()

#interview qs :
#pass keyword :used to define an empty class or empty fn
# qs : create an empty fn?
# def abc():
#     pass
# abc()
# qs : create an empty class?
# class class_name:
#     pass

#create an abstract class car
#wheel , door, mileage : common things
#gear , automatic
#honda city, polo :objects
# class car(ABC):    #we cannot create obj and body.it is always hidden
#     @abstractmethod
#     def wheel(self):
#         pass
#     @abstractmethod
#     def door(self):
#         pass
#     @abstractmethod
#     def mileage(self):
#         pass
# class honda_city(car):
#     def wheel(self):
#         print("4 wheels")
#     def door(self):
#         print("4 doors")
#     def mileage(self):
#         print("12 ")
#     def gear(self):
#         print("geared")
# class polo(car):
#     def wheel(self):
#         print("4 wheels")
#     def door(self):
#         print("4 doors")
#     def mileage(self):
#         print("20 ")
#     def auto(self):
#         print("automatic")
# obj = honda_city()
# obj.door()
# obj.wheel()
# obj.mileage()
# obj.gear()
#
# obj1 = polo()
# obj1.door()
# obj1.wheel()
# obj1.mileage()
# obj1.auto()















