import pickle

username = ""
password = ""
prevUser = False
loggedIn = False 
def menuPrint():
  print("WELCOME TO THE PROGRAM")
  print("ENTER ONE OF THE VALID CHOICES")
  print("create: to create new account")
  print("login: to enter credentials and login")
  print("cars: to use the car dictionary")
  print("Q: to quit")

def loadProfile():
  try:
    with open('profile_data','rb') as output:
      global username = pickle.load(output)
      global password = pickle.load(output)
  except:
    print("looks like your new to the car dictionary program: create an account to get started!")

def createAccount(name, passcode):
  global username = name
  global password = passcode
  with open('profile_data','rb') as output:
    pickle.dump(username)
    pickle.dump(password)
  global prevUser = True 
  
userChoice = ""


while (userChoice!= "Q"):

  if(userChoice == "login"):
    loadProfile()
    if(loggedIn==False and prevUser == True):
      while(global loggedIn == False):
        name = input("NAME:")
        word = input("PASSWORD:")
        if(name == global username and word == global password):
          print("Hello, " + name)
          global loggedIn = True
      
  elif(userChoice == "create"):
    if(global prevUser == False):
      global username = input("NAME:")
      global password = input("PASSWORD:")

  elif(userChoice == "cars"):
    if(global loggedIn == True):
      print("Coming soon")

