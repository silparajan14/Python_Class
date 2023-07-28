# num = int(input("Enter your num : "))
# if (num > 0) :
#     print("Positive number!")
# elif(num == 0):
#     print("Zero!")
# else:
#     print("Negative number!")
#
#write a program to find largest of 3 numbers
# a = int(input("Enter num1 : "))
# b = int(input("Enter num2 : "))
# c = int(input("Enter num3 : "))
# if(a > b and a>c):
#     print("%d is the greatest!"%a)
# elif(b>c):
#     print("%d is the greatest!"%b)
# else:
#     print("%d is the greatest!"%c)

#Q)num divisible by 2 and 3 both
# num = int(input("Enter number : "))
# if(num % 2 == 0 and num % 3 == 0 ):
#     print("It is divisible by both 2 and 3 ")
# else:
#     print("It is not divisible!")

#Q)Accept the age of 4 people and display the youngest one
# age_1 = int(input("Enter age1 : "))
# age_2 = int(input("Enter age2 : "))
# age_3 = int(input("Enter age3 : "))
# age_4 = int(input("Enter age4 : "))
# if(age_1 < age_2 and age_1 < age_3 and age_1 < age_4):
#     print("age_1")
# elif(age_2 < age_3 and age_2 < age_4):
#     print("age_2")
# elif(age_3 < age_4):
#     print("age_3")
# else:
#     print("age_4")

#Q)Accept the percentage from the user and display the grade according to the following criteria:
# mark = int(input("Enter mark : "))
# if(mark >= 81 and mark <=100):
#     print("A+")
# elif(mark >= 71 and mark <=80):
#     print("A")
# elif(mark >= 61 and mark <=70):
#     print("B+")
# elif(mark >= 51 and mark <=60):
#     print("B")
# elif(mark >= 41 and mark <=50):
#     print("C")
# elif(mark >= 31 and mark <=40):
#     print("D")
# else:
#     print("Fail!")

#Q)write a program to display "HAI" if a number entered by the user is the multiple of 7 , else it should print "SORRY"
# num = int(input("Enter number : "))
# if(num % 7 == 0):
#     print("HAI")
# else:
#     print("SORRY")

#Q)write a program to check the last digit of a number is divisible by 3
#to find last digit of any number (number%10)
# a = 123
# print(a%10)

# num = int(input("Enter your number : "))
# a = num%10
# if(a%3 ==0 ):
#     print("Divisible by 3")
# else:
#     print("Sorry")

#Q)write a program to accept the CP of a bike and display the road tax to be paid according to the following criteria
#cp [ >100000 , 100000<=cp<=50000 , <=50000 ]
#tax [ 15% ,    10% ,    5% ]
# price = int(input("Enter your Price of bike : "))
# if(price > 100000):
#     tax = (15/100)*price
#     print(tax)
# elif(price > 50000 and price <= 100000):
#     tax = (10/100)*price
#     print(tax)
# else:
#     tax = (5/100)*price
#     print(tax)

#Q)A company decided to give bonus to employees according to following criteria
# time = int(input("Enter your period of service : "))
# salary = int(input("Enter your salary : "))
# if (time >10):
#     bonus = (10/100)*salary
#     print(bonus)
# elif(time >= 6 and time <= 10):
#     bonus = (8/ 100) * salary
#     print(bonus)
# else:
#     bonus = (5/100)*salary
#     print(bonus)

