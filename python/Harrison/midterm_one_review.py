# ITEM ONE 
# print('Please enter all the following fields...')
# name = input('Name: ')
# address = input('Address: ')
# city = input('City: ')
# state = input('State: ')
# zip = input('Postal: ')
# telNum = input('Telephone: ')
# email = input('Email: ')

# ITEM TWO 
# usersNumber = 0
# userNumbers = []
# while(usersNumber > -1):
#     usersNumber = int(input('Number: '))
#     if(usersNumber > 0):
#         userNumbers.append(usersNumber)
# # by the time we are out of the while block we will have a list of numbers to add up.
# sum = 0
# for i in range(0,len(userNumbers)):
#     sum = sum + userNumbers[i]
# print(f'The sum of the numbers you entered is {sum}')

# ITEM THREE 
# initialCharge = float(input('Please enter the food charge: '))
# TIP_PERCENTAGE = .18
# SALES_TAX_PERCENTAGE = .07

# tipAmount = .18 * initialCharge
# salesTaxAmount = .07 * initialCharge

# total = initialCharge + tipAmount + salesTaxAmount

# print(f'The food charge was {initialCharge}')
# print(f'The tip came to {tipAmount}')
# print(f'the sales tax was {salesTaxAmount}')
# print(f'the grand total is {total}')

# CALORIES_BURNED_PER_MINUTE = 4.2
# stopValues = [10,15,20,25,30]
# for x in range(0,len(stopValues)):
#     print(f'{stopValues[x]} MINS: You have burned {stopValues[x]*CALORIES_BURNED_PER_MINUTE} calories')

# loop and ask the user to enter test scores do this five times and push to an array / list 
# loop through array and call the calc_average function AND the determine grade function 
# print these results 

# write my functions
def get_average(a,b,c,d,e):
    return (a+b+c+d+e) / 5

def determine_grade(testScore):
    if(testScore >= 90 and testScore < 100):
        return 'A'
    elif(testScore >= 80 and testScore < 90):
        return 'B'
    elif(testScore >= 70 and testScore < 80):
        return 'C'
    elif(testScore >= 60 and testScore < 70):
        return 'D'
    elif(testScore < 60):
        return 'F'
    else:
        return 'N/A'
    
testScores = []
for i in range(0, 5):
    testScores.append(
        float(input("Test Score: "))
    )
for x in range(0, len(testScores)):
    currentScore = testScores[x]
    print(f'{x + 1}) SCORE: {currentScore} GRADE: {determine_grade(currentScore)}')
average = get_average(
    testScores[0],
    testScores[1],
    testScores[2],
    testScores[3],
    testScores[4]
)
print(f'AVERAGE SCORE: {average} AVERAGE LETTER GRADE: {determine_grade(average)}')
