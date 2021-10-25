#What to look for:
#DEVICE_NUMBER, SAMPLE_DATE_TIMESTAMP, BATTERY, BATTERY_STATE

import sys
import os
import csv
import datetime

BATTERY_FILE_NAME = "battery_data.csv"
data = []

def parseHPNFileString(csvFile):
    global data
    csvFile = open(csvFile, "r")
    for row in csvFile:
        #print(row)
        rowArray = row.split(",")
        if (rowArray[0] == "DEVICE_NUMBER"):
            continue;

        if(len(rowArray) == 22):
            if((rowArray[10] != "") and (rowArray[11] != "")):
                data.append([("%s,%s,%s,%s" %
                    (rowArray[0].strip(), rowArray[1].strip(),
                     rowArray[10].strip(), rowArray[11].strip()))])

    csvFile.close()

def parseDirectory(directory):
    #get all the files in the directory
    #check that the file is a .csv file
    #then once you have a file, you can parse contents
    #and put contents in a master array to write later OR
    #write the line to an opened csv file

    for root, dirs, files in os.walk(directory):
        for file in files:
            #print("file name is: %s" % file)
            if (file.endswith('.csv')):
                csvFile = os.path.join(root, file)
                parseHPNFileString(csvFile)

def parseWriter():
    csvFile = open(BATTERY_FILE_NAME, 'w')
    writer = csv.writer(csvFile)
    writer.writerow(("DEVICE_NUMBER", "SAMPLE_DATE_TIMESTAMP", "BATTERY", "BATTERY_STATE"))
    #print(len(data))
    writer.writerows(data)

    csvFile.close()

def main(argv):

    #require an argument input for a directory
    if (len(sys.argv) != 2):
        print("%s <directory to parse>" % sys.argv[0])
        print("")
        print("Example: \npython3 battery_data.py /home/connorb/For_Connor/")
        sys.exit()

    #we now have a dirctory where all HPN .csv files are located
    directory = sys.argv[1]

    if(os.path.isdir(directory) == False):
       sys.exit()

    parseDirectory(directory)
    parseWriter()

    batteryResults = os.getcwd() + "/" + BATTERY_FILE_NAME;
    print("Wrote results to: %s" % batteryResults);

if __name__ == '__main__':
    main(sys.argv)
