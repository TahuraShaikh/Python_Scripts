'''Twenty random cards are placed in a row all face down.
A turn consists of taking two adjacent cards where the left one is face up and the right one can be face up or face down and flipping them both.
Show that this process must terminate. (with all the cards facing up).'''

def transform(b):
    for i in range(len(b)-1):      #as last card will not have any card to its right.
        if b[i] == '1':            #1 is for face down
            b[i] = '0'                      # 0 is face up
            if b[i+1] == '0':         # card to the right
                b[i+1] = '1'             
            else:
                b[i+1] = '0'
    return b

if __name__ == "__main__":
    a = list("011111001")      #can take any no. of items in list
    print(a)
    while a != transform(a.copy()):
        a = transform(a.copy())
    print(a)