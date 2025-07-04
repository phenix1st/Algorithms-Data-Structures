def max(a,b) :
    if a>=b :
        return a
    else:
        return b
    

user_input = input("Enter numbers separated by commas: ")
num_list = user_input.split(",")            # ['1', '2', '3'] #.split() splits a string into a list where each word is a list item
clean_list = []       # [1, 2, 3]
for x in num_list :
    clean_list.append(int(x))

larg=clean_list[0] 
for y in clean_list :
    larg = max(larg,y)

print(f"the max in the list is {larg}")