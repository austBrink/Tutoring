# # A Python 
# # this is a boolean 
# myVar = True
# isUser = False
# isReturning = False
# # comment
# # simple if statement

# if (isUser):
#     print("Welcome, user")
# elif (isUser and isReturning):
#     print("Welcome Back, User")
# elif (isUser == False and isReturning):
#     print("Welcome Back")
# else:
#     print("go away. Not Auth.")

# x = 2
# y = 1

# if ( (x + y == 3) or (x + y == 4) ):
#     print("Sum was 3 or 4")
# # else means IN ANY other case.
# else:
#     print("Sum was not 3 or 4")

# studentCount = 24
# studentsPerCar = 4
# #initialize at 0 for now
# numberOfCars = 0

# print("Please enter a number of Parents with cars: ")
# # use python's input function to get user input...
# numberOfCars = int(input())
# print(numberOfCars)



# # It would best to validate the user entry is a number...
# if ( (numberOfCars*4) >= studentCount):
#     print("All students have a ride.")
# else:
#     print("Some Students do not have a ride.")


# prompt the user for scores.
# need a variable for the count to know the loop run AND get average. 
# need a container for the grades. arrays / lists 
# condition for the letter grade 

userChoice = ''
grades = []
userChoice = float(input('Please enter at least one grade to start: '))
grades.append(userChoice)
userChoice = input('Enter Y for another score or any key to quit: ')
while(userChoice.lower() == 'y'):
    userChoice = float(input('Please enter another score: '))
    grades.append(userChoice)
    userChoice = input('Enter Y for another score or any key to quit: ')

# by the time this while loop is done we have a list/ array with an entry for each grade entered by the user. The length of that list is HOW MANY grades we have. 
# get the average.... The size of the array is len(array) 
# need a var to keep the sum.
sum = 0
for i in range(0, len(grades)):
    sum = sum + grades[i]

average = sum / len(grades)
print(f'Your score is {average}...')
letterGrade = ''
# get the letter grade. 
# (0,60] F 
# (60-70] D
# (70-80] C
# (80-90] B
# (90-100] A 
# time for if statements 
# I'm lazy and dont want to type so...
a = average
if(a < 60):
    letterGrade = 'F'
elif(a >= 60 and a < 70):
    letterGrade = 'D'
elif(a >= 70 and a < 80):
    letterGrade = 'C'
elif(a >= 80 and a < 90):
    letterGrade = 'B'
elif(a >= 90):
    letterGrade = 'A'

print(f'...For a letter grade of {letterGrade}')
print('Goodbye')







