
#creating dictionaries to relate keys and definitions to map classes to rooms, instructors, and times.... 

#plan: use data input to ask for definitions....


print("welcome to the class dictionary")

classLoc = {}
classTchr = {}
classTm = {}

classes = []

numOfClass = int(input("how many classes to store data for?"))

for i in range(0,numOfClass):
    userKey = input("Please enter a class")
    userRoom = input("please enter a room no")
    userProff = input("Please enter a professor")
    userTime = input("Please enter a time")

    classes.append(userKey) 

    classLoc[userKey] = userRoom
    classTchr[userKey] = userProff
    classTm[userKey] = userTime

print("Class      location       teacher        time ")
for i in range(0, len(classes)):
    

    print(str(classes[i]) + "            " + str(classLoc[classes[i]])  + "               " +  str(classTchr[classes[i]]) + "          " + str(classTm[classes[i]]))







        