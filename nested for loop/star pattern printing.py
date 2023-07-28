# *
# * *
# * * *

#write a program to print a right angled triangle using nested for loop
# row = int(input("Enter the row : "))
#                                  # i is used for rows
# for i in range(0,row):             #if row = 3 , then i = 0,1,2 still there are 3 count so its ok!
#     for j in range(0,i + 1):     #j is used for column , j = (0,1), (0,2), (0,3)
#         print('*', end = ' ')    #space between each * in same line
#     print()                      #for * to get in each line

#write a program to print square pattern using nested for loop
# row = int(input("Enter the row : "))
# for i in range(row):
#     for j in range(row):       #ie, o, 1,...(row-1),count=row itself
#         print('*',end = ' ')
#     print()

#print reverse right angle?
# * * *
# * *
# *
#
# row = int(input("Enter the row : "))
# for i in range(row):
#     for j in range(0,row-i):
#         print('*',end = ' ')
#     print()

#miss
# row = int(input("Enter the row : "))
# for i in range(row,0,-1):  #ie, range(start,end-1,decrement of 1)
#     for j in range(0,i):
#         print('*',end = ' ')
#     print()

#pyramid pattern:
#    *
#   * *
#  * * *
#        space decreasing,num of star increasing
#              i : row   (0,row)  0,1,2
#              j : space (0,2),(0,1),(0,0)   ie,(0 ,row-i-1)ie,
#                                            0 is constant and for 2nd #3-0-1 = 2, 3-1-1 = 1, 3-2-1 = 0
#              k : *     (0,1),(0,2),(0,3)   ie, (0,i + 1)
# row = int(input("Enter the row : "))
# for i in range(row):    #i = 0,1,2
#     for j in range(0,row-i-1):
#         print(" ", end = '')
#     for k in range(0,i + 1):
#         print("*",end = ' ')
#     print()

#print reverse pyramid using nested loop
# i     = 0,1,2              for  row
# j     = [0,0   0,1  0,2 ]  for space
# k     = [0,3   0,2  0,1 ]  for *
# row = int(input("Enter row : "))
# for i in range(row):
#     for j in range(0,i):
#         print(" ", end = '')
#     for k in range(0,row-i):
#         print('*',end = ' ')
#     print()






