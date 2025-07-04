sentence = input("Enter your string : ")
char = input("Enter the character you want to find : ")
count = 0
for x in sentence:
    if x == char:
        count += 1
print("The character", char, "appears", count, "times in the string.")