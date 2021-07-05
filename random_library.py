from book import Book
import myFunctions
import sys
from random import seed
from random import choice
import pymongo


#Initialize DB connection
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["library"]
books_db = db["books"]

#erase Database
books_db.delete_many({})

#Number of books to generate
books_cnt = int(sys.argv[1])

#Sample Information
pages_seq = [i for i in range(250,800)]
published_years_seq = [i for i in range(1950,2021)]
isbn_seq = [i for i in range(1111,9999)]
issued_seq = [True,False]
author_names_seq = ["Wade","Dave","Seth","Ivan","Riley","Gilbert","Jorge","Dan","Brian","Roberto","Ramon","Miles","Liam","Nathaniel","Ethan","Lewis","Milton","Claude","Joshua","Glen","Harvey","Blake","Antonio","Connor","Julian","Aidan","Harold","Conner","Peter","Hunter","Eli","Alberto","Carlos","Shane","Aaron","Marlin","Paul","Ricardo","Hector","Alexis","Adrian","Kingston","Douglas","Gerald","Joey","Johnny","Charlie","Scott","Martin","Tristin","Troy","Tommy","Rick","Victor","Jessie","Neil","Ted","Nick","Wiley","Morris","Clark","Stuart","Orlando","Keith","Marion","Marshall","Noel","Everett","Romeo","Sebastian","Stefan","Robin","Clarence","Sandy","Ernest","Samuel","Benjamin","Luka","Fred","Albert","Greyson","Terry","Cedric","Joe","Paul","George","Bruce","Christopher","Mark","Ron","Craig","Philip","Jimmy","Arthur","Jaime","Perry","Harold","Jerry","Shawn","Walter"]
author_lastNames_seq = ["Smith","Johnson","Williams","Brown","Jones","García","Miller","Davis","Rodríguez","Martínez","Hernández","López","González","Wilson","Anderson","Thomas","Taylor","Moore","Jackson","Martin","Lee","Pérez","Thompson","White","Harris","Sánchez","Clark","Ramírez","Lewis","Robinson","Walker","Young","Allen","King","Wright","Scott","Torres","Nguyen","Hill","Flores","Green","Adams","Nelson","Baker","Hall","Rivera","Campbell","Mitchell","Carter","Roberts","Gómez","Phillips","Evans","Turner","Parker"]
book_names_seq = ["Duchess With Pride","Changeling Of The Gods","Traitors Without Time","Trees Of Wood","Strangers And Enemies","Enemies And Wives","Ruination With A Goal","Limit Of Gold","Eliminating The Dark","Eliminating The City","Criminal With Gold","Man Of The Forsaken","Turtles Of Silver","Serpents Of The Mountain","Phantoms And Wolves","Witches And Agents","Completion With Immortality","Fortune Of Wind","Temptations In The Forest","Driving Into The Mines","Opponent Of Utopia","Goddess Of The End","Snakes Of Dusk","Pirates Of Rainbows","Guardians And Swindlers","Girls And Officers","Strife With Strength","Element With Sins","Traces In The Depths","Question Time","Emperor Without A Conscience","Assassin Of Nightmares","Enemies Of Tomorrow","Swindlers Without Hate","Knights And Fish","Gangsters And Cats","Misfortune Of Water","Ruination Of The Forest","Hiding The Emperor","Write About Dreams","Bandit Of Freedom","Stranger Of The North","Enemies Of My Imagination","Doctors Without A Home","Traitors And Trees","Heroes And Girls","Culmination Of Insanity","Murder Of Eternity","Clinging To My Home","Memory Of The Sea"]
book_number_seq =["I","II","III","IV","V","VI","VII","VIII","IX","X"]

# seed random number generator
seed(1)

books = []

# Populate list of books
for i in range(books_cnt):
    book = Book(
    i,
    choice(book_names_seq) + " " + choice(book_number_seq),
    choice(isbn_seq),
    choice(pages_seq),
    choice(issued_seq),
    choice(author_names_seq) + " " + choice(author_lastNames_seq),
    choice(published_years_seq))

    books.append(book.to_dict())

#myFunctions.save_books(books)

for book in books:
        books_db.insert_one(book)
