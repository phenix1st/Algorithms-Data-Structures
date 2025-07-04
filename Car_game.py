started=False
while True:
    message=input("> Enter the command : ")
    if message.lower() == "help" :
        print("Available commands: \n 1-start : start the car \n 2-stop : stop the car \n 3-quit : exit the program")
    elif message.lower() == "start":
        if started:
            print("Car is already started")
        else :
            print("Car started. Ready to go!")
    elif message.lower() == "stop":
        if started:
            print("Car stopped.")
            started=False
        else :
            print("Car is already stopped")
    elif message.lower() == "quit":
        break
    else:
        print("Invalid command. Please try again.")

print("Exiting the program. Goodbye!")







        