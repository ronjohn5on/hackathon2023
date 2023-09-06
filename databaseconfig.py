import mysql.connector    #pip install mysql-connector-python

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="wenjie",      #replace with your password
	)

my_cursor = mydb.cursor()

databasename = "nutriguide"    #enter database name
my_cursor.execute("CREATE DATABASE {}".format(databasename))    #Uncomment to Create Database 
#my_cursor.execute("DROP DATABASE {}".format(databasename))      #Uncomment to Delete Database

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
	print(db)