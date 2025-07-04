word= input("enter the word to check if it is palidrome : ")
word=word.lower()
if word==word[::-1]: # checking if the word is equal to its reverse
    print("the word is palindrome")
else :
    print("the word is not palindrome")

# word[::-1] is used to reverse the word