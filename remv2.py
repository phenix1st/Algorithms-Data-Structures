user_input = input("Enter numbers separated by commas: ")
num_list = user_input.split(",")            # ['1', '2', '3'] #.split() splits a string into a list where each word is a list item
clean_list = []      # [1, 2, 3]
result = [] 
for x in num_list :
    clean_list.append(int(x))
for number in clean_list :
    if number not in result :
        result.append(number)
if result == clean_list :
    print("there is not duplicates to remove ")
else:
    print(f"the new list is {result}")