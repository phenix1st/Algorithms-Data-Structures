message=input("Enter your message with an emoji using Fs :")
message=message.split(" ")
emojis={
    ":)" :"😁" ,
    ":(" :"😔",
    ":D" :"😂",
    ":P" :"😜",
    ":-)" :"😊",
}
result=""
for word in message :
    result += emojis.get(word, word) + " "

print(result)


