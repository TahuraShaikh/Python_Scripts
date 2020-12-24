# Simple Library management using Library and student class:
class Library:
    def __init__(self,books_list):
        self.books=books_list


    def display_available(self):
        print("Books available now in the library: ")
        for book in self.books:
            print("-> " + book)

    def borrow(self,name_book):       #function to borrow
        if name_book in self.books:
            print(f"You have been issued {name_book}.Please return it in 30 days")
            self.books.remove(name_book)           # when book is borrowed it is removed from the list
            return True
        else:
            print(f"Sorry,{name_book} is issued to someone else.We will update once it is returned.")
            return False
    def issued(self,student_name):
        self.student_name=name
        with open ("Issued.txt","w")as f:
            f.append(f"{name_book} is issued to {name}")

    def return_book(self,name_book):
        self.books.append(name_book)              # when book is returned it is appended to the list
        print(f"Thanks for returning{name_book} book.")

class Student:
    def __init__(self,student_name):
       self.student_name=input("Enter your name: ")
    def request_book(self):
        self.book = input(f"{self.student_name} , enter the name of the book you want to borrow: ")
        return self.book

    def return_book(self):
        self.book = input(f"{self.student_name}, enter the name of the book you want to return: ")
        return self.book


if __name__=="__main__":
    LibbyRead=Library(["Python","Java","C++","Django","ML","DS","AI"])    # Only one book available, if someone borrows it will be removed from available.
    #Libby.borrow("Java")
    student=Student("Susan")

    while (True):
        msg='''\n *** Welcome to Libby Read ***
        Choose from the following:
        1) List of Books
        2) Request for a book
        3) Return/Add a book
        4) Exit
        '''
        print(msg)
        x=int(input("Enter your choice: "))
        if x==1:
            LibbyRead.display_available()
        elif x==2:
            LibbyRead.borrow(student.request_book())
        elif x==3:
            LibbyRead.return_book(student.return_book())
        elif x==4:
            print("Thanks for choosing LibbyRead")
            exit()
        else:
            print("Please enter correct choice.")

