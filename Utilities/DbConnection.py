import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="faizi_FORu65",
    database="pydbprc1"
)
mycursor=mydb.cursor()
mycursor.execute("select tutorial_author from seleniumprac where tutorial_id=2")
myresult=mycursor.fetchone()
print(myresult[0])