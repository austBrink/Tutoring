import pickle 
# global variable  

TRED =  '\033[31m' # Green Text
TWHITE = '\033[37m'
class profile:
    def __init__(self, name, password):
        self.name = name 
        self.password = password
    
    def getName(self):
        return self.name
    
    def isPassword(self, attmpt):
        if(attmpt == self.password):
            return True
        else:
            return False
    
    def setPassword(self, oldPassword, newPassword):
        if (oldPassword == self.password):
            self.password = newPassword
            return 0 
        else:
            return -1 

# # # # # # # # # # # # # # # # # # # # # # # # # # #
def printMenu():
    print("Welcome to this dictionary!")
    print("choose an option:")
    print("enter S to use the dictionary")
    print("enter L for log in")
    print("don't have a profile? make one now by pressing M!")
    print("enter Q to quit")
# # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # #
# need to make this uncallable if logged in.... 
# also need to figure out how to make multiple log ins eventaully?? 
def createProfile(name, passwird):
    newProfile = profile(name, passwird)
    #pickle the profile....
    with open('profile_data', 'wb') as output:
        pickle.dump(newProfile, output, pickle.HIGHEST_PROTOCOL)
        pickle.dump(newProfile, output, pickle.HIGHEST_PROTOCOL)
    return newProfile


def login(loggedIn):
    loggedIn = True
    profileThere = False
    try:
        with open('profile_data','rb') as readIn:
            validProfile = pickle.load(readIn)
            profileThere = True
    except:
        print(TRED + "FILE ERROR", TWHITE)
    if(profileThere):
        fail = True
        while(fail):
            print("LOG IN:")
            print("____________________________")
            name = input("USERNAME -->>").strip()
            password= input("\t PASSWORD -->>").strip()
            if(name == validProfile.getName() and validProfile.isPassword(password)):
                fail = False
                return validProfile
            else:
                print (TRED + "UserName and or Password do not match!" , TWHITE)
    return None

# this is homework assignment part one. Go ahead and add cars to the dictionary. Remember first enter a comma, then the car name, then the ":" symbol followed by the definition of the car. 
def dictionary():

  myCars = {"Ford F150":"Mid sized pickup truck", "Honda Civic":"small sporty coup....enough for a good squad of people","Jeep CJ":"The old school classic jeep", "Lamborghini SV":"really cool engine and interior... awesome sound!...details and texture!", "Aston Martin":"..not a huge fan.... I also cant spell today", "Ferrari 812superfast":"A 12 cylinder monster", "Tesla":"Cool stuff", "57 Chevy": "classic Car", "Mclauren 720s":"really cool and fast"}

  userInput = ""
  while(userInput != "Q"):
    print("enter a car")
    userInput=input().strip() 
    if(userInput in myCars):
        print(myCars[userInput])
    else:
        print("sorry, we didn't find " + userInput + " in the car dictionary")

# # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # #
#MAIN PROGRAM 
# # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # #

#call the printMenu function and he'll get to work. 
loggedIn = False
printMenu()
# main menu functionality 
userChoice = ""
userProfile = None
while(userChoice!="Q"):
    userChoice = input("\t-->>")
    #User chose to start the / a  Game...
    if(userChoice == "S"):
        if(userProfile!=None):
            print("Hello, " + userProfile.getName() + "!")
            dictionary()
        else:
            print("You must login or signup to show that")
    #user wnats to log in 
    elif(userChoice=="L"):
        if(loggedIn == False):
            userProfile = login(loggedIn)
            if(userProfile != None):
                print("Welcome, " + userProfile.getName() + "!")
            else:
                print("Need to create a profile to get started")
            pass 
        elif(loggedIn == True):
            print("You are already logged in")

    elif(userChoice == "M"):
        # 1) notify
        # 2) ask for name 
        # 3) ask for passwrod
        # 4) pass to the create function... 
        if(userProfile == None):
            print("CREATE A USER")
            print("Enter your player name:")
            userName = input().strip()
            print("Choose a password")
            passWord = input().strip()
            userProfile = createProfile(userName,passWord)
    #lets go. nothing here for now... 
    #This will be where you enter the code for Homework part two. output a message to the user saying goodbye or something. 
    elif(userChoice == "Q"):
        print("Have a good weekend!")