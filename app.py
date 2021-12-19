import requests
from time import sleep
from PIL import Image
from datetime import datetime

url = 'https://pixelplacer-python-flask.jmunger.repl.co/?fbclid=IwAR2O9_jdA6xenIeVT4sNXS26-AYG8cbiDYq5s8PtiExzC4_FkQd5R9aPPr8'
totalPixels = 0

blue = (35, 41, 49, 255)
white = (255, 255, 255, 255)
sleepTime = 0.1
image = Image.open('42.png')
pix = image.load()

newImage = Image.new(mode="RGB", size = (1000,1000), color=(255,255,255))
newImage.save("createdImage.png")
newImage = Image.open('createdImage.png')
newPicture = newImage.load()

for x in range(1,1000):
    for y in range(1,1000):
        if(pix[x,y] != white and pix[x,y] != blue):
            if(x%2==0):
                if(y%2==0):
                    newPicture[x,y] = (0,0,255)
                else:
                    newPicture[x,y] = (255,0,0)
            else:
                if(y%2==1):
                    newPicture[x,y] = (0,0,255)
                else:
                    newPicture[x,y] = (255,0,0)
newImage.show()

print('Create Image? (Y/N)')
inputString = input()

if(inputString == 'Y'):
    now = datetime.now()
    currentTime = now.strftime("%H:%M:%S")
    print("Starting at " + currentTime)

    for x in range(1,1000):
        for y in range(1,1000):
            if(newPicture[x,y] == (0,0,255)):
                myobj = {'x': x,
                'y' : y,
                'color' : 'blue'
                }
                requestText = requests.post(url, data = myobj)
                totalPixels+=1
                sleep(sleepTime)
            elif(newPicture[x,y] == (255,0,0)):
                myobj = {'x': x,
                'y' : y,
                'color' : 'red'
                }
                requestText = requests.post(url, data = myobj)
                totalPixels+=1
                sleep(sleepTime)

            print("Pixels: " + str(totalPixels), end ="\r")

    # print(requestText.text)
    print("42 has been printed")
    print("Number of pixels painted: " + str(totalPixels))
    print("Number of minutes:" + str(totalPixels/60))
    now = datetime.now()
    currentTime = now.strftime("%H:%M:%S")
    print("Ending at " + currentTime)
else:
    print("Alright fine bitch I'm not gonna draw the picture")