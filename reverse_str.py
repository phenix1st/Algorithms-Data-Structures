sentence =  input (" Enter a sentence:  ")
rev =""
for i in range (len (sentence)) :
    rev = rev + sentence [len (sentence)-i-1]
print (" Reverse of the sentence is: ", rev)