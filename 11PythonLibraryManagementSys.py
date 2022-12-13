import datetime
import os
# print(os.getcwd())
import random

class LMS:
    """This class is used to keep record of books library
    It has total four module.
    1.Display Books
    2.Issue Books
    3.Return Books
    4.Add Books
    """
    def __init__(self,list_of_books,library_name):
        self.list_of_books = "List_of_books.txt"
        self.library_name = library_name
        self.books_dict = {}
        id = random.randint(100,999)
        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            # print(line)
            self.books_dict.update({str(id):{"books_title":line.replace("\n",""),
                                             "lender_name":"","Issue_data":"","Status":"Available"}})
            id = id+1

    def display_books(self):
        print("___________________________List of books_____________________")
        print("Books ID","\t","Title")
        print("_____________________________________________________________")
        for key,value in self.books_dict.items():
            print(key,"\t\t",value.get("books_title"),"-[",value.get("Status"),"]")

    def Issue_books(self):
        books_id = input("Enter books Id: ")
        current_date = datetime.datetime.now().strftime("%Y-%m_%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]["Status"] == "Available":
               print(f'This books is aleady issued to {self.books_dict[books_id]["lender_name"]} on '
                     f'{self.books_dict[books_id]["Issue_date"]}')
               return self.Issue_books()
            elif self.books_dict[books_id]["Status"] == "Available":
                your_name = input("Enter your name: ")
                self.books_dict[books_id]["lender_name"] = your_name
                self.books_dict[books_id]["Issue_date"] = current_date
                self.books_dict[books_id]["Status"] = "Already Issued"
                print("Books Issued Successfully!!!\n")
        else:
            print("Book Id Not found !!!")
            return self.Issue_books()

    def add_books(self):
        new_books = input("Enter books title: ")
        if new_books == "":
            return self.add_books()
        elif len(new_books) > 25:
            print("Books Title length is too long!!!Title length shoud be 20 characters")
            return self.add_books()
        else:
            with open(self.list_of_books,"a") as bk:
                bk.writelines(f'{new_books}\n')
                self.books_dict.update({str(int(max(self.books_dict))+1):{"books_title":new_books,"lender_name":"",
                                                                         "Issue_date":"","Status":"Available"}})
                print(f"This books '{new_books}' has been added successfully!!!")

    def return_books(self):
        books_id = input("Enter books Id: ")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["Status"] == "Available":
                print("This book is already available in library.Please check your book ID")
                return self.return_books()
            elif not self.books_dict[books_id]["Status"] == "Available":
                self.books_dict[books_id]["lender_name"] = ""
                self.books_dict[books_id]["Issue_date"] = ""
                self.books_dict[books_id]["Status"] = "Available"
                print("Successfully updated!!!\n")
        else:
            print("Book Id is not found")

try:
    myLMS = LMS("List_of_books.txt", "Python's Library")
    press_key_list = {"D":"Display Books","I":"Issue Books","A":"Add Books","R":"Return Books","Q":"Quit"}
    key_press =False
    while not (key_press == "q"):
        print(f"\n______________Welcome to {myLMS.library_name} Library Management System______________")
        for key,value in press_key_list.items():
            print("Press",key,"To",value)
        key_press = input("Press key: ").lower()
        if key_press == "i":
            print("\n Current Selection: Issue Books\n")
            myLMS.Issue_books()
        elif key_press == "a":
            print("\nCurrent Selection: Add Book\n")
            myLMS.add_books()
        elif key_press == "d":
            print("\nCurrent Selection: Display Books\n")
            myLMS.display_books()
        elif key_press == "r":
            print("\nCurrent Selection: Return Books\n")
            myLMS.return_books()
        else:
            continue
except Exception as e:
    print("Something wrong . Please check your input!!!")

