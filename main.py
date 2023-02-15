command = ""
while True:
    command = input("> ").lower()
    if command == "start" :
        print("Car started......")
    elif command == "stop":
        print("Car stopped....;.")
    elif command == "help":
        print("""
start --> to start car
stop --> to stop car
quit --> to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand!!")
