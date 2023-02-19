


print("Enter seconds")
totalSeconds = int(input())
if(totalSeconds < 60):
    seconds = totalSeconds 
    mins = 0 
    hours = 0 
    days = 0
else:
    mins = 0
    while(totalSeconds>=60):
        totalSeconds = totalSeconds - 60
        mins = mins + 1 
    seconds = totalSeconds 
    hours = 0
    while(mins>=60):
        mins = mins - 60
        hours = hours + 1
    days = 0
    while(hours>=24):
        hours = hours - 24
        days = days + 1

print("days " + str(days))
print("Hours " + str(hours))
print("Mins " + str(mins))
print("seconds " + str(seconds))
    



    







    

