print('Magic Dates: find out if your date is magic')
print('Please enter a month')
userMonth = int(input())
print('Please enter a day')
userDay = int(input())
print('enter the last two digits of your year')
userYear = int(input())

isMagicDate = userMonth * userDay == userYear

if(isMagicDate):
    print('This date is magic')
else:
    print('This date is not magic')
