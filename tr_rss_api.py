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

nms = tnm.find_all("br")
