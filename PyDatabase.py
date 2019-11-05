import mysql.connector

#***************************************************************
#The execute function is a key method in this object.
#Some examples of SQL methods that can be called are:
#"Create Database <DatabaseName>" -Creates new database
#"Show Databases"                 -Adds strings to MC object of databases in the system
#"Create Table <Name of Table(Value1 Type)>" -Creates a table based on a DDL command
#"Alter Table <Name of Table, Changes to table>" -Adds or deletes data related to table size
#"Show Tables"                    -Adds strings to MC object of tables

#Others can be used to manipulate the data in a table as well such as:
#"Insert Into" - Inserts rows into table
#"Delete From" - Deletes specific rows of table
#"Select" - Retrieves data from tables given data
#***************************************************************

db = mysql.connector.connect(host="localhost", #Connecting to a local database
                               user="root",
                               passwd="",
                               database="database1")

MC = db.cursor(buffered = True) #Creating Database object

#This code create the customers table in database 1
MC.execute("Create table customers (name VARCHAR(255), address VARCHAR(255))")

#This code adds some additional information into that table (A Row)
SQLCode = "Insert Into customers (name, address) Values (%s, %s)"
Values = [('John', 'Highway 21'),
          ('Joe', 'Pebble Beach Rd'),
          ('Karen', 'Forest Grove St')]
MC.executemany(SQLCode, Values)
db.commit()

#Any legal SQL statement can be passed through the execute statement
MC.execute("select name, address from customers")
Result = MC.fetchall()
for x in Result:
    print(x)

#Parts of a result can also be returned using fetchone() instead
MC.execute("select * from customers")
Result = MC.fetchone()
print(Result)

#Deleting data from a database is also used by the execute() function
MC.execute("DELETE FROM customers")
db.commit()
print(MC.rowcount, "record(s) deleted")

#To prevent SQL injection, a common hacking method, it is a good idea to use
#the '%' operator as a placeholder for data
SQLCommand = "select * from customers where name = %s"
Name = ("John", )
MC.execute(SQLCommand, Name)
Result = MC.fetchone()
print(Result)

#Since this table is no longer useful, time to drop it
MC.execute("drop table customers")
