#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 12:34:34 2020

@author: sebasbocaccio
"""

#Este simple programa agarra un link de wikipedia, encuentra todos los links desde esa direccion y elije uno
#para volver a iniciar el proceso; Tambien printea cual fue el articulo elejido. ( Utiliza random para elejir )
        
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import datetime
import random
import re

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    try:
         html = urlopen('http://en.wikipedia.org{}'.format(articleUrl))
    except HTTPError as e:
        return None
    try: 
        bs = BeautifulSoup(html, 'html.parser')
        return bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))
    except AttributeError as e:
        return None
    
  

links = getLinks('/wiki/Kevin_Bacon')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)        