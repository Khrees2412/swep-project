import datetime

dt = datetime.datetime.today()
year = dt.year
_month = dt.month
day = dt.day


print("Welcome to the Lautech Student library.\n What operation would you like to perform today?")
print("    ")
op_code = int(input(" * Select 1 to find a match for a book \n * Select 2 to store a new book in the library: " ))


lib_books = [
    {
    "title": "Lion King",
    "author": "Christian Ndu",
    "isbn":129383,
    "date_published":"25-01-2022",
    "color":"Red",
    "topic": "Action"
},
{
    "title": "Love in the air",
    "author": "Romeo Fonte",
    "isbn":111290,
    "date_published":"24-10-1997",
    "color":"Blue",
    "topic": "Romance"

},
{
    "title": "How to create a blockchain",
    "author": "Satoshi Nakamoto",
    "isbn":287292,
    "date_published":"03-01-2009",
    "color":"Orange",
    "topic": "Cryptocurrency"

}]

def store_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author's name: ")
    isbn  = int(input("Enter the book's isbn: "))
    date_published = "{0}-{1}-{2}".format(day,_month,year)
    color = input("Enter the color of the book: ")
    topic = input("Enter the topic of the book: ")

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "date_published": date_published,
        "color":color,
        "topic": topic
    }
    for item in lib_books:
        if item["isbn"] == book["isbn"]:
            print("Book already exists in the library")
            print(lib_books)
        else:
            lib_books.append(book)
            print("Book has been published to the library")
            print(lib_books)

def findMatch():
    print("Enter your identifier, select one of (color, author, date)")
    selection = ""
    code = int(input("Enter: \n 1 for color \n 2 for author \n 3 for date_published: "))
    if code == 1: 
            selection = "color"
    elif code == 2:
            selection = "author"
    elif code == 3:
            selection = "date_published"
    else: 
        print("Invalid operation code")

    sel = input("What is the {0} for the book you need: ".format(selection))

    for book in lib_books:
        if book[selection] == sel:
            print("Book found in the library")
            print(book)

if op_code == 1:
    findMatch()
elif op_code == 2:
    store_book()

# input()