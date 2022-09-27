# prompt the user to enter a shipping weight
print("Please enter a shipping weight: ")
# get input from user and save into shipWight var
shipWeight = input()
# convert input to float
shipWeight = float(shipWeight)

rate = 0.0
# weight less than or 2 pounds : rate = 1.50
if (shipWeight <= 2):
    rate = 1.50
elif (shipWeight > 2 and shipWeight <= 6):
    rate = 3.00
elif (shipWeight > 6 and shipWeight <= 10):
    rate = 4.00
else:
    rate = 4.75

totalShipCost = shipWeight * rate
print("For a weight of ")
print(shipWeight)
print("The rate is ")
print(rate)
print("So the total is weight times rate ")
print(totalShipCost)
