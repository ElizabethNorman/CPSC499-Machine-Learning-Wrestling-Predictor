import urllib
from urllib.request import urlopen
import requests
import gzip
from bs4 import BeautifulSoup
import time

headers = {'Accept-Encoding': 'deflate'}
response = requests.get("https://www.cagematch.net/?id=112&view=search&sParticipant1=&sParticipant2=&sParticipant3=&sParticipant4=&sEventName=&sEventType=&sDateFromDay=01&sDateFromMonth=01&sDateFromYear=2019&sDateTillDay=07&sDateTillMonth=11&sDateTillYear=2020&sPromotion=2287&sLocation=&sArena=&sRegion=&sMatchType=&sConstellation=Singles&sWorkerRelationship=Any&sFulltextSearch=", headers=headers)
# print(response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')

matches = soup.find_all(class_="TCol TColSeparator")

f = open("AEWSinglesMatches3.txt", "a")

for m in range(len(matches)):
    f.write(matches[m].getText())

url = 'https://www.cagematch.net/?id=112&view=search&sDateFromDay=01&sDateFromMonth=01&sDateFromYear=2019&sDateTillDay=07&sDateTillMonth=11&sDateTillYear=2020&sPromotion=2287&sConstellation=Singles&sWorkerRelationship=Any&s=100'
url = url[0:len(url)-3]

for x in range(4):
    print("STARTING PAGE", x+1)

    time.sleep(60)

    url = url + str((x+1)*100)

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')
    matches = soup.find_all(class_="TCol TColSeparator")

    for m in range(len(matches)):
        f.write(matches[m].getText())

    url = url[0:len(url) - 3]


f.close()
