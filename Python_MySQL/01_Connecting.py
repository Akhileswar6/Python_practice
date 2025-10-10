# To install the Python-mysql-connector module, one must have Python and PIP, preinstalled on their system. If Python and pip are already installed type the below command in the terminal.
# pip3 install mysql-connector-python


# Connecting to MySQL Server

# importing required libraries
import mysql.connector
 
dataBase = mysql.connector.connect(
  host ="localhost",                # Localhost for local connection
  user ="root",
  passwd ="Akhil@0109"
)

print(dataBase)
 
# Disconnecting from the server
dataBase.close()
