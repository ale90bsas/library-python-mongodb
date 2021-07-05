import os
import json
from book import Book
import pymongo
from ast import literal_eval


#Initialize DB connection
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["library"]
books_db = db["books"]


def clear_screen():
     os.system('clear')

def print_options():
    print("Choose your option")
    print("1. Create a Book")
    print("2. Issue a book")
    print("3. Return a book")
    print("4. Update a book")
    print("5. Show all books")
    print("6. Show specific book")
    print("7. Find")
    print("--- Press x to Exit ---")
    print("\n\n")

def input_book_info():
    print("Please enter your book info")
    id = input("Enter ID: ")
    name = input("Enter Name: ")
    isbn = input("Enter ISBN: ")
    page_count = int(input("Enter the Page count: "))
    issued = input("Has your book being issued? y/n: ")
    issued = (issued.lower == "y")
    author = input("Enter the Author: ")
    year = int(input("Enter the year when the book has been published: "))

    return {
        "id" : id,
        "name" : name,
        "isbn"  : isbn,
        "page_count" : page_count,
        "issued" : issued,
        "author" : author,
        "year" : year
    }

def create_book():

    book_dict = input_book_info()

    book = Book(
    book_dict['id'],
    book_dict['name'],
    book_dict['isbn'],
    book_dict['page_count'],
    book_dict['issued'],
    book_dict['author'],
    book_dict['year'])

    books_db.insert_one(book.to_dict())

    print("\nYour book has been created\n")
    print(book.to_dict())
    return book

def update_book(books):
    book_id = input("Please enter the ID of the desired book: ")
    book = find_book(book_id)
    if(book != None):
        
        print("Current book's information:")
        print_book(book)
        updated_book_dict = input_book_info()

        books_db.update_one(
            {"id" : str(book.id)},
            {"$set": updated_book_dict}
        )

        print("Your book has been updated!")

    else:
        print("Book not found!")



    json_books = []
    books = []

    try:
        file = open("books.json","r")
        json_books = json.loads(file.read())
        file.close()
    
    except Exception as e:
        print("There was an error reading the file: ", e)
    
    for json_book in json_books:
        book = Book(
        json_book['id'],
        json_book['name'],
        json_book['isbn'],
        json_book['page_count'],
        json_book['issued'],
        json_book['author'],
        json_book['year'])

        books.append(book)

    return books

def print_book(book):

    if(book != None):
        print("\n")
        print("Title: ",book.name)
        print("ID: ",book.id)
        print("Author: ",book.author)
        print("ISBN: ",book.isbn)
        print("Pages: ",book.page_count)
        print("Year: ",book.year)
        print("Issued: ",book.issued)
        print("\n----------------------\n")
    
    else:
        print("Book not found!")

def show_book():
    book_id = int(input("Please enter the ID of the desired book: "))
    book = find_book(book_id)
    if(book != None):
        print_book(book)
    else:
        print("Book not found!")

def print_books():
    books= books_db.find({},
    {
    "_id":0,
    "id":1,
    "name":1,
    "isbn":1,
    "page_count":1,
    "issued":1,
    "author":1,
    "year":1
    }).sort("id",1)

    print("\n==========================\nList of Books in the system\n==========================\n")
    for book_dict in books:
        book = Book(
        book_dict['id'],
        book_dict['name'],
        book_dict['isbn'],
        book_dict['page_count'],
        book_dict['issued'],
        book_dict['author'],
        book_dict['year'])

        print_book(book)
    
def find_book(book_id):

    search = "{\"id\":" + str(book_id)+"}"
    book_dict = find_books(search)[0]

    book = Book(
        book_dict['id'],
        book_dict['name'],
        book_dict['isbn'],
        book_dict['page_count'],
        book_dict['issued'],
        book_dict['author'],
        book_dict['year'])

    return book

def issue_book():
    book_id = input("Please enter the ID of the book you want to issue: ")
    book = find_book(book_id)
    if(book != None):
        
        books_db.update_one(
            {"id" : str(book.id)},
            {"$set": {"issued": True}}
        )

        print("Your book has been issued!")

    else:
        print("Book not found!")

def return_book():
    book_id = input("Please enter the ID of the book you want to return: ")
    book = find_book(book_id)
    if(book != None):
        
        books_db.update_one(
            {"id" : str(book.id)},
            {"$set": {"issued": False}}
        )

        print("Your book has been returned!")

    else:
        print("Book not found!")

def find_books(param):
    search = literal_eval(param)
    print(search)
    results =  books_db.find(
     search
    ,
    {
    "_id":0,
    "id":1,
    "name":1,
    "isbn":1,
    "page_count":1,
    "issued":1,
    "author":1,
    "year":1
    })

    return results
    
def find():
    param = input("Please enter search function: ")
    results = find_books(param)
    result_cnt = 0

    if(results != None):
        
        for book_dict in results:
            book = Book(
            book_dict['id'],
            book_dict['name'],
            book_dict['isbn'],
            book_dict['page_count'],
            book_dict['issued'],
            book_dict['author'],
            book_dict['year'])

            result_cnt +=1

            print_book(book)
        print(result_cnt," results found\n\n")
    else:
        print("No results!")
    