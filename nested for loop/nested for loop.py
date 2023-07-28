# for i in range(1,5):       #i = 1,2,3,4
#     for j in range(1,10):  #j = 1,2,....9
#         print(i,j)

#Generate multiplication table of 1 to 10 using nested for loop?
# for i in range(1,11):
#     for j in range(1,11):
#         print("%d * %d = %d"%(i,j,i*j))

#another method # to get a space between each table
# for i in range(1,11):
#     for j in range(1,11):
#         print("%d * %d = %d"%(i,j,i*j))
#     print()    #we need space only after each table ie,after each loop of i with every value of j

#another method # using tab
# for i in range(1,11):
#     for j in range(1,11):
#         print("%d * %d = %d"%(i,j,i*j), end = '\t\t')
#     print()
#only "\t" gives out in single line with space in between,so also use "print()" option.
#note the difference in first elements of last 2 egs, "\t" gives out in single line
#and along with "print()" option 2nd loop of i appears in nxt line
