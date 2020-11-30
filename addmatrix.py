r=int(input("Enter no. of rows"))
c=int(input("Enter no. of columns"))
x=[]
val=[]
for i in range(0,r):            # r is no. of elements in x, i.e no. of lists within parent list x will be counted in i
    for j in range(0,c):         # inner for loop is for elements within child list will be counted in j
        val.insert(j,int(input("enter the %d %d element"%(i,j))))      # input from user will be inserted in temporary list val
    x.insert(i,val)          # once we exit inner for loop we will add the list val  to parent list x
    val=[]                   # clears the temporary list val everytime we exit the inner for loop
Y=[]
for i in range(0,r):            # r is no. of elements in x
    for j in range(0,c):

        val.insert(j,int(input("enter the %d %d element"%(i,j))))   # if we don't use int to convert user input it just concatinates the values
    Y.insert(i,val)
    val=[]
sum=[]                     # This list holds added values from other two lists
# For accessing elements of list containing lists we need nested for loops
for i in range(0,r):
    for j in range(0,c):
        val.insert(j,x[i][j]+Y[i][j])  # 1st add elements of the child list i.e sum of 1st list within x and sum of 1st list within y & when we find sum we will put it into our parent list sum
    # above line : at the jth position sum of elements in jth position of our ith list in x & y
    sum.insert(i,val)                        # at the ith position of sum insert val
    val=[]            # clear val when we exit inner for loop
print(sum)             # two list of lists from user add them and print their sum