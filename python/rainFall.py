'''
Design a program that lets the user enter the total rainfall for each of 12 months into a list. The program should calculate and display the total rainfall for the year, the average monthly rainfall, the months with the highest and lowest amounts. (additional resources folder)
'''
def getMax (array):
    max = array[0]
    for i in range (0, len(array)):
        if(array[i] > max):
            max = array[i]
    return max

def getMin(array):
    min = array[0]
    for i in range (0, len(array)):
        if(array[i] < min):
            min = array[i]
    return min


# get user data for the 12 months.
# need someplace to store that data... means a list 
rainFall = []
# make a list for our months 
months = ["Jan","Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

for i in range (0, len(months)):
    temp = float(input(f'Please enter the rainfall for: {months[i]}'))
    rainFall.insert(i,temp);

print(rainFall)

print(getMax(rainFall))
print(getMin(rainFall))




