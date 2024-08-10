import json
import os

class Library:
    def __init__(self, file_name="library_data.json"):
        self.file_name = file_name
        self.books = {}
        self.users = {}
        self.load_data()

    def save_data(self):
        data = {
            "books": self.books,
            "users": self.users,
        }
        with open(self.file_name, 'w') as file:
            json.dump(data, file)
        print("Data saved successfully.")

    def load_data(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                self.books = data.get("books", {})
                self.users = data.get("users", {})
            print("Data loaded successfully.")
        else:
            print("No existing data file found. Starting fresh.")

    def add_book(self, isbn, title, author):
        if isbn not in self.books:
            self.books[isbn] = {"title": title, "author": author, "available": True}
            self.save_data()
            print(f"Book '{title}' by {author} added successfully.")
        else:
            print("Book with this ISBN already exists.")

    def remove_book(self, isbn):
        if isbn in self.books:
            book = self.books.pop(isbn)
            self.save_data()
            print(f"Book '{book['title']}' removed successfully.")
        else:
            print("Book not found.")

    def search_book(self, keyword):
        results = []
        for isbn, book in self.books.items():
            if keyword.lower() in book['title'].lower() or keyword.lower() in book['author'].lower():
                results.append((isbn, book))
        return results

    def check_out_book(self, isbn, user_id):
        if isbn in self.books and user_id in self.users:
            if self.books[isbn]['available']:
                self.books[isbn]['available'] = False
                self.users[user_id]['books'].append(isbn)
                self.save_data()
                print(f"Book '{self.books[isbn]['title']}' checked out successfully.")
            else:
                print("Book is not available for checkout.")
        else:
            print("Book or user not found.")

    def check_in_book(self, isbn, user_id):
        if isbn in self.books and user_id in self.users:
            if isbn in self.users[user_id]['books']:
                self.books[isbn]['available'] = True
                self.users[user_id]['books'].remove(isbn)
                self.save_data()
                print(f"Book '{self.books[isbn]['title']}' checked in successfully.")
            else:
                print("User has not checked out this book.")
        else:
            print("Book or user not found.")

    def register_user(self, user_id, name):
        if user_id not in self.users:
            self.users[user_id] = {"name": name, "books": []}
            self.save_data()
            print(f"User {name} registered successfully.")
        else:
            print("User ID already exists.")

    def unregister_user(self, user_id):
        if user_id in self.users:
            if not self.users[user_id]['books']:
                del self.users[user_id]
                self.save_data()
                print("User unregistered successfully.")
            else:
                print("User still has books checked out. Cannot unregister.")
        else:
            print("User not found.")

def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Check Out Book")
        print("5. Check In Book")
        print("6. Register User")
        print("7. Unregister User")
        print("8. Exit")

        try:
            choice = int(input("Enter your choice (1-8): "))

            if choice == 1:
                isbn = input("Enter ISBN: ")
                title = input("Enter title: ")
                author = input("Enter author: ")
                library.add_book(isbn, title, author)

            elif choice == 2:
                isbn = input("Enter ISBN of book to remove: ")
                library.remove_book(isbn)

            elif choice == 3:
                keyword = input("Enter search keyword: ")
                results = library.search_book(keyword)
                if results:
                    print("Search results:")
                    for isbn, book in results:
                        status = "Available" if book['available'] else "Checked Out"
                        print(f"ISBN: {isbn}, Title: {book['title']}, Author: {book['author']}, Status: {status}")
                else:
                    print("No books found.")

            elif choice == 4:
                isbn = input("Enter ISBN of book to check out: ")
                user_id = input("Enter user ID: ")
                library.check_out_book(isbn, user_id)

            elif choice == 5:
                isbn = input("Enter ISBN of book to check in: ")
                user_id = input("Enter user ID: ")
                library.check_in_book(isbn, user_id)

            elif choice == 6:
                user_id = input("Enter new user ID: ")
                name = input("Enter user name: ")
                library.register_user(user_id, name)

            elif choice == 7:
                user_id = input("Enter user ID to unregister: ")
                library.unregister_user(user_id)

            elif choice == 8:
                print("Thank you for using the Library Management System. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 8.")

        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
