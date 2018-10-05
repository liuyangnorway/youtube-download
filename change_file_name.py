# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 13:02:50 2018

@author: Jingdong
"""

import os
path = r'D:\Downloads\Download_5KPlayer\Neural Networks and Deep Learning'
os.chdir(path)

for file in os.listdir(path):
     if os.path.isfile(os.path.join(path,file))==True:
         list =file.replace(')','(').split('(')
         if len(list)==3:
             file_new_name='{}_{}{}'.format(list[1].strip(),list[0].strip(),list[2])     
             os.rename(os.path.join(path,file),os.path.join(path,file_new_name))
             print( file,'ok') 
     
        