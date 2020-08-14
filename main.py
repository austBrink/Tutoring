
# HomeWorkAssignmentTWO 
# pretend you are working for a software firm (could be for the government, for research, or a company making games)
# You are assigned to a team to ensure that software user's accounts are secure. It's your job to create profiles and check passwords.
# in this program your job is to..... 
# 1) Use print() to display a welcome to the program 
# 2) Use print() to tell the user to enter their name 
# 3) Use this line of code .... userName = input() .... to save the users name
# 4) Use print() to tell the user to enter their password 
# 5) Use set userPassword = input() to save the user password. 

# 6) Now as a test, print() the username and the userpassword 


# Later we will build a login function that will check and see if an entered username and password match these ones you just coded in! :) So stay tuned. 


# Happy coding
# Enter your name here print)

print("Please enter your name")
yourName=input().strip() # to save the user password 
print("now enter password")
yourPassword=input().strip()  # the username and the password

# now that a username and password are saved in their variables. lets try to enter the program. 
print("thanks for coming back. enter your username and password to log in")

loggedOut = True
while(loggedOut==True):
  print("Enter your username to log in")
  newUserName = input().strip()
  print("Enter a password to login")
  newUserPassword = input().strip()

  if (newUserName == yourName):
    if(newUserPassword == yourPassword):
      print("WELCOME TO THE PROGRAM YOUR IN")
      print("Hello " + yourName)
      loggedOut = False
    else:
      print("nope your password didnt match")
  else:
    print("nope inccorect user name") 







