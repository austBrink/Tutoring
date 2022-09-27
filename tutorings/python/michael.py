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

studentCount = 24
studentsPerCar = 4
#initialize at 0 for now
numberOfCars = 0

print("Please enter a number of Parents with cars: ")
# use python's input function to get user input...
numberOfCars = int(input())
print(numberOfCars)



# It would best to validate the user entry is a number...
if ( (numberOfCars*4) >= studentCount):
    print("All students have a ride.")
else:
    print("Some Students do not have a ride.")








