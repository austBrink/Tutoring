'''
Use a main function that calls 2 functions, one for getting user input and the other for printing the output. Whether you pass values or create void or value returning functions or global variables is up to you. 

In the inputGet function write a while loop that asks the user to enter two numbers num1 and num2. The numbers should be added and the sum displayed. Make sure that num1 is not negative and num2 is not negative. 

The loop should ask the user if he or she wishes to perform the operation again. If so, the loop should repeat, otherwise it should terminate. 

'''

def display(printMe):
    print(printMe)

def getSum(x,y):
    return x + y

def inputGet():
    active = True
    isNegative = True
    while(active and isNegative):
        #get number 1 and 2...
        num1 = int(input("please enter a value for number one "))
        num2 = int(input("please enter a value for number two "))

        if(num1 < 0 or num2 < 0):
            print("Please enter positive values for numbers one and two...")
            continue
        else:
            isNegative = False
            display(str("Your numbers add up to... ") + str(getSum(num1,num2)))

        userChoice = input("Do you want to add some numbers again? Y/N \n").upper().strip()
        
        if(userChoice == 'N'):
            active = False
            print("see ya")
        else:
            isNegative = True


def main():
    inputGet()
    
main()