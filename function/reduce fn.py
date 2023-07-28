#reduce fn : a reduce fn in python takes a seq as an argument and a new reduced result is returned
#reduce fn belongs to fn tool module
#modules : collection of fns # it is a python file with .py extension

#how to import reduce fn ?
#from functools import reduce

#find the largest elements from the list using reduce fn?
from functools import reduce

# li = [100,200,300,400]
# max = reduce(lambda a,b:a if a>b else b,li)
# print(max)

#find the smallest element from the given list
# li = [2,1,3,5,7]
# min = reduce(lambda a,b:a if a<b else b,li)
# print(min)

#find the sum of numbers from list
# li = [1,2,3,4,5,6]
# sum = reduce(lambda a,b:a+b ,li)
# print("sum = ",sum)

#product of numbers from list
# li = [5,7,9,11,13]
# product = reduce(lambda a,b:a*b,li)
# print("product = ",product)




