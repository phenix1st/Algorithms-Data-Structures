"""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""
# Lists
# Lists are ordered collections of items that can be of any data type, including strings, integers
# Lists are denoted by square brackets [] and are mutable, meaning they can be changed after creation
# Lists are ordered, meaning that items have a specific position in the list
# Lists are indexed, meaning that each item has a specific index or position in the list
# Lists are mutable, meaning that they can be changed after creation
# example
names = ["adem", "yaakoub", "mohammed", "jalil", "seddiki", "wassim"]
print(names[0])  # this will print adem
print(names[-1])  # this will print wassim
print(names[2:])  # this will print mohammed,jalil,seddiki,wassim
print(names[:])  # this will print all the list

# 2D Lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# to access the items we use matrix[][] rows first than colomns
print(matrix[0][2])
matrix[0][2] = 225
print(matrix)  # this will print [[1,2,3],[4,5,6],[7,8,9]

# this means each time rows will have a list of the three first [1,2,3] then [4,5,6] then [7,8,9]
for rows in matrix:
    for item in rows:  # this means each time item will have a number 1,2,3 then 4,5,6 then 7,8,9
        print(item)  # this will print each number

# to insert a new element from the end we use .append
# to insert a new element from the middle or beginning or the end we use .insert
# hamdi will be in index 2 new list is "adem","yaakoub","hamdi","mohammed","jalil","seddiki","wassim"
names.insert(2, "hamdi")
# to remove a item we use .remove
names.remove("hamdi")  # hamdi will be removed
# to remove all the list elements we use clear
names.clear()  # this empties the list []
num = [1, 2, 3, 3, 4, 6, 5]
# to remove the elements from the end we use .pop  removes from the end in default (fargha)
num.pop()
# to find the index of an element we use .index
num.index(2)  # this will return 1 which is the index of number 2 in the list or the first occurence of an element in other meanings
# if we pass a value that dont exist in the list we get error in terminal
# a solution
print(50 in num)  # this will return False because 50 doesnt exist in num list
# to search for the occurences of an element we use .count
print(num.count(3))  # this will return 2 occurences of 3
# to sort any list we use .sort
num.sort()  # this way the list is sorted
# to reverse any list we use .reverse
num.reverse()  # this way our list is reversed
num31 = num.copy()  # to copy a list into another list we use .copy this way num31 == num
