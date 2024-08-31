import math

#part 1
def showMax(a, b, c):
    if (a > b and a > c):
        print(a)
    elif (b > a and b > c):
        print(b)
    elif(c > a and c > b):
        print(c)

alpha = int(input("Enter an integer: "))
beta = int(input("Enter another integer: "))
gamma = int(input("Enter the last integer: "))

showMax(alpha, beta, gamma)

#part 2
def showVolume(h, r):
    Volume = math.pi*r*2*h
    print(Volume)

radius = float(input("Enter the radius: "))
height = float(input("Enter the height: "))

showVolume(radius, height)

#part 3

def draw(ch,n):
    for i in range(0,n):
        print(ch) 

draw("*",8)


#part 4
def greet():
    print("Hello")
    print("Welcome to my script")

greet()

#part 5 
def showRatio(x,y):
    if (y == 0):
        print("division by zero is undefined")
    else:
        ratio = x / y
        print("the ratio is ... " + str(ratio))

numerator = 9
denominator = 3 
showRatio(numerator, denominator)
numerator = 9
denominator = 0 
showRatio(numerator, denominator)


#part 1

def maxVal(a, b):
    if(a>b):
        return a 
    else:
        return b

print(str(maxVal(6,9)))

#part 2
def sumVals(x, y, z):
    return x + y + z

first = int(input("Enter a number: "))
second = int(input("Enter another number: "))
third = int(input("Enter the last number: "))

total = sumVals(first, second, third)
print("The sum is", total)

#part 3 
def isNeg(n):
    if(n<0):
        return True
    else:
        return False

print(str(isNeg(8)))
print(str(isNeg(-8)))

#part 4 
def isUpper(ch):
    return ch.isupper()

value = isUpper("A")
if(value == True):
    print("Capital was found")
else:
    print("Lower Case was found")

#part 5
def amtDue(p, q):
    return p * q

price = int(input("Enter a number: "))
quantity = int(input("Enter another number: "))

total = amtDue(price, quantity)
print("The amount due is", total)

#part 6
def lowEquiv(ch):
    if ch >= 'A' and ch <= 'Z':
        return chr(ord(ch)-32)
    else:
        return ch

symbol = input("Enter a character: ")

print("The lower case equivalent is", lowEquiv(symbol))

