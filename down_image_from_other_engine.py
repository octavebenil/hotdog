import requests
import re
import os
from bs4 import BeautifulSoup


def duckduckgo(query):
    print("DuckDuckGo engine")
    url = "https://duckduckgo.com/?q={}&t=h_&iar=images&iaf=size%3AMedium&iax=images&ia=images"
    url = url.format(query)
    img_src = []
    try:
        response = requests.get(url)
        page = BeautifulSoup(response.text,'html.parser')
        links = page.findAll('img')
        for l in links:
            # print(l['src'])
            img_src.append(l['src'])
    except:
        print("link dead")
    return img_src

def bing(query):
    print("Bing engine")
    url = "https://www.bing.com/images/search?cw=1465&ch=681&q={}&qft=+filterui:imagesize-medium+filterui:photo-photo&FORM=IRFLTR"
    url = url.format(query)
    img_src = []
    try:
        response = requests.get(url)
        page = BeautifulSoup(response.text,'html.parser')
        links = page.findAll('img')
        for l in links:
            # print(l['src'])
            img_src.append(l['src'])
    except:
        print("link dead")
    return img_src

def google(query):
    print("Google engine")
    url = "https://www.google.com/search?q={}&tbm=isch&source=lnt&tbs=isz:m&sa=X&ved=0ahUKEwjvoKS6ssXiAhUl5eAKHaF6BLYQpwUIIA&biw=1470&bih=701&dpr=0.9"
    url = url.format(query)
    img_src = []
    try:
        response = requests.get(url)
        page = BeautifulSoup(response.text,'html.parser')
        links = page.findAll('img')
        for l in links:
            # print(l['src'])
            img_src.append(l['src'])
    except:
        print("link dead")
    return img_src

imgs_src = []
query="pizza"

du = duckduckgo(query)
bi = bing(query)
go = google(query)

for d in du:
     imgs_src.append(d)

for d in bi:
     imgs_src.append(d)

for d in go:
     imgs_src.append(d)

print(imgs_src)

if len(imgs_src) > 0:
    list_f = open(query+"_urls_list.txt", "w")
    for url in imgs_src:
        print(url)
        list_f.write(url)
    list_f.close()
