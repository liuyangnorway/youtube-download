# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 20:47:41 2018

@author: Jingdong
"""
#

from moviepy.editor import VideoFileClip
import os
import pandas as pd
#import video_length
# from video_length import search


path=r'E:\coursera\Deep Learning Specialization\C1_Neural Networks and Deep Learning\Video'
word='.mp4'

def search(path, word):
    filelist=[]
    for filename in os.listdir(path):
        fp = os.path.join(path, filename)
        if os.path.isfile(fp) and word in filename:
            filelist.append(filename)
        elif os.path.isdir(fp):
            search(fp, word)
    return filelist        

def search2(path, endword):
    filelist=[]
    for filename in os.listdir(path):
        fp = os.path.join(path, filename)
        if os.path.isfile(fp) and fp.endswith(word):
            filelist.append(fp)
    return filelist

def search3(path, endword):
    filelist=[]
    for filename in os.listdir(path):
        fp = os.path.join(path, filename)
        if os.path.isfile(fp) and fp.endswith(word):
            filelist.append(filename)
    return filelist

path=r'E:\coursera\Deep Learning Specialization\C1_Neural Networks and Deep Learning\Video'
word='.mp4'

T=[]
T2=[]
for  filename in search3(path, word):
    try:
        with VideoFileClip(filename) as clip:
            #clip = VideoFileClip(filename)
            duration_in_sec = clip.duration
            T.append(float("{0:.2f}".format(duration_in_sec/60)))
            T2.append('{0:.2f}:{1:.2f}'.format(duration_in_sec//60,duration_in_sec%60))
            
    except:
        print('产生异常:{}'.format(filename))

T=[]
T2=[]

path=r'E:\coursera\Deep Learning Specialization\C1_Neural Networks and Deep Learning\Video'
word='C1W'

def find_video_length(path, word):
    T=[]
    T2=[]
    Files=[]
    for  filename in search(path, word):
        try:
            with VideoFileClip(filename) as clip:                
                #clip = VideoFileClip(filename)
                duration_in_sec = clip.duration
                T.append(float("{0:.2f}".format(duration_in_sec/60)))
                T2.append('{0:.0f}:{1:.2f}'.format(duration_in_sec//60,duration_in_sec%60))
                Files.append(filename)                          
        except:
            print('产生异常:{}'.format(filename))

    df = pd.DataFrame(Files,columns=['FileName'])
    df['Title']=df['FileName'].apply(lambda x: x[0:7])
    df['Length(sec)']=T
    df['Length']=T2
    df.set_index('Title',inplace=True)
    return df


df=find_video_length(path, 'C1W1')
l1=float("{0:.2f}".format(df['Length(sec)'].sum()))
df=find_video_length(path, 'C1W2')
l2=float("{0:.2f}".format(df['Length(sec)'].sum()))
df=find_video_length(path, 'C1W3')
l3=float("{0:.2f}".format(df['Length(sec)'].sum()))
df=find_video_length(path, 'C1W4')
l4=float("{0:.2f}".format(df['Length(sec)'].sum()))
df=find_video_length(path, 'C1W')
l=float("{0:.2f}".format(df['Length(sec)'].sum()))
[l1,l2,l3,l4,l]
    
