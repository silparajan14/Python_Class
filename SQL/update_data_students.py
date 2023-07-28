import pymysql

# no space between "localhost"
mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "" ,
    database = "student"
)

mycursor = mydb.cursor()

## single data updation :

# id = int(input("enter id to be updated : "))
# name = input("enter name : ")
# sql = "update student_reg set name = '%s' where id = %d "%(name,id)
# mycursor.execute(sql)
# mydb.commit()
# print("database updated....")
# # here, I have updated "silpa",id = 5 with "ilu"

## multiple data updation :

# #email, phone :
# sql = "update student_reg set email = '%s' , phone = %d where id = %d"%("abi@123",9678956780,3)
# mycursor.execute(sql)
# mydb.commit()
# print("database updated....")
# #here, I have changed "abhi@123" to "abi@123" and phn : 1234 to 9678956780

## update using name :

# sql = "update student_reg set email = '%s' where name = '%s' "%('silparnair@123','silpa')
# mycursor.execute(sql)
# mydb.commit()
# print("database updated....")
# # #here, I have changed "silpa@123" to "silparnair@123" using name

##using email and name together :

# sql = "update student_reg set phone = %d where email = '%s' and name = '%s'"%(9879644360,'siva@123','siva')
# mycursor.execute(sql)
# mydb.commit()
# print("database updated....")
# # #here, I have changed phone of "siva" using email and name together

## using OR :

# sql = "update student_reg set email = '%s' where phone = %d  or name = '%s'"%('siva1@123',723458,'siva')
# mycursor.execute(sql)
# mydb.commit()
# print("database updated....")
## here, i changed email of siva using OR












