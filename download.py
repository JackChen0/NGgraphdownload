# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 23:55:07 2019

@author: stu30
"""
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request as url
import re
  
x = []

html ='https://www.natgeomedia.com/'
request = url.Request(html, headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/73.0.3683.103 Safari/537.36'})
newhtml = urlopen(request).read().decode('utf-8')

soup = BeautifulSoup(newhtml, features ="html.parser")

import os

os.makedirs('C:/Users/stu30/Desktop/coding/bug/img', exist_ok=True)

#print(soup.title.string) #TITLE
subtitle = soup.find_all('img',{'src':re.compile('.*?\.jpg')})
for j in subtitle:
    j = j['src'] #取SRC標籤內容
  
#    r = requests.get(j, stream=True)
#    image_name = j.split('/')[-1]
#    with open('./img/%s' % image_name, 'wb') as f:
#        for chunk in r.iter_content(chunk_size=128):
#            f.write(chunk)
#    print('Saved %s' % image_name)
   
    r = requests.get(j, stream=True) #隨下載隨看 
    rename = j.split('/')[-1] #訂立名方式
    with open('C:/Users/stu30/Desktop/photo/%s'%rename, 'wb') as f: 
        #存檔位址以及命名方式
        for chunk in r.iter_content(chunk_size=128): #下載速率
            f.write(chunk)
            print('Saved %s' % rename)

   
