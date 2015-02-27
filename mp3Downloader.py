"""
Kunal Chavhan
Github username: techcraze
Email: techcraze5@gmail.com
Date: 27/2/2015
Code description: It is an open source code which uses URLLIB module to download mp3 songs from www.mymp3singer.com.
                  
"""


import urllib
import os
from bs4 import BeautifulSoup
import re

def artistSearch(artist):
    urlSearch = "http://mymp3singer.com/song_search.php?search="+artist
    dir = os.getcwd()
    print "searching for keyword "+artist+" in mp3singer.com"
    url = urllib.urlopen(urlSearch)
    soup = BeautifulSoup(url.read())
    img_urls = []
    for r in soup.findAll('a'):
        img_urls.append("http://www.mymp3singer.com/"+r.get('href'))
    if not img_urls:
        print "Sorry no result found for keyword "+artist
        return
    
    open = urllib.urlopen(img_urls[15])
    
    manchav_soup=BeautifulSoup(open.read())
    for x in manchav_soup.findAll('a',href=re.compile(r'.*get.*')):
        imgUrl = "http://www.mymp3singer.com"+x.get('href')
        try:
            imgData = urllib.urlopen(imgUrl)
            filename = x.get_text()
            print "Downloading mp3 song from "+imgUrl
            print "Please wait.."
            urllib.urlretrieve(imgUrl,filename)
            print filename+" is downloaded in "+dir
            
            break
        except:
            print "error"
        
        
artistSearch("atif")
