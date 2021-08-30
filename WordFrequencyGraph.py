# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 14:47:36 2020
For the purpose of experimenting with NLTK
@author: Mary E. Koone, PhD student, University of Texas at Arlington

citation for code that uses NLTK:
Bird, Steven, Edward Loper and Ewan Klein (2009), 
Natural Language Processing with Python. 
O’Reilly Media Inc.
"""
import nltk, re, pprint
import os
import pandas as pd
from nltk import word_tokenize as wt

targetDir = 'C:\\Users\\Owner\\Documents'
os.chdir(targetDir)
#makes list of everything in directory
fileNames = os.listdir()
#makes a list of all filenames in directory
#removes everything that is not a csv named with a customer ID
fileNames = [file for file in fileNames if ((file[0:4] == "cust") and (file[-3:] == 'csv'))]
#make a list to put tokenized reviews into
Tokens = []

for file in fileNames:
    df = pd.read_csv(file)
    reviews = df['review_body']
    headlines = df['review_headline']
    for review in reviews: 
        tokens = wt(review)
        for token in tokens: Tokens.append(token)
    for review in headlines: 
        tokens = wt(review)
        for token in tokens: Tokens.append(token)
#get frequency distrubution of tokens
fdist = nltk.FreqDist(Tokens)
fdist.plot(100)
vocab = fdist.keys()
#words that appear only once
uniq = fdist.hapaxes()

