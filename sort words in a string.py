#This code sorts the list of words in alphabetical order

# take input from user
str=input("Enter a string:")

#break the string in words take words in lower case
words=[word.lower() for word in str.split()]

#sort the words of the string
words.sort()

#print sorted words
print("\nThe sorted words of the string are:\n")
for word in words:
    print(word)
