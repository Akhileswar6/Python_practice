# Example 2: Inserting Multiple Rows
# importing required libraries
import mysql.connector
 
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="Akhil@0109",
  database = "gfg"
)

# preparing a cursor object
cursorObject = dataBase.cursor()
 
sql = "INSERT INTO STUDENT (NAME, BRANCH, ROLL, SECTION, AGE)\
VALUES (%s, %s, %s, %s, %s)"
val = [("Nikhil", "CSE", "98", "A", "18"),
       ("Nisha", "CSE", "99", "A", "18"),
       ("Rohan", "MAE", "43", "B", "20"),
       ("Amit", "ECE", "24", "A", "21"),
       ("Anil", "MAE", "45", "B", "20"), 
       ("Megha", "ECE", "55", "A", "22"), 
       ("Sita", "CSE", "95", "A", "19")]
  
cursorObject.executemany(sql, val)
dataBase.commit()
  
# disconnecting from server
dataBase.close()