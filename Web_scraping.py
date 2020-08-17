from bs4 import BeautifulSoup
import requests
import html5lib
import csv
import json


url="https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=men++sunglasses&_sacat=0"

r = requests.get(url)

soup=BeautifulSoup(r.content,'html5lib')
print(soup.prettify())

items=[]

table=soup.find('div',attrs={'class':"srp-river srp-layout-inner"})

print(table)

for row in table.findAll('div',attrs={'class':'s-item__wrapper clearfix'}):
    item={}
    item['Title']=row.h3.text
    item['Image']=row.img['src']
    items.append(item)

filename='sunglass2.csv'
with open(filename, 'w',newline='') as f:
    w=csv.DictWriter(f,['Title','Image'])
    w.writeheader()

    for item in items:
        w.writerow(item)
