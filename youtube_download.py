# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 09:01:29 2018
##  https://github.com/nficano/pytube
@author: Jingdong
"""
def singlelinkdownload(url,directory='./'):      
    from pytube import YouTube
    yt = YouTube(url)
    #length_min=int(yt.length)/60
    #title = yt.title
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(directory)
    
def Playlistdownload(url,directory='./'):         
    from pytube import Playlist
    pl = Playlist(url)
    #pl.download_all()   
    # or if you want to download in a specific directory
    pl.download_all(directory)

def Playlist_gettitle(url,directory='./'):         
    from pytube import Playlist
    from pytube import YouTube
    import pandas as pd
    pl = Playlist(url)
    #pl.download_all()   
    # or if you want to download in a specific directory
    title_list=pd.DataFrame(columns=['url','title','length_min'])
    for url in set(pl.video_urls):
        yt = YouTube(url)  
        title=yt.title
        length_min=int(yt.length)/60
        title_list = title_list.append({'url': url,'title':title,'length_min':length_min},ignore_index=True)
  


import os 
os.chdir(r'D:\Downloads\movie')
url='https://www.youtube.com/watch?v=bFqbNXeNvPw&t=4959s' 
singlelinkdownload(url)

directory = r'E:\coursera\Applied Data Science with Python Specialization\Applied-Text-Mining-in-Python\Vedios\Natural Language Processing_Coursera'

url="https://www.youtube.com/watch?v=n25JjoixM3I&list=PLLssT5z_DsK8BdawOVCCaTCO99Ya58ryR"
Playlistdownload(url,directory)




directory = r'D:\Downloads\02如懿傳'
url="https://m.youtube.com/playlist?list=PLtHz1oM_BGWKCufXvPJSWovEqiXJEqkY_"
Playlistdownload(url,directory)

directory = r'D:\Downloads\01甄嬛传'
url="https://m.youtube.com/playlist?list=PL4U9STbe5zoLx3_OPdyOGLNyQwStxEAov"
Playlistdownload(url,directory)



import urllib
import requests
from bs4 import BeautifulSoup

textToSearch = "Ruyi's Royal Love in the Palace"
textToSearch = "Royal Love in the Palace"
query = urllib.request.quote(textToSearch)
url = "https://www.youtube.com/results?search_query=" + query


def getHTMLText(url):
    try:
        r=requests.get(url,timeout=300)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r
    except:
        print("产生异常")
        return "产生异常"
html = getHTMLText(url)
soup = BeautifulSoup(html.text, 'lxml')
for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
    print( 'https://www.youtube.com' + vid['href'])
    
for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
    print(vid['href'])
    print(vid['title'])
  
for vid in soup.findAll(attrs={'class':'yt-uix-button vve-check yt-uix-sessionlink yt-uix-button-default yt-uix-button-size-default'}):
    print(vid['href'])
    print(vid['aria-label'])


