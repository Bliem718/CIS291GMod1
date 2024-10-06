#Imports the necessary modules (random)
import random

#Defines the main function of the exercise with variable N as a parameter.
def createNumberFile(N):

#Tries to check if N is an integer.
    try:
        int(N)

#If N is not an integer, then this exception runs and ends the function.
    except ValueError:
        print(N + " is not an integer. Please input an integer next time.")

#If N is an integer,
    else:

#If N is 0 or less, then prompts the user to input a positive integer, which is used for this function again.
        if int(N) <= 0:
            N = input(N + " is not a positive integer. Input a positive number: ")
            createNumberFile(N)

#If N is a positive integer,
        else:

#Prompts the user to give a name for a new .txt file.
            fileName = str(input("Please give a name for an output file: "))

#Tries to check fileName can be accessed.
            try:

#Sets variable newFile to open fileName with writing supported.
                newFile = open(fileName, "w")

#Defines variable i for use in the while loop.
                i = 0

#The loop writes a random number between 1 and 100 with a newline for every number, which loops over N amount of times.
                while i < int(N):
                    newFile.write(str(random.randrange(1, 100)) + "\n" )
                    i += 1

#Tells the user that the file has been created/changed with N numbers.
                print(fileName + ".txt has been created/changed with " + N + " random numbers.")

#If file cannot be accessed, then tells the user that the file cannot be accessed.
            except Exception:
                print(fileName + ".txt cannot be accessed.")

#Prompts the user to input a number, which is used in the below function.
N = input("Input a positive number: ")
createNumberFile(N)
