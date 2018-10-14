#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 12:40:50 2018

@author: guru
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
url = "http://tamilrockers.hn"
html = urlopen(url)
soup = BeautifulSoup(html, "lxml")

firstpost = soup.find(class_="ipsType_textblock")
tnmheader = firstpost.find(string=re.compile("Tamil New Movies"))
tnm = tnmheader.find_next("strong")

nms = str(tnm).split("<br/>")

movie_list = {}

for nm in nms:
    nm = BeautifulSoup(nm,'lxml')
    name = nm.text.split(' - [')[0]
    links = {}
    for qual in nm.find_all('a'):
        qual_link = qual.attrs['href']
        qual_name = qual.text
        links[qual_name] = qual_link
        
    movie_list[name]=links
    
