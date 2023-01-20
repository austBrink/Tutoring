import math
# These were given with the problem 
NUMBER_OF_SLICES_IN_PIZZA = 8 
FAMILY_SIZE = 4

# prompt the user for what we need 
print('How many slices do each of y\'all eat?')
slicesPerPerson = int(input())

# initializing a variable 
numberOfPizzas = 0 
remainingSlices = 0

# How many pizza I need 
# I am now able to get the slices needed because the family told me how many they each eat. 
slicesNeeded = slicesPerPerson * FAMILY_SIZE

# Division to get number of pizza
numberOfPizzas = math.ceil(slicesNeeded / NUMBER_OF_SLICES_IN_PIZZA)
# Get the remainder based on the modulus operator % 
remainingSlices = slicesNeeded % NUMBER_OF_SLICES_IN_PIZZA

print('Number of pizzas ' + str(numberOfPizzas))

print('Remaining Slices ' + str(remainingSlices))