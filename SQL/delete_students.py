import pymysql

# no space between "localhost"
mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "" ,
    database = "student"
)

mycursor = mydb.cursor()

## delete using id :

# id = int(input("enter id to be deleted : "))
# sql = "delete from student_reg where id = %d "%id
# mycursor.execute(sql)
# mydb.commit()
# print("data deleted successfully....")
## here , I deleted id = 1

## delete using name :

# name = input("enter name to be deleted : ")
# sql = "delete from student_reg where name = '%s' "%name
# mycursor.execute(sql)
# mydb.commit()
# print("data deleted successfully....")
## here, I deleted "abhi"

## delete using email and name :

# name = input("enter name to be deleted : ")
# email = input("enter email to be deleted : ")
# sql = "delete from student_reg where name = '%s' and email = '%s' "%(name,email)
# mycursor.execute(sql)
# mydb.commit()
# print("data deleted successfully....")
# # here, I deleted "amy" with email : "amy@123"

## even if one data is not found above returns "data deleted successfully....", so use this :

# name_1 = input("enter name to be deleted : ")
# email_1 = input("enter email to be deleted : ")
# sql = "select name,email from student_reg "
# mycursor.execute(sql)
# a = mycursor.fetchall()
# for i in a :
#     if name_1 == i[0] and email_1 == i[1]:
#         sql_1 = "delete from student_reg where name = '%s' and email = '%s' " %(name_1, email_1)
#         mycursor.execute(sql_1)
#         mydb.commit()
#         print("success!")
#         break
# else:
#         print("data not found!")
### here, when one data is not matched then we get "data not found!"
### for loop il data kittilengi else work avum apo "data not found!" kittum,
#                  but for loop il data kityal pinne else work avanda so use "break"


# # "else" used under "if" :
# for i in range(1,10):
#     print(i)
# else:
#     print("finish!")

























