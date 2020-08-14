# practice dictionary skills 
# write a program to store cars and their descriptions..
# look up a car get a description 
# first make a dictionary of car
 # format: name = {key1:index1, key2:index2}


# for the dictionary go ahead and add some more cars and their descriptions. 

# remember the format. ..... 

# {stuff: description , newstuff:newdescription}
# so go to the end of the dictionary, add a comma, and then CARTYPE : CARDESCRIPTION of course car type and description can be whatever you want them to be. 

myCars = {"Ford F150":"Mid sized pickup truck", "Honda Civic":"small sporty coup....enough for a good squad of people","Jeep CJ":"The old school classic jeep", "Lamborghini SV":"really cool engine and interior... awesome sound!...details and texture!", "Aston Martin":"..not a huge fan.... I also cant spell today", "Ferrari 812superfast":"A 12 cylinder monster", "Tesla":"Cool stuff"}

print("enter a car")
userInput = input().strip()

if(userInput in myCars):
    print(myCars[userInput])
else:
    print("sorry, we didn't find " + userInput + " in the car dictionary")








 