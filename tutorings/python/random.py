#Assuming that everyone in the family eats 3 slices of pizza how many pizzas are required for a family of 4 for one meal? How many are the leftover slices?
# one. assume that each pizza has 8 slices....
slicesPerPerson = 3
familySize = 4
numberOfSlices = slicesPerPerson * familySize
#we need the number of pizzas. 8*x = num of slices 
pizzaNum = round(numberOfSlices/8)
pizzaslicesRemaining = numberOfSlices%8 
print("REQUIRED PIZZA NUMBER " + str(pizzaNum))
print("SLICES LEFT OVER " + str(pizzaslicesRemaining))

#that the grocery tax in this Alabama city is 8% calculate. and the amount of tax and total amount that you have to pay for $30 of groceries
huntsvilleTax = 0.08
groceries = 30
taxAmt = groceries * 0.08 
totalBill = taxAmt + groceries
print("City: Huntsville" + "\n" + "tax amount: " + str(huntsvilleTax) + "\n" + "groceries in dollars: " + str(groceries))
print("amount paid for tax: " + str(taxAmt))
print("total bill: " + str(totalBill))