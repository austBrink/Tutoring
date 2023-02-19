# open a text file 
# display unique words 
# use a set 

TEXT2 = "c:/vault/tutoring/python/text2.txt"
words = set(open(TEXT2).read().split())
print('unique words from the file: \n')
for i in words:
    print(f'\t{i}')
# Yours can be a relative path..
#open('text2.txt')
# my_set = set(map(str.strip, open('filename.txt')))