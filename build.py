import os
import sys
import io
import datetime
import xml.dom.minidom
import requests
import feedparser

url = 'https://chrisevans9629.github.io/feed.xml'

#result = requests.get(url)

d = feedparser.parse(url)

#print(d.feed.title)

#print(d.entries[:3])


def getItems():
    items = sorted(d.entries[:5],key=lambda i: i.updated, reverse=True)
    return [{"title": item.title, "url": item.link} for item in items]

items = "".join([ "- [{}]({})\n".format(item["title"],item["url"]) for item in getItems()])


readmecontent = open('README.md','r').read()

def changeContent(str,change,start,end):
    sindex = str.find(start)+len(start)
    eindex = str.find(end)

    result = str[:sindex] + change + str[eindex:]
    return result


#print(changeContent('test[[hello!]]','test','[[',']]'))

newContent = changeContent(readmecontent,items, "<!--blog-start-->\n","<!--blog-ends-->\n")

print(newContent)



dataFile = open('data.txt', 'w')

time = datetime.datetime.now().strftime('%d/%m/%y %I:%M %S %p')

dataFile.write('hello world! ' + time)

print(sys.argv)

