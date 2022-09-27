

userMonth = int( input("please enter a month: ") )

userDay = int( input( "please enter day:"))

userYear = int( input("please enter two digit year: "))

 

if (userMonth * userDay == userYear):
    print( "the date " + str( userMonth ) + "/"+str( userDay )+ "/" + str( userYear ) +" is  magic")
else:
    print( "the date " + str( userMonth ) + "/"+str( userDay )+ "/" + str( userYear ) +" is not  magic")

