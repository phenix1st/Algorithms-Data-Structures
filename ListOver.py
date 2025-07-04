user_input=input("Enter your First List seperated by a comma , : ")
user_input2=input("Enter your second List seperated by a slash / : ")
user_input=user_input.split(",")
user_input2=user_input2.split("/")
clear_list=[]
clear_list2=[]
list3=[]
for i in user_input:
     clear_list.append(int(i))
for n in user_input2 :
     clear_list2.append(int(n))    
k=0
for y in user_input :
     for x in user_input2 :
          if y==x :
              list3.insert(k,y)
              k+=1

print(f"the common elements in the two list are {list3}")
#AI Solution and correction for some mistakes 
"""
user_input = input("Enter your First List separated by commas: ")
user_input2 = input("Enter your Second List separated by slashes: ")

# Split and convert to integers
clear_list = [int(i) for i in user_input.split(",")]
clear_list2 = [int(n) for n in user_input2.split("/")]

# Find common elements
list3 = []
for i in clear_list:
    if i in clear_list2:
        list3.append(i)

print(f"The common elements in the two lists are: {list3}")
"""