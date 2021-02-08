num=9
guess_attempts=0
min_attempt=3

while guess_attempts < min_attempt:
    guess=int(input("Enter a number: "))
    guess_attempts+=1
    if guess==num:
        print("You guessed the number right")
        break

else:
    print("You failed")





