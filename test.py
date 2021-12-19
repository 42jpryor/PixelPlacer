import requests
from time import sleep
from PIL import Image
from datetime import datetime

url = 'https://pixelplacer-python-flask.jmunger.repl.co/?fbclid=IwAR2O9_jdA6xenIeVT4sNXS26-AYG8cbiDYq5s8PtiExzC4_FkQd5R9aPPr8'
totalPixels = 0

now = datetime.now()
currentTime = now.strftime("%H:%M:%S")
print("Starting at " + currentTime)

for x in range(5):
    for y in range(5):
        myobj = {'x': x,
        'y' : y,
        'color' : 'red'
        }
        requestText = requests.post(url, data = myobj)
        totalPixels+=1
        print("Printed pixel at: X:" + str(x) + "  Y:" + str(y), end ="\r")
        sleep(1)

# print(requestText.text)
print("42 has been printed")
print("Number of pixels painted: " + str(totalPixels))
now = datetime.now()
currentTime = now.strftime("%H:%M:%S")
print("Ending at " + currentTime)