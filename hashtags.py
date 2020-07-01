#Get Hashtags to go along with the photo
import random

hashtags = ["#changestartswithyou", "#youhavethepower", "#changeisgood", "#bliss", "#calm","#zen", "#goodlife", "#life", "#lifequotestoliveby", "#mindful", "#mindfulness", "#dream", "#dreambig", "#igquotes", "#words", "#embracechange", "#lessonlearned", "#lifelessons", "#sayings", "#motivaion", "#motivational", "#inspiration", "#inspiration", "#inspirationalwords", "#dailyinspiration", "#dailyquotes", "#quotes", '#quotesdaily', '#innerpeace', '#powerofnow', '#wisewords', '#thoughtoftheday', '#quoteslover', '#thoughtfulquotes', '#wordstoremember', '#innerpeace', '#believe']
list = []
for x in range (0,20):
    num = random.randint(0, len(hashtags)-1)
    if(hashtags[num] not in list):
        list.append(hashtags[num])

f = str(list).replace(',', '').replace("'","")
print(f)
