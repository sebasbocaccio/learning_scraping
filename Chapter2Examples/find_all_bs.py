#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 21:45:40 2020

@author: sebasbocaccio
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")

bsObj = BeautifulSoup(html)

nameList = bsObj.findAll("span", {"class":"green"})

for name in nameList:
    print(name.get_text())