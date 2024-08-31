# write a while loop that will prompt the user for a number 
# then multiple this number by 10 
# keep asking for new number while the product is less than 25 

product = 0
while(product < 25):
    # how to get user input from the terminal python... 
    userNumber = int(input("Enter a number: "))
    product = userNumber * 10
    if(product < 25):
        print(product)
    else:
        print("You've entered a number who's product is less than 25")
    0