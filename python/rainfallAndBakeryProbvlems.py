# # functions

# # global variable

# def printANumber():
#   myNumber = 5
#   print(myNumber)


def printArray(anyArray):
    for i in range(0, len(anyArray)):
        print(anyArray[i])


# def getArrayMin (anArray):
#   min = anArray[0]
#   for i in range(0,len(anArray)):
#     if(min > anArray[i]):
#       min = anArray[i]
#   return min

# def getArrayMax (anArray):
#   max = anArray[0]
#   for i in range(0,len(anArray)):
#     if(max < anArray[i]):
#       max = anArray[i]
#   return max

# def sum (x,y):
#   return x+y

# printANumber()
# print(myNumber)

# code begins
# studentGradesMay = [60, 70, 90, 34, 78]
# studentGradesJun = [90, 50, 90, 78]
# studentGradesJul = [62, 90, 100, 78]

# print(getArrayMin(studentGradesMay))
# print(getArrayMin(studentGradesJun))
# print(getArrayMin(studentGradesJul))

# print(getArrayMax(studentGradesMay))
# print(getArrayMax(studentGradesJun))
# print(getArrayMax(studentGradesJul))

# print(sum(1,2))

# printArray(studentGradesMay)
# print("===================")
# printArray(studentGradesJun)

# Write a program that uses nested loops to collect data and calculate the average rainfall over a period of two years. The outer loop will iterate once for each year. The inner loop will iterate twelve times, once for each month. Each iteration of the inner loop will ask the user for the inches of rainfall for that month. After all iterations, the program should display the number of months, the total inches of rainfall, and the average rainfall per month for the entire period.

# rainYearOne = [0] * 12
# rainYearTwo = [0] * 12

# for year in range(1, 3):
#     print("year " + str(year))
#     for month in range(1, 13):
#         rainFall = int(input("Enter the rainfall for the month of " + str(month) + ": "))
#         if (year == 1):
#           rainYearOne[month-1] = rainFall
#         elif (year == 2):
#           rainYearTwo[month-1] = rainFall

# total = [*rainYearOne , *rainYearTwo]

# print(len(total))

# totalRainfall = 0

# for month in range(0,24):
#   totalRainfall = totalRainfall + total[month]

# rainAveragePerMonth = totalRainfall / 24;
# print(total)
# print("Number of Months: 24")
# print("Total Rainfall: " + str(totalRainfall))
# print("Average per month: " + str(rainAveragePerMonth))

print("WELCOME TO THE BAKERY")

muffins = 10
cupcakes = 10

print("Enter 0 to list inventory, Enter 1 for sale, enter 2 to quit ")
userChoice = int(input("Enter a choice: "))
while (userChoice != 2):
    if (userChoice == 0):
        print("Cupcakes: " + str(cupcakes))
        print("Muffins: " + str(muffins))
    if (userChoice == 1):
        userChoice2 = input(
            "Do you want a cupcake or a muffin? Enter cupcake or muffin: "
        ).lower()
        if (userChoice2 == "muffin"):
            muffins = muffins - 1
        elif (userChoice2 == "cupcake"):
            cupcakes = cupcakes - 1
    print("Enter 0 to list inventory, Enter 1 for sale, enter 2 to quit ")
    userChoice = int(input("Enter a choice: "))
print("Goodbye User")
