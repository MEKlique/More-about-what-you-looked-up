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
#wt tokenizes http as separate punctuation
#for html parsing   raw = BeautifulSoup(html, 'html.parser').get_text()
from bs4 import BeautifulSoup as bsp

#function takes text and returns 1 if HTML tokens are found, default 1
#check various getText functions in BeautifulSoup
#bsp.get_text() converts it's to it/'s...need to fix
#note that wt(text) returns html pieces as punctuation '<', 'br', '/', '>'
#function is not used in main

def hasHTTP(text):
    x = 1
    withHTTP = bsp(text, 'html.parser')
    justText = withHTTP.get_text()
    if (str(withHTTP) == justText): x = 0
    return x, withHTTP, justText

targetDir = 'C:\\Users\\Owner\\Documents\\'
os.chdir(targetDir)
#makes list of all filenames in directory
fileNames = os.listdir()

#removes everything that is not a csv named with a customer ID
fileNames = [file for file in fileNames if ((file[0:4] == "cust") and (file[-3:] == 'csv'))]

#make a list to put tokenized reviews into
Tokens = []

for file in fileNames:
    df = pd.read_csv(file)
    reviews = df['review_body']
    headlines = df['review_headline']
    
    qt = []
    vcb = []
    v_sz = []
    
    for review in reviews:
        tokens = wt(review)
        #qtyToks = len(tokens)
        #qt.append(qtyToks)
        vocab = sorted(set(tokens))
        vcb.append(vocab[0])
        vocab_size = len(vocab)
        v_sz.append(vocab_size)
        #put the qtyWords into a vector to store as a column in the customer csv file
        #make a new df with everything, including new columns and overwrite original
        #get qty letters, qtyPeriods (to approximate sentances)
    df['review_body_tokens'] = qt
    df['review_mostFrequentToken'] = vcb
    df['review_uniqWords'] = v_sz
    qt = []
    vcb = []
    v_sz = []
    
    for headline in headlines:
        tokens = wt(headline)
        qtyToks = len(tokens)
        qt.append(qtyToks)
        vocab = sorted(set(tokens))
        vcb.append(vocab[0])
        vocab_size = len(vocab)
        v_sz.append(vocab_size)
    df['hdr_body_tokens'] = qt
    df['hdr_mostFrequentToken'] = vcb
    df['hdr_uniqWords'] = v_sz
    
    
    df.to_csv(file)
'''
This cleans up csv files that have acquired extra index columns.

for file in fileNames:
    df = pd.read_csv(file)
    header = df.keys()
    removeMe = [name for name in header if (name[0:7] == 'Unnamed')]
    for name in removeMe: del df[name]
    df.to_csv(file)
    
'''
#calculate basic meta data
#tokenQty = len(singleCust)
#vocab = sorted(set(singleCust))
#vocab_size = len(vocab)

#calculate lexical diversity (set of words/total words)