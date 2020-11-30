# program generates 4 digit no. using random function and user needs to guess the number.For every digit user guesses at correcty position we print one place is correctly guessed
# to quit the game user has to enter 10
import random
nump =random.randint(1000,9000)
print(nump)
n=int(input("Enter a 4 digit number:"))
while n!=10:
    num=nump
    cor=0
    while num%10:
        numc=num%10
        nc=n%10
        num=num//10
        n=n//10
        if numc==nc:
            cor=cor+1
    if cor==4:
        print("Congrats ! You gussed it right")
        break
    else:
        print("%d digits were guessed right"%cor)
        n=int(input("Enter a 4 digit number:"))
else:
    print("You quit the game")