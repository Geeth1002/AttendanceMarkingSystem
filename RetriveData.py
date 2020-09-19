import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="attendance")
mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM attend");
myresult=mycursor.fetchall();

for row in myresult:
    print(row)