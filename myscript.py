# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 12:31:19 2019

@author: Ashish.Dadwal
"""



import os


       
def CombCSV(srcDir,destCSV):
    with open(destCSV,'w',encoding='utf-8') as destFile:
        header=''
        for root,dirs,files in os.walk(srcDir):
            for f in files:
                if f.endswith(".csv"):
                    with open(os.path.join(root,f),'r',encoding='utf-8') as csvfile:
                        if header=='':
                            header=csvfile.readline()
                            destFile.write(header)
                        else:
                            csvfile.readline()
                        for line in csvfile:
                            destFile.write(line)          

CombCSV('D:/New folder (3)/all-news-articles-from-home-page-media-house/Nov2017/csvdataset','D:/TextricsReader/combined.csv')