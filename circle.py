import requests
from time import sleep
from PIL import Image
from datetime import datetime
import math

originLocation = (500,500)
startLocationX = 445
startLocationY = 5
radianRotation = 0

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy



url = 'https://pixelplacer-python-flask.jmunger.repl.co/?fbclid=IwAR2O9_jdA6xenIeVT4sNXS26-AYG8cbiDYq5s8PtiExzC4_FkQd5R9aPPr8'
totalPixels = 0

blue = (35, 41, 49, 255)
white = (255, 255, 255, 255)

smallerimage = Image.open('42small.png')
smallerPix = smallerimage.load()

newImage = Image.new(mode="RGB", size = (1000,1000), color=(255,255,255))
newImage.save("createdImage.png")
newImage = Image.open('createdImage.png')
newPicture = newImage.load()


now = datetime.now()
currentTime = now.strftime("%H:%M:%S")
print("Starting at " + currentTime)

for z in range(48):
    degreeRotation = 30 * z
    startLocationY+=5
    for x in range(1,50):
        for y in range(1, 50):
            if(smallerPix[x,y] != white and smallerPix[x,y] != blue):
                tempX = startLocationX + x
                tempY = startLocationY + y
                startLocation = (tempX, tempY)
                newX, newY = rotate(originLocation, startLocation, math.radians(degreeRotation))
                myobj = {'x': int(newX),
                'y' : int(newY),
                'color' : 'red'
                }
                requestText = requests.post(url, data = myobj)
                # print(requestText.text)
                totalPixels+=1
                print("Printed pixel at: X:" + str(newX) + "  Y:" + str(newY), end ="\r")
                sleep(1)

        

# print(requestText.text)
print("42 has been printed")
print("Number of pixels painted: " + str(totalPixels))
print("Number of minutes:" + str(totalPixels/60))
now = datetime.now()
currentTime = now.strftime("%H:%M:%S")
print("Ending at " + currentTime)