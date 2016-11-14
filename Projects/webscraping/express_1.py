import urllib
import urllib.request
from bs4 import BeautifulSoup
import requests
import re
import datetime
import time
from random import randint
import csv


def search_page(str):
    theurl = "http://www.xpres.co.uk/search.aspx?SearchTerm="+ str + "&IsSubmit=true&submitBtn=&PageSize=999999&SubmitRefresh=Search"
    thepage = urllib.request.urlopen(theurl)
    soupdata = BeautifulSoup(thepage, "html5lib")
    return soupdata


#seach term
search_word = search_page("unisub")

#define base of internal links
urllead = "http://www.xpres.co.uk/"

#Load internal url's from search page into array
inturls = []

for link in search_word.findAll('a',{"class":"product-thumb text-center"}, href=True):
    url = link.get('href')
    inturls.append(urllead+url)




i = int(0)
n = int(len(inturls))
data = []

for i in inturls:
    url=i
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html5lib")
    sku = soup.find('div', attrs={'class':'col-md-5 description-size'}).contents[0].text
    item = soup.find('div', attrs={'class':'col-md-5 description-size'}).contents[1].text
    for a in soup.findAll('div', attrs={'class':'qbreak-variant'}):
        qty = a.contents[0].text.strip()
        price = a.contents[2].string.replace(' ea\n', '').strip()
        data.append([sku, item,"'"+qty, price])
    time.sleep(randint(0,9))

#gets date time for file name
fd = datetime.datetime.now()
fd_str = str(fd.strftime('%d-%m-%Y'))

#write date to csv
filename = 'express'+fd_str+'.csv'

with open(filename, 'w', newline='') as exp:
 a = csv.writer(exp, delimiter=',')
 a.writerows(data)
exp.close()
