import requests
from bs4 import BeautifulSoup
import csv
   
URL = "https://townhall.hashnode.com/table-of-contents-feature"
r = requests.get(URL)
   
soup = BeautifulSoup(r.content, 'html5lib')
   
contents=[]  # a list to store quotes
   
table = soup.find('div', attrs = {'class':'blog-content-wrapper article-main-wrapper css-m96uju'}) 
   
for row in table.findAll('div',
                         attrs = {'class':'css-bjn8wh'}):
    content = {}
    content['img'] = row.img['src']    
    contents.append(content)
   
filename = 'contents.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['img'])
    w.writeheader()
    for content in contents:
        w.writerow(content)