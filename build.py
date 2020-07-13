import os
import sys
import io
import datetime
import xml.dom.minidom
import requests
import feedparser

url = 'https://chrisevans9629.github.io/feed.xml'

d = feedparser.parse(url)

def getItems():
    items = sorted(d.entries[:5],key=lambda i: i.updated, reverse=True)
    return [{"title": item.title, "url": item.link, "updated": item.updated.split('T')[0] } for item in items]

items = "".join([ "- [{} - {}]({})\n".format(item["title"],item["updated"],item["url"]) for item in getItems()])

readmeFile = 'README.md'
readmecontent = open(readmeFile,'r').read()

def changeContent(str,change,start,end):
    sindex = str.find(start)+len(start)
    eindex = str.find(end)

    result = str[:sindex] + change + str[eindex:]
    return result

newContent = changeContent(readmecontent,items, "<!--blog-start-->\n","<!--blog-ends-->\n")

open(readmeFile,'w').write(newContent)

