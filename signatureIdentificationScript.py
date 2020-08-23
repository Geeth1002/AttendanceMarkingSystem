from tkinter import Image

import cv2
import pytesseract
import mysql.connector
import imutils
import numpy

# Create Database Connection
from PIL.ImageOps import grayscale

mydb = mysql.connector.connect(host="localhost", user="root", passwd="");
mycursor = mydb.cursor()
mycursor.execute("use attendance")
# mycursor.execute("ALTER TABLE `attend` ADD `day1` VARCHAR(50) NOT NULL AFTER `name`;")

# import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract\\tesseract.exe";

# Load image
x = input("Enter the day");
img = cv2.imread('1.png')
if (x == 1):
    img = cv2.imread('1.png');
    mycursor.execute("ALTER TABLE `attend` ADD `day1` VARCHAR(50) NOT NULL AFTER `name`;")
if (x == 2):
    img = cv2.imread('2.png')
    mycursor.execute("ALTER TABLE `attend` ADD `day2` VARCHAR(50) NOT NULL AFTER `day1`;")
if (x == 3):
    img = cv2.imread('3.png')
    mycursor.execute("ALTER TABLE `attend` ADD `day3` VARCHAR(50) NOT NULL AFTER `day2`;")
if (x == 4):
    img = cv2.imread('4.png')
    mycursor.execute("ALTER TABLE `attend` ADD `day4` VARCHAR(50) NOT NULL AFTER `day3`;")
if (x == 5):
    img = cv2.imread('5.png')
    mycursor.execute("ALTER TABLE `attend` ADD `day5` VARCHAR(50) NOT NULL AFTER `day4`;")

    # First Iteration
# Crop Image and get index number
x = 80
y = 275
w = 120
h = 20
cropImg1 = img[y:y + h, x:x + w]
img1 = cv2.cvtColor(cropImg1, cv2.COLOR_BGR2RGB);
image = imutils.resize(img1, width=612, height=800)
id = (pytesseract.image_to_string(image));
id = id.strip()
status = str("absence")

# crop image and get Signature
sigx = 530
sigy = 275
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

mycursor.execute("UPDATE attend set day1=%s where id=%s", (status, id));

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

mycursor.execute("UPDATE attend set day1=%s where id=%s", (status, id));

# Third Iteration
# Crop Image and get index number
x = 83
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

mycursor.execute("UPDATE attend set day1=%s where id=%s", (status, id));

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
sigy = 355
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

mycursor.execute("UPDATE attend set day1=%s where id=%s", (status, id));
# gggg


# cv2.imshow('Result',blackAndWhiteImage);
# cv2.waitKey(0);
