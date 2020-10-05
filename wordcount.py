# put your code here.
 
def letter_count_in_dict(file):
    ''' Defines count of each letter in dictionary'''
    
    nFile = open(file)
    counted_letters = {} #empty dictionary 

    for letter in nFile:
        # if letter.isalpha() == True: 
        counted_letters[letter] = counted_letters.get(letter, 0) + 1

    return counted_letters

print(letter_count_in_dict('test.txt'))

