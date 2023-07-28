import pymysql

# no space between "localhost"
mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "" ,
    database = "employee"
)

mycursor = mydb.cursor()

#from user ask for number of enteries needed : (5needed)
num = int(input("enter the number of entry : "))
for i in range(num):
    emp_name = input("enter name : ")
    designation = input("enter designation : ")
    salary = int(input("enter salary : "))
    comp_name = input("enter comp_name : ")
    sql = "insert into emp_reg(emp_name,designation,salary,comp_name) values('%s','%s',%d,'%s')"%(emp_name,designation,salary,comp_name)
    mycursor.execute(sql)

mydb.commit()

print("data added successfully!")

