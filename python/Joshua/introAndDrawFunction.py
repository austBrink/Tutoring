
# create a draw function. THat takes symbol and number as params and prints to the screen the symbol "n" number of times. 
def draw (symbol, number):
    temp = ''
    for i in range (0, number):
        temp = temp + symbol
    print(temp)

# show volume of a cylinder...
# h*r 
# showVolume
def showVolume (height, radius):
    print(height * radius)

number = int(input())
if (number < 10):
    if(number > 5):
        print('your number is between 5 and 10')
    elif(number < 5):
        print('your number is smaller than 5')
    else:
        print('your number is 5!')
elif (number > 10):
    if (number < 20):
        print('your number is between 10 and 20')
    elif (number > 20):
        print('your number is bigger than 20')
    else: 
        print('your number is 20')
else:
    print ('the number is 10')  
    
# a look at while loops...
# while loop will run as long as it's condition is true...
userInput = input()
while(userInput != "1"):
    print("not one")
    userInput = input()

# envoke or call the draw function ... 
# let's suppose I want to print
# draw('*', 5)
# draw('.',10)
# # print a test.  
# showVolume(5,2)
