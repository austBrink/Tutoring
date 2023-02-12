# Write a program that uses ( nested loops ) to collect data and calculate the average rainfall over a period of two years. The outer loop will iterate once for each year. The inner loop will iterate twelve times, once for each month. Each iteration of the inner loop will ask the user for the inches of rainfall for that month. After all iterations, the program should display the number of months, the total inches of rainfall, and the average rainfall per month for the entire period.

# review loops 
NUMBER_OF_YEARS = 2
NUMBER_OF_MONTHS_IN_YEAR = 12
# array / list 
months = ["Jan","Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# containers or a structure 
totalRainFall = []

# run a loop for two years.. 
for i in range(0, NUMBER_OF_YEARS):
  print(f'DATA FOR YEAR {i + 1}')
  for j in range(0, NUMBER_OF_MONTHS_IN_YEAR):
    print(f'Enter the inches of rainfall for {months[j]}')
    tempRainfallAmount = float(input())
    totalRainFall.insert(len(totalRainFall),tempRainfallAmount)

totalMonths = NUMBER_OF_YEARS * NUMBER_OF_MONTHS_IN_YEAR

print(f'TOTAL NUMBER OF MONTHS: {totalMonths}')

rainfallTotal = 0
for n in range(0,len(totalRainFall)):
  rainfallTotal = rainfallTotal + totalRainFall[n]

print(f'THE TOTAL RAINFALL WAS {rainfallTotal}')

print(f'THE AVERAGE RAINFALL PER MONTH IS {rainfallTotal / totalMonths}')