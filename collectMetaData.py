# -*- coding: utf-8 -*-
"""
CollectMetaData.py
Python 3.6.4 64 bit
Created on Thu Aug 13 21:58:46 2020

@author: Mary Koone  
for Style Clusters Project
U of TX Arlington
"""
import os
import datetime
import pandas as pd

#=========================
#put directory containing csv files to examine here
targetDir = 'C:\\Users\\Mary\\Documents\\Uta\\NLP\\AWSreviews\\multis'
#=========================
os.chdir(targetDir)

#makes list of everything in directory
fileNames = os.listdir()

#removes everything that is not csv
fileNames = [file for file in fileNames if file[-4:] == ".csv"]
  
#count how many customers
qtyFiles = len(fileNames)
writeMe = 'number of files = ' + str(qtyFiles) + '\n'
print(writeMe)

headers = ['cID', 'noReviews', 'fileSize', 'dateOfFirst', 'over#days', 'numCategories', 'avRating']
meta = pd.DataFrame(columns = headers)

for file in fileNames:
    #collect items of interest
    cID = file[:-4]
    #read file into dataFrame
    df = pd.read_csv(file)
    
    noReviews = len(df) - 1
    fileSize = os.stat(file).st_size
    #########df['review_date'] gives the column with 'review_date' header
    dateLate = df['review_date'].max()
   
    #----------------------
    [year, month, day] = str(df['review_date'].min()).split(sep = '-')
    dateEarly = datetime.date(int(year), int(month), int(day))
    #########
    noDays = int((dateLate-dateEarly).total_seconds()/60/60/24)
    noWeeks = int(noDays)/7
    noYears = int(noDays)/365
    noCategories = len(df['product_category'].unique())
    avRating = df['star_rating'].mean()
    row = [cID, noReviews, fileSize, dateEarly, noDays, noCategories, avRating]
    new = pd.DataFrame([row], columns = headers)
    meta = meta.append(new)
    
meta.to_csv('multis.csv')


    