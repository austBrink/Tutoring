
#program to open a file, read numbers line by line and display the sum and average of the numbers (file contents)

#create a container for the numbers (each line)
import sys
from warnings import catch_warnings


numbersFromFile = []

#open a file, read in the file with numbers


try:
    myFile = open("text.txt","r")
    numbersFromFile = myFile.readlines()
except IOError as e:
    catch_warnings
    print('we ran into some trouble with opening the file')

#save lines into array with readlines()


#clean my array. Could include junk like spaces and newlines... 
for n in numbersFromFile:
    #for each item strip of newline and spaces proceeding and postceeding 
    n.strip()


#create a var to store sum. print the sum with message. 
sum = 0
isError = False
setSize = len(numbersFromFile)

for x in numbersFromFile:
    try:
        x = int(x)
        sum += x
    except ValueError as e:
        isError = True 
        setSize -= 1
          
if(isError):
    print("we ran into some junk in your file but added everything that we could.")


print("The sum of numbers in the data file is " + str(sum))

#now get a hold of the average... Take sum and divide by numebr of numbers in file. but number of numbers in file is just the length of the array. 
#only attemp to take average if the array is not null.... 
if(setSize>0):
    average = sum / setSize
else:
    average = 0

print("The average of the numbers in the data file is " + str(average))







    