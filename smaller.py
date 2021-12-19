import requests
from time import sleep
from PIL import Image
from datetime import datetime


url = 'https://pixelplacer-python-flask.jmunger.repl.co/?fbclid=IwAR2O9_jdA6xenIeVT4sNXS26-AYG8cbiDYq5s8PtiExzC4_FkQd5R9aPPr8'
totalPixels = 0

blue = (35, 41, 49, 255)
white = (255, 255, 255, 255)

image = Image.open('42.png')
pix = image.load()

smallerimage = Image.open('42small.png')
smallerPix = smallerimage.load()


now = datetime.now()
currentTime = now.strftime("%H:%M:%S")
print("Starting at " + currentTime)

for x in range(687,1000):
    for y in range(1,1000):
        if(pix[x,y] == white):
            modx = x%50
            mody = y%50
            if(smallerPix[modx,mody] != blue and x%2==0 and y%2==0):
                myobj = {'x': x,
                'y' : y,
                'color' : 'red'
                }
                requestText = requests.post(url, data = myobj)
                totalPixels+=1
                print("Printed pixels: " + str(totalPixels), end ="\r")
                sleep(1)

        

# print(requestText.text)
print("42 has been printed")
print("Number of pixels painted: " + str(totalPixels))
print("Number of minutes:" + str(totalPixels/60))
now = datetime.now()
currentTime = now.strftime("%H:%M:%S")
print("Ending at " + currentTime)