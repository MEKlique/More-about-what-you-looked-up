# -*- coding: utf-8 -*-
"""
Directory Ops

Created on Wed Jul 8 17:49:35 2020

@author: Mary Koone

A script to compare the create and last-modify time of files
It writes the filenames whose times are the same to a file.
Included are the commands needed to make this a batch file 
that will move the designated files to a subfolder. 

Final result is a separation by directory of the customers
whose reviews cover only one category as opposed to those
whose reviews cover multiple categories.

"""
#open existing files
createTimes = open('createTimes.txt', 'r')
lastChange = open('lastWriteTime.txt', 'r')
#create destination file
moveMe = open('moveMe.bat', 'w')
#read first line of each file and compare
#note that we expect the exact same number of lines in each file.
#no checking since this is down and dirty code
for line in createTimes:
    change = lastChange.readline()
    if (line!=change):
        current = line.split(' ')[-1].splitlines()[0]
        line2write = 'move ' + current + r" multiCat\c" +  current[1:] + '\n'
        moveMe.write(line2write)

#close all open files
createTimes.close()
lastChange.close()
moveMe.close()

