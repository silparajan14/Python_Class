# 1
# 2 2
# 3 3 3

# n = int(input("Enter the num of rows : "))
# num = 1
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(num,end = " ")
#     num += 1
#     print()      #new line

#reverse of the above
#1 1 1
#2 2
#3

# n = int(input("Enter the num of rows : "))
# num = 1
# for i in range(0,n):
#     for j in range(0,n-i):
#         print(num,end= " ")
#     num += 1
#     print()

#miss
# n = int(input("Enter the num of rows : "))
# num = 1
# for i in range(n,0,-1):
#     for j in range(0,i):
#         print(num,end= " ")
#     num += 1
#     print()

#3 3 3
#2 2
#1
# n = int(input("Enter the num of rows : "))
# num = n
# for i in range(n):
#     for j in range(0,n-i):
#         print(num,end= " ")
#     num -= 1
#     print()

#miss
# row = int(input("Enter the num of rows : "))
# num = row
# for i in range(row,0,-1):
#     for j in range(0,i):
#         print(num,end= " ")
#     num -= 1
#     print()

#1
#2 3
#4 5 6

# row = int(input("Enter your num : "))
# num = 1
# for i in range(0,row):
#     for j in range(0,i+1):
#         print(num,end=" ")
#         num += 1
#     print()

#multiplication of any number given by user
# 5
# 10 10
# 15 15 15
# num = int(input("Enter a number : "))
# row = int(input("Enter the num of rows : "))
# n = 1
# for i in range(row):
#     for j in range(0,i+1):
#         print(num*n,end = " ")
#     n += 1
#     print()

#miss(easy)
# num = int(input("Enter a number : "))
# row = int(input("Enter the num of rows : "))
# for i in range(row):
#     for j in range(0,i+1):
#         print(num*(i+1),end = " ")
#     print()

#print pyramid and reverse pyramid
#1)
#       1
#     2   2
#   3   3   3

#2)
# 1   1   1
#   2   2
#     3

#1)
# row = int(input("Enter the row : "))
# num = 1
# for i in range(row):
#     for j in range(0,row-i-1):
#         print(" ", end = '')
#     for k in range(0,i + 1):
#         print(num,end = ' ')
#     num += 1
#     print()
#2)
# row = int(input("Enter row : "))
# num = 1
# for i in range(row):
#     for j in range(0,i):
#         print(" ", end = '')
#     for k in range(0,row-i):
#         print(num,end = ' ')
#     num += 1
#     print()

#3)
# 4 4 4 4
#  3 3 3
#   2 2
#    1
# row = int(input("Enter row : "))
# num = row
# for i in range(row):
#     for j in range(0,i):
#         print(" ", end = '')
#     for k in range(0,row-i):
#         print(num,end = ' ')
#     num -= 1
#     print()

#4)
# 1 2 3
#  4 5
#   6
# row = int(input("Enter row : "))
# num = 1
# for i in range(row):
#     for j in range(0,i):
#         print(" ", end = '')
#     for k in range(0,row-i):
#         print(num,end = ' ')
#         num += 1
#     print()

#5)
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end= " ")
#     print()

#6)
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()

#7)
# 0 1 2 3 4 5
# 0 1 2 3 4
# 0 1 2 3
# 0 1 2
# 0 1
# for i in range(5,0,-1):
#     for j in range(0,i+1):
#         print(j,end = " ")
#     print()

#8)
# 0
# 0 1
# 0 2 4
# 0 3 6 9
# 0 4 8 12 16
# 0 5 10 15 20 25
# for i in range(0,6):
#     for j in range(0,i+1):
#         print(i*j,end = " ")
#     print()










