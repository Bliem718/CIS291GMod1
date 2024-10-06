#This program is made by Bryan Liem. This program creates an output file by gathering two columns of data from another file
#and creates pop.txt, the file holding the countries and its population by ddescending order.

#Imports module csv, whicch is needed for this program.
import csv

#The try statement runs; if an error is encountered while running, the program goes to the except statement.
try:

#Opens pop.txt' with write permissions and UN.csv with read permissions.
    with open('pop.txt', 'w') as outputFile:
        with open('UN.csv', 'r') as dataFromUN:

#Reads the dataFromUN file and puts the CSV data into a list.
            countryInfo = csv.reader(dataFromUN, delimiter=',')

#Creates an empty list.
            countryList = []

#For every country in countryInfo, adds the population and the name of the country into countryList.
            for row in countryInfo:
                countryPop = [float(row[2]), row[0]]
                countryList.append(countryPop)

#Sorts the entities in countryList in reverse order, higher populated countries are listed higher.
            countryList.sort(reverse=True)

#Writes to pop.txt the "Population" and "Country" headings for the list. F string format is used here to format the placement of the headings.
            outputFile.write(f'{"Population"}{"Country":>37}\n')

#Writes to pop.txt the country data from countryList. F string format is used here to format the placement of the data.
            for country in countryList:
                outputFile.write(f'{country[0]:<7.2f}M{country[1]:>39}\n')

#Tells the user that the data has been written onto pop.txt.
            print('pop.txt has been created with countries by descending order of population.')

#If an error occurs while running the program, tells the user that there was an error.
except Exception:
    print('There was an error in opening, reading, or writing one of the files. Program will terminate.')