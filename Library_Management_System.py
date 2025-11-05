class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        availability = "Available" if self.available else "Issued"
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {availability}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")

    def display_books(self):
        if not self.books:
            print("No books available.")
        else:
            for book in self.books:
                print(book)

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id and book.available:
                book.available = False 
                print(f"Book '{book.title}' has been issued.")
                return
        print("Sorry, the book is either not available or already issued.")

    def return_book(self, book_id):
        """ Return an issued book """
        for book in self.books:
            if book.book_id == book_id and not book.available:
                book.available = True 
                print(f"Book '{book.title}' has been returned.")
                return
        print("This book was not issued.")

    def search_book(self, keyword):
        """ Search books by title or author """
        found_books = [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
        if found_books:
            for book in found_books:
                print(book)
        else:
            print(f"No books found matching '{keyword}'.")

    def view_issued_books(self):
        issued_books = [book for book in self.books if not book.available]
        if issued_books:
            for book in issued_books:
                print(book)
        else:
            print("No books have been issued.")

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"Book '{book.title}' has been removed from the library.")
                return
        print("Book not found.")

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. View Issued Books")
        print("7. Remove Book")
        print("8. Exit") 

        choice = input("Enter your choice: ")

        if choice == '1':
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            new_book = Book(book_id, title, author)
            library.add_book(new_book)

        elif choice == '2':
            library.display_books()

        elif choice == '3':
            book_id = input("Enter Book ID to issue: ")
            library.issue_book(book_id)

        elif choice == '4':
            book_id = input("Enter Book ID to return: ")
            library.return_book(book_id)

        elif choice == '5':
            keyword = input("Enter title or author to search: ")
            library.search_book(keyword)

        elif choice == '6':
            library.view_issued_books()

        elif choice == '7':
            book_id = input("Enter Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == '8':
            print("Exiting system...")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
