import pymysql

# no space between "localhost"
mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "" ,
    database = "student"
)

mycursor = mydb.cursor()

#from user ask for number of enteries needed :
num = int(input("enter the number of entry : "))
for i in range(num):
    name = input("enter name : ")
    phn_num = int(input("enter num : "))
    email = input("enter email : ")
    sql = "insert into student_reg(name,phone,email) values('%s',%d,'%s')" % (name, phn_num, email)
    mycursor.execute(sql)

mydb.commit()

print("data added successfully!")







