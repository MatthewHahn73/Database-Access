import mysql.connector

db = mysql.connector.connect(host="localhost", #Connecting to a local database
                               user="",
                               passwd="",
                               database="database1")

MC = db.cursor() #Creating Database object

#The execute function takes in a string parameter of DDL SQL commands to manipulate a databse
#Some examples are:
#"Create Database <DatabaseName>" -Creates new database
#"Show Databases"                 -Adds strings to MC object of databases in the system
#"Create Table <Name of Table(Value1 Type)>" -Creates a table based on a DDL command
#"Alter Table <Name of Table, Changes to table>" -Adds or deletes data related to table size
#"Show Tables"                    -Adds strings to MC object of tables

#This code create the customers table in database 1
MC.execute("Create table customers (name VARCHAR(255), address VARCHAR(255))")

#This code adds some additional information into that table (A Row)
SQLCode = "Insert Into customers (name, address) Values (%s, %s)"
Values = [('John', 'Highway 21'),
          ('Joe', 'Pebble Beach Rd')
          ('Karen', 'Forest Grove St')]
MC.execute(SQLCode, Values)
db.commit()
