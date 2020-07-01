from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import urllib.request
import json
import random
import textwrap

#For generating random quotes
def getFont(i):
    switcher={
        1: "LongLiner.ttf",
        2: "Chasy.otf",
        3: "Summer.otf",
        4: "Lemon.otf",
        5: "Orange.ttf",
        6: "paper.ttf",
        7: "Shorelines.otf",
    }
    return switcher.get(i)

#Get a image from picsum
urllib.request.urlretrieve("https://picsum.photos/1080", "00000001.jpg")

#Open json file
f = open('quotes.json')
quotes = json.load(f)

#Select a random quote from the json file
num = random.randint(0,len(quotes)-1)
thisQuote = quotes[num].get("text")

#TODO Remove saving photo locally
img = Image.open("00000001.jpg")
lines = textwrap.wrap(thisQuote, width=25)
draw = ImageDraw.Draw(img)

#Get a random Font
fontNumber = random.randint(1,8)
font = ImageFont.truetype(getFont(fontNumber), 95)


#Get the largest letter in the font
if(fontNumber == 4):
    line_height = font.getsize('hg')[1] + 20
else:
    line_height = font.getsize('hg')[1]

y_text = 50
x = 0
for line in lines:
    draw.text((50, y_text),line,(255,255,255),font=font, align = "left")
    y_text += line_height


#Draw the author
draw.text((50, y_text+line_height),"- " + quotes[num].get("author"),(255,255,255),font=font, align = "left")

img.save('sample-out.jpg')
