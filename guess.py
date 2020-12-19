#Guess the number between 1 to 10:
import random
randNumber=random.randint(1,10)
print(randNumber)
Guess=None                    #this is the player guess, set to none as we are using in loop
guesses=0
while(Guess!=randNumber):
    Guess=int(input("Enter your guess:"))
    if (Guess==randNumber):
        print ("\nYour guess is right,congrats!!!")
    else:
        if (Guess>randNumber):
            print("Your guess is wrong, please enter smaller number than this")
        else:
            print("You guess is wrong, please enter a larger number than this")
    guesses+=1
print(f"You guessed the number in {guesses} attempts")
with open ("attempts.txt","r") as f:           #attempts text file has attempts of the user
    attempts=int(f.read())
if (guesses<attempts):
    print("You have broken the record")
    with open ("attempts.txt","w")as f:
        f.write(str(guesses))     #can also append