#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 19:44:43 2020

@author: sebasbocaccio
"""

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
#from "home/sebasbocaccio/Desktop/Scrappy/messi import parse

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(),features="lxml")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title


title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
#title = getTitle("https://www.clarin.com/")

if title == None:
    print("Title could not be found")
else:
 
    print(title)