# lst = [lambda i=i : i for i in range(1,6)]   #1,2,3,4,5
# for i in lst:
#     print(i())

#reverse 1 to 100
# lst = [lambda i=i :i for i in range(100,0,-1)]
# for i in lst:
#     print(i(),end= " ")

#multiplication table generation
# num = int(input("Enter num : "))
# lst = [lambda i=i:i*num for i in range(1,11)]
# for i in lst:
#     print(i())
#or
# num = int(input("Enter num : "))
# lst = [lambda i=i:"%d * %d = %d"%(i,num,i*num)for i in range(1,11)]
# for i in lst:
#     print(i())

#print even and odd range(100,200)
# lst = [lambda i=i:"%d is odd"%i if(i%2!=0) else "%d is even"%i for i in range(100,200)]
# for i in lst:
#     print(i())
#or
# even = []
# odd = []
# li = [lambda i = i:i for i in range(100,200)]
# for i in li:
#     if i()%2==0 :
#         even.append(i())
#     else:
#         odd.append(i())
# print(even)
# print(odd)
#  WRONG
# even =[]
# odd = []
# lst = [lambda i=i:even.append(i) if(i%2!=0) else odd.append(i) for i in range(100,200)]
# for i in lst:
#     print(i())

#reverse of a string
# str = input("Enter str : ")
# lst = [lambda i=i:str[: : -1] for i in range(1) ]
# for i in lst:
#     print(i())
#miss
# str = input("Enter str : ")
# lst = [lambda i=i:i  for i in range(len(str)-1,-1,-1)]
# for i in lst:
#     print(str[i()],end=" ")














