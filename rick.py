import requests
from time import sleep
from PIL import Image
from datetime import datetime

# Set the variables
url = 'https://pixelplacer-python-flask.jmunger.repl.co/?fbclid=IwAR2O9_jdA6xenIeVT4sNXS26-AYG8cbiDYq5s8PtiExzC4_FkQd5R9aPPr8'
totalPixels = 0
blue = (35, 41, 49, 255)
white = (255, 255, 255, 255)
sleepTime = 0.1
threshold = 100
threshold1 = 100
threshold2 = 150
threshold3 = 200

# Open the image
image = Image.open('Rick500.png')
pix = image.convert('RGB')
# pix = image.load()

# Create the blank new image
rickImage = Image.new(mode="RGB", size = (1000,1000), color=(255,255,255))
rickImage.save("rickImage.png")
rickImage = Image.open('rickImage.png')
rickPicture = rickImage.load()

def colorImage(x, y, totalPixels):
    try:
        if(rickPicture[x,y] == (255,0,0)):
            myobj = {'x': x,
            'y' : y,
            'color' : 'red'
            }
            requestText = requests.post(url, data = myobj)
            totalPixels+=1
            sleep(sleepTime)
        elif(rickPicture[x,y] == (0,255,0)):
            myobj = {'x': x,
            'y' : y,
            'color' : 'green'
            }
            requestText = requests.post(url, data = myobj)
            totalPixels+=1
            sleep(sleepTime)
        elif(rickPicture[x,y] == (0,0,255)):
            myobj = {'x': x,
            'y' : y,
            'color' : 'blue'
            }
            requestText = requests.post(url, data = myobj)
            totalPixels+=1
            sleep(sleepTime)
        
        print("Pixel Coords: (" + str(x) + "," + str(y) + ")   Pixels: " + str(totalPixels), end ="\r")
    except:
        print("Error")
        sleep(10)
        colorImage(x, y, totalPixels)

# Loop through the image reading the pixels and creating the new image to be used
for x in range(500):
    for y in range(500):
        r, g, b = pix.getpixel((x,y))
        if(r <= threshold+30):
            rickPicture[x*2,y*2] = (255, 0, 0)
            totalPixels+=1
        if(g <= threshold):
            rickPicture[x*2,y*2+1] = (0, 255, 0)
            totalPixels+=1
        if(b <= threshold):
            rickPicture[x*2+1,y*2+1] = (0, 0, 255)
            totalPixels+=1

# Save the image
rickImage.save("rickImage.png")
rickImage.show()

# Prompt if you actually want to make the image
print("Total pixel placement count: " + str(totalPixels))
print('Create Image? (Y/N)')
inputString = input()


if(inputString == 'Y'):
    now = datetime.now()
    currentTime = now.strftime("%H:%M:%S")
    print("Starting at " + currentTime)

    totalPixels = 0
# Sends the data to the server
    for x in range(1000):
        for y in range(1000):
            colorImage(x,y,totalPixels)

    
    # print(requestText.text)
    print("42 has been printed")
    print("Number of pixels painted: " + str(totalPixels))
    print("Number of minutes:" + str(totalPixels/60))
    now = datetime.now()
    currentTime = now.strftime("%H:%M:%S")
    print("Ending at " + currentTime)
else:
    print("Alright fine bitch I'm not gonna draw the picture")