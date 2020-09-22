import mysql.connector
import matplotlib.pyplot as plt
import shlex


mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="attendance")
mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM attend")
myresult=mycursor.fetchall()

y=0
arr =[]
arrname=[]
for row in myresult :
    print(row)
    for t in row:
        # print(t)
        if (t == 'present'):
            y=y+1
    arr.append(y)
    y=0
print('\nAttendance Presentage : \n')
# print(arr)

a = arr[0]*20
b = arr[1]*20
c = arr[2]*20
d = arr[3]*20
e = arr[4]*20
f = arr[5]*20

print("10000409 : " + str(a)+"%")
print("10009301 : " + str(b)+"%")
print("10009302 : " + str(c)+"%")
print("10009303 : " + str(d)+"%")
print("10009304 : " + str(e)+"%")
print("10009306 : " + str(f)+"%")


#Student 1
labels = 'Present', 'Absent'
sizes = [a,100-a]
explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Ms. M S Dilshanika Perera - 10000409\n')
plt.show()

#Student 2
labels = 'Present', 'Absent'
sizes = [b,100-b]
explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Mr. C W M A Shehan Abeyrathne - 10009301\n')
plt.show()

#Student 3
labels = 'Present', 'Absent'
sizes = [c,100-c]
explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Mr. B A K M Chithrananda - 10009302\n')
plt.show()

#Student 4
labels = 'Present', 'Absent'
sizes = [d,100-d]
explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Ms. W Shashini Minosha De Silva - 10009303\n')
plt.show()


#Student 5
labels = 'Present', 'Absent'
sizes = [e,100-e]
explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Mr. K L Udara Maduranga Liyanage - 10009304\n')
plt.show()

#Student 6
labels = 'Present', 'Absent'
sizes = [f,100-f]
explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Mr. Hansa Anuradha Wickramanayake - 10009306\n')
plt.show()








