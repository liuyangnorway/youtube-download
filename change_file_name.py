# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 13:02:50 2018

@author: Jingdong
"""

import os
import time

path = r'D:\Downloads\Download_5KPlayer\Neural Networks and Deep Learning'
os.chdir(path)

for file in os.listdir(path):
     if os.path.isfile(os.path.join(path,file))==True:
         list =file.replace(')','(').split('(')
         if len(list)==3:
             file_new_name='{}_{}{}'.format(list[1].strip(),list[0].strip(),list[2])     
             os.rename(os.path.join(path,file),os.path.join(path,file_new_name))
             print( file,'ok') 
     


def findfile(root, keywords):
    for fileDir, dirs, files in os.walk(root):
        for file in files:
            if keywords in file:
                full_path = os.path.join(fileDir, file)
                #print(os.path.normpath(os.path.abspath(full_path)))
                mtime = os.path.getmtime(full_path)
                datetime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(mtime))
                print('{0}  {1}'.format(os.path.normpath(os.path.abspath(full_path)),datetime))



root="E:" + os.sep+ "datacamp" + os.sep+ "find_finn"+ os.sep+"old"
keywords= "fileA"
findfile(root, keywords)

fileDir="E:" + os.sep+ "datacamp" + os.sep+ "find_finn"
keywords= "url_dict_new"
findfile(fileDir, keywords)

files=os.listdir(fileDir)
for file in files:
    if keywords in file:
        full_path = os.path.join(fileDir, file)
        print(os.path.normpath(os.path.abspath(full_path)))
        