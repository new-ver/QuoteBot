from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import urllib.request
import json
import random
import textwrap

#Get a image from picsum
urllib.request.urlretrieve("https://picsum.photos/1080", "00000001.jpg")

f = open('quotes.json')
quotes = json.load(f)

#Select a random quote from the json file
num = random.randint(0,len(quotes)-1)
thisQuote = quotes[num].get("text")

img = Image.open("00000001.jpg")
lines = textwrap.wrap(thisQuote, width=25)
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("LongLiner.ttf", 95)

#Get the largest letter in the font
line_height = font.getsize('hg')[1]
y_text = 0
x = 0
for line in lines:
    draw.text((50, y_text),line,(255,255,255),font=font, align = "left")
    y_text += line_height


#Draw the author
draw.text((50, y_text+line_height),"- " + quotes[num].get("author"),(255,255,255),font=font, align = "left")

img.save('sample-out.jpg')
