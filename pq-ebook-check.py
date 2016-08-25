import urllib
from urllib import request
import codecs
import csv

urlFiles = 'pq.csv'
resultsLog = 'pqResults.txt'

def readURLList():
    """"read in the IDs, URLs"""

    uL = []
    with open(urlFiles, 'r') as x:
        reader = csv.reader(x)
        for row in reader:
            uL.append(row)

    return uL

def checkTitle(titleTitle, titleURL, debugMode):
    """go to the vendor's site and check that access and the title are present"""

    r = urllib.request.urlopen(titleURL)
    httpList = r.readlines()

    # extract the title ID from the URL after the "=" (equals) which will be used for validation
    accessID = titleURL[titleURL.find('=')+1:]
    accessString = 'href="reader.action?docID=' + str(accessID) + '">Available for Online Reading</a>'
    if debugMode == '1':
        print('accessID is: '+str(accessID))
        print('accessString is: ' + str(accessString))


    titleFound = False

    # check for the title in the source code - abbreviate the title at the first ":" (colon)
    titleSearch = titleTitle[:titleTitle.find(':')-1]

    for l in httpList:
        if titleSearch.upper() in l.decode().upper():
            titleFound = True
            if debugMode == '1':
                print('\tTitle, '+titleSearch+' is found!')
            continue

    # check for the id with the access string in the HTML of the page
    accessFound = False
    for t in httpList:
        if str(accessString) in str(t.decode(encoding='utf-8')):
            accessFound = True
            if debugMode == '1':
                print('\tAccess is found!')
            continue

    return (titleFound, accessFound)


def writeResults(resultString):
    """log the results"""
    with codecs.open(resultsLog, 'a', encoding='utf-8') as x:
        x.write(resultString+'\n')

def runCheck(debugMode=None):
    """runs the program - if the user enters the program with the debug mode = 1, they'll get feedback as it runs"""

    debugMode = str(debugMode)
    if debugMode == '1':
        print('running in debug mode!\n')
    else:
        print('running in regular mode!\n')
        # return

    checkList = readURLList()

    counter = 0
    for title in checkList:
        counter += 1
        if debugMode == '1':
            print('record #: '+str(counter))
        titleID = title[0]
        titleTitle = title[1]
        titleURL = title[2]

        result = checkTitle(titleTitle, titleURL, debugMode)

        resultString = str(titleID) + '\t' + str(titleTitle) + '\t' + str(titleURL) + '\t' + str(result[0]) + '\t' +\
                       str(result[1])

        writeResults(resultString)


        if debugMode == '1':
            cont = input('continue?')
            if cont == 'n':
                print((1/0))

# run the check when the program is instantiated without the debug mode
runCheck()