import mysql
import mysql.connector
import xml.etree.ElementTree as ET
import mysql.connector
from mysql.connector import connect


mydb= mysql.connector.connect(host="localhost", user="root",passwd="");
mycursor=mydb.cursor()
createDB="CREATE DATABASE attendance";
use="USE attendance"
createtable="CREATE TABLE `attendance`.`attend` ( `id` VARCHAR(12) NOT NULL , `title` VARCHAR(4) NOT NULL , `name` VARCHAR(100) NOT NULL , PRIMARY KEY (`id`)) ENGINE = MyISAM";

mycursor.execute(createDB);
mycursor.execute(use)
mycursor.execute(createtable);



conn = mysql.connector.connect(user='root', password='',
                               host='localhost', database='attendance')


if conn:
    print("Connected Successfully")
else:
    print("Connection Not Established")

tree = ET.parse('studentNames.xml')

std = tree.findall('students')

for ep in std:
    #eid = ep.find('number').text
    no = ep.find('studentNumber').text
    title = ep.find('title').text
    name = ep.find('studentName').text

    print(no)


    cursor = conn.cursor()
    cursor.execute("INSERT INTO attend (id,title,name) VALUES(%s,%s,%s)", (no, title, name))
    conn.commit()
    print("Data inserted succussfully")
