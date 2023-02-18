 
# Things to note. look up how to print python in currancy format. 

import math

dataSource = open('brewster.dat','r')
lines = []
salesPerson = []
price = []


# getting our data sorted. Want a list for each column. store lines row into a list first. then store the first adn second values as the columns. These will be parallel arrays. for example item 0 in salesPerson corresponds to item 0 in price. 

for line in dataSource:
    lines = line.split(' ')
    salesPerson.append(lines[0])
    price.append(lines[1])


# need to get rid of that pesky \n character at the end of each item for price values. can't convert into floats until I do. 
for i in price:
    j = i.rstrip('\n')
    index = price.index(i)
    price[index] = j 


#changing the types from strings to something we can do math on. Looping through each string and casting. 
for item in salesPerson:
    numberValue = int(item)
    index = salesPerson.index(item)
    salesPerson[index] = numberValue 

#see previous comment 
for item in price:
    numberValue = float(item)
    index = price.index(item)
    price[index] = numberValue


personOne = 0
for i in price:
    index = price.index(i)
    if (salesPerson[index]== 100):
        personOne = personOne + i 
#print(personOne)

personTwo = 0
for i in price:
    index = price.index(i)
    if (salesPerson[index]== 101):
        personTwo = personTwo + i 
#print(personTwo)

personThree = 0
for i in price:
    index = price.index(i)
    if (salesPerson[index]== 102):
        personThree = personThree + i 


total = personOne + personTwo + personThree

print("title")
print()
print("Salesperson ID          Sale Amount")
print("===================================")
count = 1 
for i in range(0,len(price)):
    print(str(salesPerson[i]) + "                       " + "${:.2f}".format(price[i]))

    if(count == 3):
        print("Total Sales for this Salesperson: " + "${:.2f}".format(personOne))
    if(count== 6):
        print("Total Sales for this Salesperson: " + "${:.2f}".format(personTwo))
    if(count== 9):
        print("Total Sales for this Salesperson: " + "${:.2f}".format(personThree))

    count = count + 1 

print("Total of all price: " + "${:.2f}".format(total))

     
    