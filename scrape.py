# 1. image comparison with image data(scraping) from Ebay then get the price

# 2. using search by image API then grab the price
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=dumbell&_sacat=0"

def getData(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup

def parse(soup):
    productlist = []
    results = soup.find_all("div",{"class":"s-item__wrapper clearfix"})
    for item in results:
        product = {
            'title': item.find("div",{"class":"s-item__title"}).text,
            'price': item.find("span",{"class":"s-item__price"}).text,
            'image': item.find("div", {"class":"s-item__image-wrapper image-treatment"}).find('img')['src']
        }
        productlist.append(product)
    return productlist

def output(productlist):
    productdf = pd.DataFrame(productlist)
    productdf.to_csv("dumbell data.csv", index=False)

soup = getData(url)
productlist = parse(soup)
output(productlist)