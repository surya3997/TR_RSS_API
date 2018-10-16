#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 12:40:50 2018

@author: guru
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
from threading import Thread
from queue import Queue
import re
import sys


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
    for post in nm.find_all('a'):
        post_name = post.text
        post_url = post.attrs['href']
        links[post_name] = post_url
        
    movie_list[name]=links
    
def doWork():
    while True:
        post, url = q.get()
        mag_link = getmaglink(url)
        movie_list[name]=(url,mag_link)
        q.task_done()

def getmaglink(url):
    try:
        post_soup=BeautifulSoup(urlopen(url),'lxml')
        return post_soup.find('a',attrbs={'href':re.compile('magent')})
    except:
        return None

concurrent = len(movie_list)*5
q = Queue(concurrent)
for i in range(concurrent):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()

for movie in movie_list:
    try:
        for post_url in movie_list.items():
            q.put((movie, post_url))
        q.join()
    except KeyboardInterrupt:
        sys.exit()