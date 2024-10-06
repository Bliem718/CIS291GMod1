#Imports the csv module.
import csv

#The try statement runs; if an error is encountered while running, the program goes to the except statement.
try:

#Opens presidentOutput.txt with write permissions and presidential.csv with read permissions.
    with open('presidentOutput.txt', 'w') as outputFile:
        with open('presidential.csv', 'r') as presidentialList:

#Reads the presidentialList file and puts the CSV data into a dictionary list.
            presidentInfo = csv.DictReader(presidentialList, delimiter=',')

#Creates lists holding the parties of each president that have not served full term.
            notFullTermDem = []
            notFullTermRep = []

#For each president in the presidentInfo dictionary, if start or end date is not 1/20, adds the name of the president to their respecctive party list.
            for row in presidentInfo:

                if row['start'][:4] != '1/20' or row['end'][:4] != '1/20':
                    if row['party'] == 'Democratic':
                        notFullTermDem.append(row['name'])
                    elif row['party'] == 'Republican':
                        notFullTermRep.append(row['name'])

#Writes to presidentOutput.txt  about the names of the Democratic presidents who did not serve full term.
            outputFile.write('Democratic Presidents:')
            for i in notFullTermDem:
                outputFile.write('\n' + i + ' did not serve at all full terms.')

#Creates two extra newlines.
            outputFile.write('\n' + '\n')

#Writes to presidentOutput.txt  about the names of the Republican presidents who did not serve full term.
            outputFile.write('Republican Presidents:')
            for i in notFullTermRep:
                outputFile.write('\n' + i + ' did not serve at all full terms.')

#Tells the user that the data has been transfered into presidentOutput.txt.
            print('Data from presidential.csv successfully outputted into presidentOutput.txt.')

#If an error occurs while running the program, tells the user that there was an error.
except Exception:
    print('There was an error opening the necessary files. Program will be terminated.')