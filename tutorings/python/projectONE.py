

def main():
    print("Welcome! Please, see app specifications below:")
    print("1: Word Count")
    print("2: Word Search")
    print("3: Word Replacement")
    print("4: Word Frequency")
    
    try:
        # Validate user's input
        feature = int(input("Enter the feature of the app you want to use: "))
        while feature < 1 or feature > 4:
            print("You can only specify feature in the range 1-4: ")
            feature = int(input("Enter the feature of the app you want to use: "))

    except ValueError:
        print("ERROR: A non-numeric value was entered")
    else:
        # Ask user to enter a sentence to analyze and assign
        # the input to a variable called sentence
        sentence = input("Enter a sentence: ")
        if feature == 1:
            # call the count_word function and pass sentence as argument
            # assign the value returned by the function call
            # to a variable called word_count
            word_count = count_word(sentence)
            print()
            print(f'There are {word_count} words in the sentence')

        elif feature == 2:
            # Ask user to enter a word to find and assign
            # the input to a variable called word_to_find
            word_to_find = input("Enter a word to find: ")
            # call the is_word_found function and pass
            # sentence and word_to_find as arguments
            # assign the value returned by the function call
            # to a variable called isfound
            isfound = is_word_found(sentence, word_to_find)
            print()
            if isfound:
                print(f'The word {word_to_find} was found in the sentence')
            else:
                print(f'The word {word_to_find} was not found in the sentence')

        elif feature == 3:
            # Ask user to enter a word to replace and assign
            # the input to a variable called word_to_replace
            word_to_replace = input('Enter a word to replace: ')
            # Ask user to enter a replacement word and assign
            # the input to a variable called replacement_word
            replacement_word = input('Enter replacement word: ')
            occurrences, new_sentence = replace_word(sentence, word_to_replace, replacement_word)
            print()
            print(f'There are {occurrences} occurrences of the word "{word_to_replace}" which has been replaced')
            print('The new sentence is: ')
            # print the new_sentence
            print(new_sentence)

        else:
            # call the word_frequency function and pass
            # sentence as an argument
            # assign the value returned by the function call
            # to a variable called unique_words
            unique_words = word_frequency(sentence)
            print()
            print(format("word","15s"), format("frequency", "10s"))
            for key, val in unique_words.items():
                print(format(key,"15s"), format(val, "5d"))
            
# Count the number of words in a sentence
def count_word(sentence):
    # Tokenize sentence into words
    word_list = sentence.split()
    # return the length of the word_list
    return len(word_list)

def is_word_found(sentence, word_to_find):
   return word_to_find.lower() in sentence.lower()

# Replace all the occurrences of a word in a sentence with another word
def replace_word(sentence, word_to_replace, replacement_word):
    # declare an empty list called replacement_idx
    replacement_idx = []
    # Tokenize sentence into words
    word_list = sentence.split()
    # loop through the word list
    # and look for the occurrence of the word
    for i in range(len(word_list)):
        # normalize the case of the word so search
        # can be case insensitive
        if word_list[i].strip('.').strip(',') == word_to_replace:
            # append the value of variable i to the replacement_idx list
            replacement_idx.append(i)
    # find the length of replacement_idx list and assign the value
    # to a variable called occurrences
    occurrences = len(replacement_idx)
    new_sentence =  word_to_sentence(word_list, replacement_idx, replacement_word)
    return occurrences, new_sentence

# Find the unique words and their frequency
def word_frequency(sentence):
    # declare an empty dictionary called unique_words
    unique_words = {}
    word_list = sentence.split()
    
    # loop through the word list
    # and add unique word to the dictionary
    # while incrementing the count of the existing words
    # the dictionary key is the unique word
    # the dictionary value is the word count
    for word in word_list:
        # check if word is a key in unique_words dictionary
        # use the in operator and be sure to maintain the indentation
        if word in unique_words:
            unique_words[word]+=1
        else:
            unique_words[word] = 1
    # return unique_words dictionary
    return unique_words

# Concatenate a list of words into sentence
def word_to_sentence(word_list, replacement_idx, replacement_word):
    # declare a variable sentence and initialize/assign an empty string to it
    sentence = ' '
    for i in range(len(word_list)):
        if i in replacement_idx:
            sentence+=replacement_word+" "
        else:
            sentence+= word_list[i]+" "
    # return sentence
    return sentence
        
# Call the main function
main()
