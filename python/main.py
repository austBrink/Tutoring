
#read a txt file. display the sum of the numbers in that file. and the average. 

#create a file object and open the file path... 

numbersFromFile = []

myFile = open("fileA.txt","r")

numbersFromFile = myFile.readlines()


for line in numbersFromFile:
    print(line)