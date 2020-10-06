# put your code here.
 
def word_count_in_dict(file):
    ''' Defines count of each letter in dictionary'''
    
    nFile = open(file)
    counted_words= {} #empty dictionary 
    
    for line in nFile: ## for line in nFile:
        line = line.split(" ")
        # counted_letters[letter] = counted_letters.get(letter, 0) + 1

        for word in line:
            if word.isalpha() == True: 
                counted_words[word] = counted_words.get(word, 0) + 1
    
    return counted_words
                

    # return counted_words

print(word_count_in_dict('test.txt'))