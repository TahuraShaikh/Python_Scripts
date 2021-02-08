#without GUI: simple start stop quit commands for a game

'''help:
start: to start our game, msg: started ,ready to go
stop : to stop our game, msg:  stopped
quit: to exit, program terminates.
for other command: sorry , choose from the 3 options '''

print("\n Are you ready to play, choose : \n\nstart(S), stop(T), help(H):")

command=""
started=False
stopped=False

while True:
    command=input(">").upper()

    if command == "S":

        if started:
            print("Already started")
        else:
            started=True
            print("Started ,ready to go")

    elif command=="T":
        if stopped:
            print("You are already stopped")
        else:
            stopped=True
            print("You stopped")

    elif command=="H":

        print('''
(S): to start 
(T): to stop
(Q): to exit''')

    elif command=="Q":
        break
    else:
        print("Sorry, choose from the 3 options")