#This is the code for letter frequency analysis
Alphabet1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Alphabet2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
list1=[]
def analyse(text):
    for i in range(0,26):
        letters = text.count(Alphabet1[i]) + text.count(Alphabet2[i])
        list1.append(letters)
        if len(list1) == 26:
            return list1
        

print(analyse("zZ"))

