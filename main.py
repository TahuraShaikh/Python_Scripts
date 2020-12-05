'''n=int(input("Enter a number"))         #n=5678      # reversing a number
nr=0                                   #nr=8765
while n%10!=0:        # removes the last no. and checks till its value is not equal to 0
    c=n%10              #
    nr=nr*10+c
    n=n//10
print(nr)'''

from playsound import playsound
playsound('D:\\Ritviz.WAV')