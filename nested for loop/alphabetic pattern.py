#ascii stands for american std code for information interchange
# A TO Z : 65 TO 90   ie, A = 65, B = 66 ... Z = 90
# a to z : 97 - 122   ie, a = 97, b = 98 ... z = 122

#pattern
#A           65
#B B         66 66
#C C C       67 67 67

#miss
# row = int(input("Enter number of rows : "))
# for i in range(65,65+row):
#     for j in range(65,i+1):
#         print(chr(i), end = " ")
#     print()

#mine
# row = int(input("Enter number of rows : "))
# num = 65
# for i in range(65,65+row):
#     for j in range(65,i+1):
#         print(chr(i), end = " ")
#         num += 1
#     print()

#for small letters
# a
# b b
# c c c

#miss
# row = int(input("Enter number of rows : "))
# for i in range(97,97+row):
#     for j in range(97,i+1):
#         print(chr(i), end = " ")
#     print()

#mine
# row = int(input("Enter number of rows : "))
# num = 97
# for i in range(97,97+row):
#     for j in range(97,i+1):
#         print(chr(i), end = " ")
#         num += 1
#     print()

#work 1
# a a a a a
# b b b b
# c c c
# d d
# e
#starting range ittu kodukumbo not wroking?but correct anu

# row = int(input("Enter number of rows : "))
# num = 97
# for i in range(row):
#     for j in range(row-i):
#         print(chr(num), end = " ")
#     num += 1
#     print()

#other
# n = int(input("Enter rows : "))
# for i in range(97,97+n):
#     for j in range(97,97+n):
#         print(chr(i),end =" ")
#     n-=1
#     print()

#work 2
# A
# A B
# A B C
# A B C D
# A B C D E
# n = int(input("Enter the number of rows : "))
# num = 65
# for i in range(65,65+n):
#     for j in range(65,i+1):
#         print(chr(j),end=" ")
#         num += 1
#     print()

#work 3
# a
# b c
# d e f
# row = int(input("Enter the number of rows : "))
# num = 97
# for i in range(row):
#     for j in range(i+1):
#         print(chr(num),end = " ")
#         num += 1
#     print()

#    OR

# row = int(input("Enter the number of rows : "))
# num = 97
# for i in range(97,97+row):
#     for j in range(97,i+1):
#         print(chr(num),end = " ")
#         num += 1
#     print()

#rough
# a b c d e
# f g h i
# j k l
# m n
# o
# row = int(input("Enter number of rows : "))
# num = 97
# for i in range(row):
#     for j in range(row-i):
#         print(chr(num), end = " ")
#         num += 1
#     print()

#rough(to compare two methods)
# A
# B B
# C C C
# D D D D
# E E E E E
#1)
# row = int(input("Enter the number of rows : "))
# num = 65
# for i in range(65,65+row):
#     for j in range(65,i+1):
#         print(chr(i),end=" ")
#         num += 1
#     print()
#2)miss
# row = int(input("Enter number of rows : "))
# for i in range(65,65+row):
#     for j in range(65,i+1):
#         print(chr(i), end = " ")
#     print()

