pyg = 'ay'

original = input('Enter a word:')

language = input("Put in 'p' for Pyglatin or 'e' for English:")




if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word[1:len(word)]
    if word[-2:len(word)] == pyg:
        ends_with_ay = True
    else:
        ends_with_ay = False
#check if the first letter of the word has a vowel
    if first =='a' or first== 'e' or first =='i' or first == 'o' or first == 'u': 
        starts_with_vowel = True
    else:
        starts_with_vowel = False
#check if user wants to encrypt a word into Piglatin or decrypt a Piglatin into English
    if language == 'e':
        if starts_with_vowel== True and ends_with_ay == True:
            word = word[0:len(word)-2]                                 #getting rid of 'ay'
            word = word[-1] + word[0:len(word)-1]
            print (word)
        else:
            print ("THIS ISNT PIG LATIN!")
    if language == 'p':
        if starts_with_vowel== False or ends_with_ay == False:
            word = new_word + first + pyg
            print (word)
        else:
            print ("THIS ISNT ENGLISH!")
        
else:
    print ('empty')
