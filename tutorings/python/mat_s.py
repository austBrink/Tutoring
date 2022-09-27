
myFile = open("nums.txt","r")
file = myFile.read()
myList = file.split()


# convert each item in list to integer so we can do our maths. 
for i in range(0,len(myList)):
   myList[i] = int(myList[i])

max = myList[0]

for x in range(0,len(myList)):
   if(myList[x] > max):
      max = myList[x]

sum = 0

for x in range(0,len(myList)):
   sum = sum + myList[x]


mySet = set(myList)

#start the displaying....

print("The elements in the set are:")
for item in mySet:
   print(item)


print("Maximum value is... " + "${:,.2f}".format((max)))

print("The sum is...." +"${:,.2f}".format((sum)) )












