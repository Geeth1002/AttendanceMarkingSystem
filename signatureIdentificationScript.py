from tkinter import Image

import cv2
import pytesseract
import mysql.connector
import imutils
import numpy
#aaa
# Create Database Connection
from PIL.ImageOps import grayscale

mydb = mysql.connector.connect(host="localhost", user="root", passwd="");
mycursor = mydb.cursor()
mycursor.execute("use attendance")
# mycursor.execute("ALTER TABLE `attend` ADD `day1` VARCHAR(50) NOT NULL AFTER `name`;")

# import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract\\tesseract.exe";

# Load image
x = int(input("Enter the day : "));

if (x == 1):
    img = cv2.imread('1.png')
    query = 'UPDATE attend set day1=%s where id=%s'
    mycursor.execute("ALTER TABLE `attend` ADD `day1` VARCHAR(50) NOT NULL AFTER `name`;")
if (x == 2):
    img = cv2.imread('2.png')
    query = 'UPDATE attend set day2=%s where id=%s'
    mycursor.execute("ALTER TABLE `attend` ADD `day2` VARCHAR(50) NOT NULL AFTER `day1`;")
if (x == 3):
    img = cv2.imread('3.png')
    query = 'UPDATE attend set day3=%s where id=%s'
    mycursor.execute("ALTER TABLE `attend` ADD `day3` VARCHAR(50) NOT NULL AFTER `day2`;")
if (x == 4):
    img = cv2.imread('4.png')
    query = 'UPDATE attend set day4=%s where id=%s'
    mycursor.execute("ALTER TABLE `attend` ADD `day4` VARCHAR(50) NOT NULL AFTER `day3`;")
if (x == 5):
    img = cv2.imread('5.png')
    query = 'UPDATE attend set day5=%s where id=%s'
    mycursor.execute("ALTER TABLE `attend` ADD `day5` VARCHAR(50) NOT NULL AFTER `day4`;")

# First Iteration
# Crop Image and get index number
x = 80
y = 275
w = 120
h = 20
cropImg1 = img[y:y + h, x:x + w]
cv2.imshow("Segmentation",cropImg1)
img1 = cv2.cvtColor(cropImg1, cv2.COLOR_BGR2RGB);
cv2.imshow("BGR to RGB",img1)
image = imutils.resize(img1, width=612, height=800)
cv2.imshow("Resacle Image",image)
id = (pytesseract.image_to_string(image));
id = id.strip()
status = str("absence")

# crop image and get Signature
sigx = 530
sigy = 275
sigw = 135
sigh = 20
cropSigImg = img[sigy:sigy + sigh, sigx:sigx + sigw]
cv2.imshow("Segmentation Signature")
grayImage1 = cv2.cvtColor(cropSigImg, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Scale",grayImage1)
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage1, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("black & white",blackAndWhiteImage)
whitepix = numpy.sum(blackAndWhiteImage == 0)
# print(whitepix);
if (whitepix > 100):
    status = str("present")
else:
    status = str("absence")
print(id)
print(status)

mycursor.execute(query, (status, id));

# Second Iteration
# Crop Image and get index number
x = 80
y = 300
w = 120
h = 20
cropImg1 = img[y:y + h, x:x + w]
img1 = cv2.cvtColor(cropImg1, cv2.COLOR_BGR2RGB);
image = imutils.resize(img1, width=612, height=800)
id = (pytesseract.image_to_string(image));
id = id.strip()

# crop image and get signature
sigx = 530
sigy = 305
sigw = 135
sigh = 20
cropSigImg = img[sigy:sigy + sigh, sigx:sigx + sigw]
grayImage1 = cv2.cvtColor(cropSigImg, cv2.COLOR_BGR2GRAY)
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage1, 127, 255, cv2.THRESH_BINARY)
whitepix = numpy.sum(blackAndWhiteImage == 0)
# print(whitepix);
if (whitepix > 100):
    status = str("present")
else:
    status = str("absence")
print(id)
print(status)

# mycursor.execute("UPDATE attend set day1=%s where id=%s",(status,id));
mycursor.execute(query, (status, id));

# Third Iteration
# Crop Image and get index number
x = 80
y = 330
w = 120
h = 20
cropImg1 = img[y:y + h, x:x + w]
img1 = cv2.cvtColor(cropImg1, cv2.COLOR_BGR2RGB);
image = imutils.resize(img1, width=612, height=800)
id = (pytesseract.image_to_string(image));
id = id.strip()

# crop image and get signature
sigx = 530
sigy = 330
sigw = 135
sigh = 20
cropSigImg = img[sigy:sigy + sigh, sigx:sigx + sigw]
grayImage1 = cv2.cvtColor(cropSigImg, cv2.COLOR_BGR2GRAY)
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage1, 127, 255, cv2.THRESH_BINARY)
whitepix = numpy.sum(blackAndWhiteImage == 0)
# print(whitepix);
if (whitepix > 100):
    status = str("present")
else:
    status = str("absence")
print(id)
print(status)

# mycursor.execute("UPDATE attend set day1=%s where id=%s",(status,id));
mycursor.execute(query, (status, id));

# Fourth Iteration
# Crop Image and get index number
x = 80
y = 355
w = 120
h = 20
cropImg1 = img[y:y + h, x:x + w]
img1 = cv2.cvtColor(cropImg1, cv2.COLOR_BGR2RGB);
image = imutils.resize(img1, width=612, height=800)
id = (pytesseract.image_to_string(image));
id = id.strip()

# crop image and get signature
sigx = 530
sigy = 360
sigw = 135
sigh = 20
cropSigImg = img[sigy:sigy + sigh, sigx:sigx + sigw]
grayImage1 = cv2.cvtColor(cropSigImg, cv2.COLOR_BGR2GRAY)
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage1, 127, 255, cv2.THRESH_BINARY)
whitepix = numpy.sum(blackAndWhiteImage == 0)
# print(whitepix);
if (whitepix > 100):
    status = str("present")
else:
    status = str("absence")
print(id)
print(status)

# mycursor.execute("UPDATE attend set day1=%s where id=%s",(status,id));
mycursor.execute(query, (status, id));

# Fifth Iteration
# Crop Image and get index number
x = 80
y = 383
w = 120
h = 20
cropImg1 = img[y:y + h, x:x + w]
img1 = cv2.cvtColor(cropImg1, cv2.COLOR_BGR2RGB);
image = imutils.resize(img1, width=612, height=800)
id = (pytesseract.image_to_string(image));
id = id.strip()

# crop image and get signature
sigx = 530
sigy = 383
sigw = 135
sigh = 20
cropSigImg = img[sigy:sigy + sigh, sigx:sigx + sigw]
grayImage1 = cv2.cvtColor(cropSigImg, cv2.COLOR_BGR2GRAY)
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage1, 127, 255, cv2.THRESH_BINARY)
whitepix = numpy.sum(blackAndWhiteImage == 0)
# print(whitepix);
if (whitepix > 100):
    status = str("present")
else:
    status = str("absence")
print(id)
print(status)

# mycursor.execute("UPDATE attend set day1=%s where id=%s",(status,id));
mycursor.execute(query, (status, id));

# sixth Iteration
# Crop Image and get index number
x = 80
y = 409
w = 120
h = 20
cropImg1 = img[y:y + h, x:x + w]
img1 = cv2.cvtColor(cropImg1, cv2.COLOR_BGR2RGB);
image = imutils.resize(img1, width=612, height=800)
id = (pytesseract.image_to_string(image));
id = id.strip()

# crop image and get signature
sigx = 530
sigy = 409
sigw = 135
sigh = 20
cropSigImg = img[sigy:sigy + sigh, sigx:sigx + sigw]
grayImage1 = cv2.cvtColor(cropSigImg, cv2.COLOR_BGR2GRAY)
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage1, 127, 255, cv2.THRESH_BINARY)
whitepix = numpy.sum(blackAndWhiteImage == 0)
# print(whitepix);
if (whitepix > 100):
    status = str("present")
else:
    status = str("absence")
print(id)
print(status)

# mycursor.execute("UPDATE attend set day1=%s where id=%s",(status,id));
mycursor.execute(query, (status, id));

# cv2.imshow('Result',blackAndWhiteImage);
# cv2.waitKey(0);
