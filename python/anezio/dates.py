## march 13, 2022

months = ["Jan" ,"Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

userString = input('enter a date as mm/dd/yyyy: ')

dateItems = userString.split('/')

print(dateItems)

monthAsNumber = int(dateItems[0])

print(monthAsNumber)

monthAsString = months[monthAsNumber - 1]

print(monthAsString)

print(f'{monthAsString} {dateItems[1]}, {dateItems[2]}')
