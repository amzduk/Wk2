'''
 Exercise 3:
 Given a paragraph of text, 
 1. count the number of times each character occurs in the text, 
   and print out each character and its count (in any order).
 2. do it now in a case-insensitive manner for the alphabets
 3. extension: print in the descending order of the count
'''


def count_char(text):
    pass
    # add your code here
    d = {}
    for i in text:
        letter = i
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1
    for i in d:
        print(i, d[i])




def count_char_insensitive(text):
    pass
    # add your code here
    d = {}
    for i in text:
	i.lower()
        letter = i
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1
    for i in d:
        print(i, d[i]) 



# bonus task:
def count_char_ordered(text):
    pass
    d = {}
    for i in text:
        i.lower()
        letter = i      
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1
    
    a = 0
    count = d.Values.Max()
    while count > 0:
        for i in d:
            if a != len(d):
                if d[i] == count:
                    print(i, d[i])
        count -= 1

    # add your code here 

text1 = 'I felt happy because I saw the others were happy and because I knew I should feel happy but I wasn’t really happy' # Robert Bolano
text2 = 'HellO, WorLd!'

# testing exercise 2
count_char(text2)
count_char_insensitive(text2)
count_char_ordered(text2)

