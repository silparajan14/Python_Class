import pymysql

# no space between "localhost"
mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "" ,
    database = "employee"
)

mycursor = mydb.cursor()

# database alter :
# to add new column to an existing table :
# sql = "alter table table_name add new_column_name int(10){ie,datatype}  "

### column : phn_num is added to emp_reg :

# sql = "alter table emp_reg add phn_num bigint(10)"
# mycursor.execute(sql)
# mydb.commit()
# print("column added...")

### to add data to this new column use update, as column is already there only we need to update that column.

### to delete a column from a table :
# syntax :  sql = "alter table table_name drop column column_name "

# sql = "alter table emp_reg drop column phn_num "
# mycursor.execute(sql)
# mydb.commit()
# print("column dropped...")

# to rename a column :
# syntax : sql = "alter table table_name change column_name new_column_name data_type() "

# sql = "alter table emp_reg change comp_name company_num varchar(144)"
# mycursor.execute(sql)
# mydb.commit()
# print("column renamed...")




















