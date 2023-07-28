## to drop table and database :

# sql = "drop table table_name "
# sql = "drop database database_name "

# import pymysql
#
# #for connecting python and mysql :
# mydb = pymysql.connect(
#     host = "localhost",
#     user = "root",
#     password = ""
# )
# mycursor = mydb.cursor()

##create sample_database
#
# sql = "create database sample_database"
#
# mycursor.execute(sql)
#
# print("database created successfully")


import pymysql

# no space between "localhost"
mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "" ,
    database = "sample_database"
)

mycursor = mydb.cursor()

## table creation :
# sql = "create table sample_reg(id int auto_increment,name varchar(30),phone bigint(10),email varchar(50) ,primary key(id))"
#
# mycursor.execute(sql)
#
# mydb.commit()
# print("table created successfully!")

## drop sample_reg :

# sql = "drop table sample_reg "
# mycursor.execute(sql)
# mydb.commit()
# print("table dropped.....")

### drop sample_database :
# sql = "drop database sample_database "
# mycursor.execute(sql)
# mydb.commit()
# print("database dropped.....")





