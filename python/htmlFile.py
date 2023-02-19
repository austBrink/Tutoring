'''
Write a program that asks the user for his or her name, then asks the user to enter a sentence that describes himself or herself. Here is an example of the program’s screen:
 
Enter your name: Julie Taylor [Enter] 
Describe yourself: I am a computer science major
Once the user has entered the requested input, the program should create an HTML file, containing the input, for a simple Web page. Here is an example of the HTML content, using the sample input previously shown:
<html>
 <head>
 </head>
 <body>
    <center>
       <h1>Julie Taylor</h1>
    </center>
    <hr />
    I am a computer science major
    <hr />
 </body>
 </html>
 '''

#create variables for input, prompting the user for username and bio. 
userName = input("Enter your name: ")
userBio = input("tell us about you: ")

#create a string to populate the HTML file 
htmlContent =  '<html>\n<head>\n</head>\n<body>\n<center>\n<h1>' + str(userName) + '</h1>\n </center> \n <hr/> ' + str(userBio) + '\n <hr /> \n </body> \n </html>' 

#create and open an html file reference for writing. 
htmlFile = open('index.html', 'w')

#write the html content string to the file 
htmlFile.write(htmlContent)

#close the file
htmlFile.close()





    
    
    



