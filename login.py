#issues to be resolved
granted=False

def grant():
    global granted
    granted=True

def login(name,password):
    success=False
    file=open("login.txt","r")
    if {name} in file:
        print("Login Successfull")
    else:
        print("Wrong Credentials")
    for i in file:
        a,b=i.split(",")
        b = b.strip()
        if (a==name and b==password):
            success=True
            break
    file.close()
    if (success):
        print("Login Successfull")
        grant()
    else:
        print("Wrong Credentials")



def register(name,password):
    file=open("login.txt","a")
    file.write("\n"+name+","+password)
    file.close()
    grant()

def access(option):
    global name
    if (option=="login"):
        name=input("Enter name:")
        password=input("Enter password:")
        login(name,password)
    else:
        print("Enter your name and password to register ")
        name = input("Enter name:")
        password = input("Enter password:")
        register(name, password)


def start():
    global option
    print("Welcome")
    option=input("Login or Register (login,reg):")
    if (option!="login" and option!="reg"):
        start()


start()
access(option)
if (granted):
    print("Welcome")
    pritn("Username:",name)

