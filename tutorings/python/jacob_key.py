# Write a program that asks the user to enter a number of seconds and then prints
# the same amount of time in days, hours, minutes, and seconds.
# For example, 3667 seconds is equivalent to 0 days, 1 hour, 1 minute, and 7 seconds.
# End of instructions.
# Have the user enter a number of seconds.
seconds = int(input("Enter the number of seconds."))
# Calculate the minutes.
if seconds < 60:
    print (f'{seconds} seconds')
if seconds >=60 and seconds < 3600:
    minutes = seconds // 60
    minuteRemainder = seconds % 60
    print (f'{seconds} seconds are equal to: {minutes} minutes and {minuteRemainder} seconds')
if seconds >= 3600 and seconds < 86400:
    hours = seconds // 3600
    hoursremainder = seconds % 3600
    minutes = hoursremainder // 60
    minuteRemainder = hoursremainder % 60
    print (f'{seconds} seconds are equal to: {hours} hours {minutes} minutes and {minuteRemainder} seconds.')
if seconds >= 86400:
    days = seconds // 86400
    daysremainder = seconds % 86400
    hours = daysremainder // 3600
    hoursremainder = daysremainder % 3600
    minutes = hoursremainder // 60
    minuteRemainder = hoursremainder % 60
    print(f'{seconds} seconds are equal to: {days} days {hours} hours {minutes} minutes and {minuteRemainder} seconds.')