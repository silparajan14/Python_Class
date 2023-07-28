#set
#unordered collection of data types
#is iterable and has no duplicate values
#represent by { }
#unordered : there is no order for item in a set
#set cannot have 2 elements with same name , ie duplicate not allowed
#unindexed
#mutable

# s = {"a","b","c"}
# print(s)

#length of the set :
# print(len(s))

#without len funtion :
# count = 0
# for i in s:
#     count += 1
# print(count)

#add() : to add one item (not existing elements)
# s.add("d")
# print(s)

#update() : used to add items from another set
# s1 = {"h","i","j","k"}
# s.update(s1)
# print(s)

#updating using a list : (we cannot add set into a list)
# s3= [1,2,3,4]
# s.update(s3)
# print(s)

#update using tuple : (we cannot add set into a tuple)
# s4 = (10,11,12)
# s.update(s4)
# print(s)

#remove() :
# s.remove("a")
# print(s)

#discard() : remove something
# s.discard("b")
# print(s)

#pop() : ethengilum oru element povum (since no position)
# s.pop()
# print(s)

#intersection_update method() : used to keep only items that are present in both sets
# x = {"a","b","c"}
# y = {"c","d","e"}
# x.intersection_update(y)
# print(x)

#symmetric_difference_update() : method will keep only the element that are not present in both sets
# x1 = {"a","b","c"}
# x2 = {"a","d","f"}
# x1.symmetric_difference_update(x2)
# print(x1)

#frozenset() : it is an inbuild function in python which takes an iterable object as input and makes the immutable
#simply it freeze iterable object and makes them unchangable
# li = [1,2,'a','b']
# x = frozenset(li)

#to change a set to a list{ here, list() is called a constructor }
# set = {1,2,'a','b'}
# a = list(set)
# print(a)

#set() : to convert a list or a tuple to a set
#it doesnt print duplicates

#li = ['b',"a",'c','b','a','d']
#remove duplicate elements from list "li" and sort it
# a = set(li)
# print(a)
# b = list(a)
# b.sort()
# print(b)














