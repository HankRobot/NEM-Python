#this is the code for substitute() procedure
# rules: 1) substituted are left without capital or lowered case, 2)non-substituted letters are then upper cased
Alphabet1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Alphabet2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def substitute(text,guess):
    replacement = text.upper()                                                  # uppercase all texts
    for i in range(0,26):
        get_upperletters = Alphabet2[i]                                         # this will get 'a' to 'z' in upper case
        position = guess[i]                                                     # this will get letters of guess
        if position != '_':                                                     # only replace letters if guess doesn not have '_'
            replacement = replacement.replace(get_upperletters, position)
    return replacement
    
print(substitute('Dont tell anyone pls','c_________encrypt_________'))


