

fileName = "brewster.dat"
fileObj = None
print("Brewster's Used Cars, Inc.")
print("Sales Report")
print()
print("Salesperson ID           Sale Amount")
print("=" * 35)
try:
    salesfile = open(fileName, 'r')
except IOError:
    print("Error opening the file")

else:
    subtotal = 0
    Total = 0
    lastID = None
    prevID = ""
    IDTotal = 0


    for line in salesfile:

        fields = line.split()
        ID = fields[0]
        amt = float(fields[1])

        if(prevID != ""):
            if((prevID != ID)):
                print("Total sales for this salesperson: "+ str("${:,.2f}". format(IDTotal)))
                print()
                IDTotal = 0

#in the case list of fields failed to populate. 
        #if lastID is None:
            #lastID == ID
# if ID is string 
        if ID != None:
            subtotal = 0
            lastID = ID
            print (str(ID) + "                       " + str("${:,.2f}". format(amt)) )
            Total += amt
            IDTotal += amt
            prevID = ID
    print("Total sales for this salesperson: "+ str("${:,.2f}". format(IDTotal)))   
    print("Total of all Sales:", str("${:,.2f}". format(Total)))
finally:
    try:
        salesfile.close()

    except (IOError, NameError):
        print('Error closing the file "' + fileName + '".')

