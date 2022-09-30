#!/usr/bin/python

"""Split a large CSV file into chunks, 
each with their own copy of the header."""

import csv


def splitCSV( filename , rowcount=100000 ):

    # Header data must be retained for the whole script.
    header = []

    with open(filename , "r" , newline='') as headerfile:
        headerReader = csv.reader(headerfile)
        header = next(headerReader)
        #print(header)

    with open(filename , "r" , newline='') as bigFile:
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
                    tmpfilename = filename[:-4] + str(filenamecount) + ".csv"
                    with open(tmpfilename, 'w', newline='') as tmpcsv:
                        wrtr = csv.writer(tmpcsv)
                        wrtr.writerow(header)
                        wrtr.writerows(tmprows)
                    tmprows = []
                    count = 0
                    filenamecount = filenamecount + 1
        # Clean up remaining rows into a final file.
        tmpfilename = filename[:-4] + str(filenamecount) + ".csv"
        with open(tmpfilename , "w", newline='') as tmpcsv:
            wrtr = csv.writer(tmpcsv)
            wrtr.writerow(header)
            wrtr.writerows(tmprows)
