#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 19:55:42 2020

@author: sebasbocaccio
"""
#Con este programa, vamos recorriendo todos los links de wikipedia recursivamente SIN REPETIR
#Este Programa busca los links desde el home de wikipedia y va buscando y recorriendo todos los links todavia no recorridos. 

# OJO: NO esta tenido en cuenta que esto puede fallar. 
#Tendrias que arreglar esto con try y except como en archivo wikipedia_links

# OJO 2 : Una funcion recursiva en python solo puede ser llamada 1000 veces. 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #We have encountered a new page
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks('')