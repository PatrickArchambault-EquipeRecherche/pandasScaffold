#!/usr/bin/python

"""Split a large CSV file into chunks, 
each with their own copy of the header."""

import csv
from os import read

# Header data must be retained for the whole script.
header = []

with open("lab_data.csv" , "r" , newline='') as headerfile:
    headerReader = csv.reader(headerfile)
    header = next(headerReader)
    #print(header)

with open("lab_data.csv" , "r" , newline='') as bigFile:
    looper = csv.reader(bigFile)

    count = 0
    filenamecount = 1
    tmprows = []
    for row in looper:
        if row != header:
            tmprows.append(row)
            count = count + 1
            if count == 100000:
                #print(count)
                tmpfilename = "lab_data_" + str(filenamecount) + ".csv"
                with open(tmpfilename, 'w', newline='') as tmpcsv:
                    wrtr = csv.writer(tmpcsv)
                    wrtr.writerow(header)
                    wrtr.writerows(tmprows)
                tmprows = []
                count = 0
                filenamecount = filenamecount + 1
    # Clean up remaining rows into a final file.
    tmpfilename = "lab_data_" + str(filenamecount) + ".csv"
    with open(tmpfilename , "w", newline='') as tmpcsv:
        wrtr = csv.writer(tmpcsv)
        wrtr.writerow(header)
        wrtr.writerows(tmprows)
