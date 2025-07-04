phone=input("Enter your cell phone number: ")
cell=""
numbers={
    "1":"one"
    , "2":"two"
    , "3":"three"
    , "4":"four"
    , "5":"five"
    , "6":"six"
    , "7":"seven"
    , "8":"eight"
    , "9":"nine"
}
for x in phone :
    cell += numbers.get(x,"not found !")+ " "

print(f"Here is Your phone number in words : \n {cell}")