word1= input("enter the first word")
word2= input("enter the second word")
def cheker(w1,w2) :
    if w1==w2 :
        return True
    elif len(w1)> len (w2)  or len(w1) < len(w2) or w1 != w2 :
        return False
    elif w1[0] == w2[0] :
        return cheker(w1[1:],w2[1:])

fact=cheker(word1,word2)
print(f"the words {word2}, {word1} are same") if fact else print(f"the words {word2}, {word1} are not same")

