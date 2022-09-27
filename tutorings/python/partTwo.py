import pickle

import fileinput

fileToEncrypt = "fileA.txt"

codes = {'a':'!', 'b':'@', 'c':'#', 'd':'$', 'e':'%', 'f':'^', 'g':'&', 'h':'*', 'i':'--', 'j':'_', 'k':'=','l':'+', 'm':'>', 'n':'<', 'o':',,', 'p':'..', 'q':'``', 'r':'~', 's':'//', 't':';', 'u':'?', 'v':'|', 'w':':','x':'...', 'y':'[]', 'z':'>@'}


# get values of keys and return as a tuple? write to file.

f = open(fileToEncrypt, 'r+') 
b = open("fileB.txt", 'r+')
for line in f:
    line = line.rstrip()
    if not line:
        continue
    for f_key, f_value in codes.items():
        if f_key in line:
            line = line.replace(f_key, f_value)
        b.write(line)

b.close()
            