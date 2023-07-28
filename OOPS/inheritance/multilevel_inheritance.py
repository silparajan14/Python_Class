#A---> B ----> C
#syntax :
# class A:
#     def a1(self):
#         print("a1")
# class B(A):
#     def b1(self):
#         print("b1")
# class C(B):
#     def c1(self):
#         print("c1")
# obj = C()
# obj.a1()
# obj.b1()
# obj.c1()

#mobile = storage, color
#samsung = name
#galaxy = year of implimentation or launch , speed
# class mobile:
#     def mobile1(self,storage,color):
#         self.storage = storage
#         self.color = color
#         print("storage = ",self.storage)
#         print("color = ",color)
# class samsung(mobile):
#     def samsung1(self,name):
#         self.name = name
#         print("name = ",self.name)
# class galaxy(samsung):
#     def galaxy1(self,launch,speed):
#         self.launch = launch
#         self.speed = speed
#         print("launch = ",self.launch)
#         print("speed = ",self.speed)
# obj = galaxy()
# obj.mobile1(168,"black")
# obj.samsung1("Galaxy S23")
# obj.galaxy1("feb 01,23","8gb ram")

#multilevel inheritance using constructors :
#syntax :
# class mobile:
#     def __init__(self,storage,color):
#         self.storage = storage
#         self.color = color
#         print("storage = ",self.storage)
#         print("color = ",color)
# class samsung(mobile):
#     def __init__(self,storage,color,name):
#         super().__init__(storage,color)
#         self.name = name
#         print("name = ",self.name)
# class galaxy(samsung):
#     def __init__(self,storage,color,name,launch,speed):
#         samsung.__init__(self,storage,color,name)
#         self.launch = launch
#         self.speed = speed
#         print("launch = ",self.launch)
#         print("speed = ",self.speed)
# obj = galaxy("168gb","black","Galaxy S23","feb 01,23","8gb ram")

#car , maruthi, maruthi 800
# class car:
#     def __init__(self,name,color):
#         self.name = name
#         self.color = color
#         print("name = ",self.name)
#         print("color = ",color)
# class maruthi(car):
#     def __init__(self,name,color,fuel):
#         super().__init__(name,color)              #car.__init__(name,color) same
#         self.fuel = fuel
#         print("fuel = ",self.fuel)
# class maruthi_800(maruthi):
#     def __init__(self,name,color,fuel,mileage,engine):
#         maruthi.__init__(self,name,color,fuel)
#         self.mileage = mileage
#         self.engine = engine
#         print("mileage = ",self.mileage)
#         print("engine =  ",self.engine)
# obj = maruthi_800("maruthi","red","petrol","15 kmpl","796cc")












