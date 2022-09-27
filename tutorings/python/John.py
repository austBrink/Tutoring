# This is the template for creating your Python programs. You must use this template.
#
# Program Developer Name:  your name here
#
# Date Program Developed:  current date here
#
#Version: the current version number here
#
# Organization: CIS 202 - 302
############
#
# Replace this line with a description of the problem as it is stated (as close as possible given text characteristics)
#
###########
#
# Document your inputs below this line
#
# Insert your lists of inputs here
#
###########
#
# Document your outputs below this line
#
# Insert your list of outputs here
#
###########
#
# Document your processes below this line
#
# Insrt your list of processes here
#
############
#
# Start your program code after this line

# first things first get input from the user. 
# input is anything from the user.... 
print("Please enter an amount for the sale: ")
# now that we have prompted the user, get the user input. 
userEnteredSale = float(input())

# Now to set constants... 
stateTax = 0.05
countyTax = 0.025

#follow instructions on printing to the screen...
print("SALE AMOUNT: ")
print(userEnteredSale)
print("STATE SALES TAX ") 
print(stateTax*userEnteredSale)
print("COUNTY SALES TAX")
print(countyTax*userEnteredSale)
# I need to print total tax to screen. create a variable for that...
totalTax = (stateTax + countyTax)*userEnteredSale
print("TOTAL SALES TAX")
print(totalTax)
salesTotal = totalTax + userEnteredSale
print("THE SALE TOTAL WAS: ")
print(salesTotal)

#This is the end of the program
#################################

