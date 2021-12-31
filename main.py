class Library:
    def __init__(self, booklist, library_name):
        self.booklist = booklist
        self.library_name = library_name
        self.lenddict = {}

    def display_book(self):
        print(f"we have the following book in our {self.library_name}")
        for book in self.booklist:
            print(book)

    # user = the person who is having the book and book = the book which the user
    def lend_book(self, user, book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book: user})
            print(f"The lender database has been updated , now u can take the book")
            print(f"The is with {user}")
        else:
            print(f"oops you can not use the book , it is been lended by {self.lenddict[book]}")

    def add_book(self, book):
        self.booklist.append(book)
        print("book is been added  to the book list")

    def return_book(self, book):
        self.lenddict.pop(book)


if __name__ == '__main__':
    Affan = Library(['Amaze', 'All over', 'Again', 'be good', 'c++', 'canvas', 'deploy', 'integrate',
                     'python for every one', 'Java', 'learn to be master'], "tech")

    while True:
        print(f"Welcome to th world of books  {Affan.library_name}")
        print("1. To display books")
        print("2. To lend books ")
        print("3. To add books")
        print("4. To return book")
        user_choice = input("Enter your choice")
        if user_choice not in ['1','2','3','4']:
            print("Enter a valid option")
            continue
        else:
            user_choice=int(user_choice)


        if user_choice == 1:
            Affan.display_book()

        elif user_choice == 2:
            book = input("Enter the name of book you want from ")
            user = input("Enter your name ")
            Affan.lend_book(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book your adding")
            Affan.add_book(book)

        elif user_choice == 4:
            book = input("Enter the book name you want  to return ")
            Affan.return_book(book)

        else:
            print("Invalid input !!!!! ")
            print("not a valid option")

        print("press n to exit and y  to continue")
        user_choice2 = ""
        while user_choice2 != "y" and user_choice2 != "n":
            user_choice2 = input()
            if user_choice2 == "n":
                exit()
            elif user_choice2 == "y":
                continue
