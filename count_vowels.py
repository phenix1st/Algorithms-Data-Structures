sentence = input("Enter your string : ")
sentence = sentence.lower()
count = 0
for x in sentence:
    match x:
        case "a" | "e" | "i" | "o" | "u":
            count += 1
        case _:
            pass
print("The vowels appears", count, "times in the string.")