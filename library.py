class Library:
    def __init__(self,book_title,author_name,book_edition):
        self.author_name = author_name
        self.book_title = book_title
        self.book_edition = book_edition
    def getAuthorName(self):
        return self.author_name
    def getBooktitle(self):
        return self.book_title
    def getBookEdition(self):
        return self.book_edition
    def setAuthorName(self,author_name):
        self.author_name = author_name
    def setBooktitle(self,book_title):
        self.book_title = book_title
    def setBookEdition(self,book_edition):
        self.book_edition = book_edition
    

book1 = Library("Introduction to Computer Fundamental","PK Sinha",5)
book2 = Library("Introduction to Algorithms","Thomas H",6)
print("********Digital Libray of DIU: Book List**********\n")
print(f"Book 1: {book1.getBooktitle()} ,Author: {book1.getAuthorName()} , Edition: {book1.getBookEdition()}\n")
print(f"Book 2: {book2.getBooktitle()} ,Author: {book2.getAuthorName()} , Edition: {book2.getBookEdition()}\n")
book1.setBookEdition(6)
book2.setAuthorName("Thomas H. Cormen, Charles E. Leiserson,Ronald L, and Clifford Stein");
print("INFORMATION UPDATED!\n\n")
print("Updated Information:\n")
print(f"Book 1: {book1.getBooktitle()} ,Author: {book1.getAuthorName()} , Edition: {book1.getBookEdition()}\n")
print(f"Book 2: {book2.getBooktitle()} ,Author: {book2.getAuthorName()} , Edition: {book2.getBookEdition()}\n")
