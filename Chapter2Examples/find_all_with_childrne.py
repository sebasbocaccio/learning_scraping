#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 16:02:41 2020

@author: sebasbocaccio
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
#html = urlopen("http://www.pythonscraping.com/pages/page3.html")
#bsObj = BeautifulSoup(html, 'html.parser')

#for child in bsObj.find("table",{"id":"giftList"}).children:
 #   print(child)
    
    
#html=urlopen('http://www.pythonscraping.com/pages/page3.html')
#bs=BeautifulSoup(html,'html.parser')
#for child in bs.find('table',{'id':'giftList'}).children:
#    print(child)
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)