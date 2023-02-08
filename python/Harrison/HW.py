import math

SALES_TAX = 0.08
subtotal = 30
amountOfTaxes = SALES_TAX * subtotal 
total = subtotal + amountOfTaxes

print(total)

# problem 2 
SLICES_PER_PIZZA = 8 
FAMILY_SIZE = 4 
SLICES_PER_PERSON = 3 

totalSlices = FAMILY_SIZE * SLICES_PER_PERSON

# round to the nearest whole number 
numberOfPizzas =  math.ceil(totalSlices / SLICES_PER_PIZZA) 

# recipe
CUPS_OF_SUGAR = 1
CUPS_OF_FLOUR = 2
CUPS_OF_BUTTER = 1

TOTAL_COOKIES_RECIPE_MAKES = 48

# base unit recipe 
SUGAR_UNIT = CUPS_OF_SUGAR / TOTAL_COOKIES_RECIPE_MAKES
FLOUR_UNIT = CUPS_OF_FLOUR / TOTAL_COOKIES_RECIPE_MAKES
BUTTER_UNIT = CUPS_OF_BUTTER / TOTAL_COOKIES_RECIPE_MAKES

# get how many cookies to make from the user
print('ENTER THE NUMBER OF COOKIES')
userCookies = int(input())

# display the recipe for this number of cookies

print('CUPS OF SUGAR: ')
print(SUGAR_UNIT * userCookies)

print('CUPS OF FLOUR: ')
print(FLOUR_UNIT * userCookies)

print('CUPS OF BUTTER: ')
print(BUTTER_UNIT * userCookies)

