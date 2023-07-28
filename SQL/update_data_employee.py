import pymysql

# no space between "localhost"
mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "" ,
    database = "employee"
)

mycursor = mydb.cursor()

## single data updation :

# id = int(input("enter id to be updated : "))
# name = input("enter name : ")
# sql = "update emp_reg set emp_name = '%s' where id = %d "%(name,id)
# mycursor.execute(sql)
# mydb.commit()
# print("database updated....")
# ## here, I have updated "silpa",id = 1 with "silparajan"

## multiple data updation :

#designation, comp_name :
# sql = "update emp_reg set designation = '%s' , comp_name = '%s' where id = %d"%("data_scientist",'infosys',1)
# mycursor.execute(sql)
# mydb.commit()
# print("database updated....")
# #here, I have changed "fresher" to "data_scientist" and "comp_name" to "infosys"

## update using emp_name :

# sql = "update emp_reg set designation = '%s' where emp_name = '%s' "%('data_analyst','vishnu')
# mycursor.execute(sql)
# mydb.commit()
# print("database updated....")
# # #here, I have changed "fresher" to "data_analyst" using name : "vishnu"

##using designation and emp_name together :

# sql = "update emp_reg set salary = %d where designation = '%s' and emp_name = '%s'"%(1500000,'data_analyst','vishnu')
# mycursor.execute(sql)
# mydb.commit()
# print("database updated....")
# # #here, I have changed salary of vishnu using name and designation

## using OR :

# sql = "update emp_reg set designation = '%s' where salary = %d  or emp_name = '%s'"%('senior',750,'rajan')
# mycursor.execute(sql)
# mydb.commit()
# print("database updated....")
# # here, I changed designation of rajan to senior using salary(which is not 750) OR emp_name

