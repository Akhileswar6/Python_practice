# Creating Database -> After connecting to the MySQL server let's see how to create a MySQL database using Python. For this, we will first create a cursor() object and will then pass the SQL command as a string to the execute() method. 
# Creating MySQL database with Python

# importing required libraries
import mysql.connector
 
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="Akhil@0109"
)

# preparing a cursor object
cursorObject = dataBase.cursor()

# creating database
cursorObject.execute("CREATE DATABASE python")

