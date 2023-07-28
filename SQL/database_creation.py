# pip install pymysql : console > terminal >command prompt(from upper down arrow) type "pip install pymysql"
# or settings > interpreter > + >pymysql
#
import pymysql

#for connecting python and mysql :
mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = ""
)

# #create cursor object :
mycursor = mydb.cursor()
# #cursor object which is used to select,retreive data from a set of rows. also used to execute an sql command.

#create database databasename :"student" = databasename
# sql = "create database student"
#
# mycursor.execute(sql)
#
# print("database created successfully")

# work :
#create "employee " database
# sql = "create database employee"
#
# mycursor.execute(sql)
#
# print("database created successfully")






























