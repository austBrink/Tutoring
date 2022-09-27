myFile = open("words.txt","r")

file = myFile.read()

myList = file.split("/n")

print(myList)