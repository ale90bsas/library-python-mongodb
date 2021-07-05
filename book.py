class Book:
    def __init__(self,id,name,isbn,page_count,issued,author,year):
        self.id = id
        self.name = name
        self.isbn = isbn
        self.page_count = page_count
        self.issued = issued
        self.author = author
        self.year = year

    
    
    def doIssue(self):
        self.issued = True
    
    def doReturn(self):
        self.issued = False

    def to_dict(self):
        
        return {

            "id" : self.id,
            "name" : self.name,
            "isbn" : self.isbn,
            "page_count" : self.page_count,
            "issued" : self.issued,
            "author" : self.author,
            "year"  : self.year


        }

#book = Book(1,"Book Name", 12345,200,2003,"John Doe", 2021)
#print(book.to_dict())