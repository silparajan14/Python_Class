import pymysql

# no space between "localhost"
mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "" ,
    database = "employee"
)

mycursor = mydb.cursor()

## delete using id :

# id = int(input("enter id to be deleted : "))
# sql = "delete from emp_reg where id = %d "%id
# mycursor.execute(sql)
# mydb.commit()
# print("data deleted successfully....")
# # here , I deleted id = 7

## delete using emp_name :

# name = input("enter name to be deleted : ")
# sql = "delete from emp_reg where emp_name = '%s' "%name
# mycursor.execute(sql)
# mydb.commit()
# print("data deleted successfully....")
# # here, I deleted "mani"

## delete using designation and emp_name :

# name = input("enter name to be deleted : ")
# designation = input("enter designation to be deleted : ")
# sql = "delete from emp_reg where emp_name = '%s' and designation = '%s' "%(name,designation)
# mycursor.execute(sql)
# mydb.commit()
# print("data deleted successfully....")
# # here, I deleted "vijaya" with designation : "devops"

## even if one data is not found above returns "data deleted successfully....", so use this :

# name_1 = input("enter name to be deleted : ")
# designation_1 = input("enter designation to be deleted : ")
# sql = "select emp_name,designation from emp_reg "
# mycursor.execute(sql)
# a = mycursor.fetchall()
# for i in a :
#     if name_1 == i[0] and designation_1 == i[1]:
#         sql_1 = "delete from emp_reg where emp_name = '%s' and designation = '%s' " %(name_1, designation_1)
#         mycursor.execute(sql_1)
#         mydb.commit()
#         print("success!")
#         break
# else:
#         print("data not found!")
### here, when one data is not matched then we get "data not found!"
### for loop il data kittilengi else work avum apo "data not found!" kittum,
#                  but for loop il data kityal pinne else work avanda so use "break"





