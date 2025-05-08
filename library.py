import json
import os
import csv

data_file = "library.txt"

def load_library():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    return []

def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file, indent=4)

def add_book(library):
    title = input('Enter the title of the book: ')
    author = input('Enter the author of the book: ')           
    year = input('Enter the year of the book: ')           
    genre = input('Enter the genre of the book: ')           
    read = input('Have you read the book? (yes/no): ').lower() == 'yes'

    new_book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }

    library.append(new_book)
    save_library(library)
    print(f'Book "{title}" added successfully.')

def remove_book(library):
    title = input("Enter the title of the book to remove from the library: ").lower()
    initial_length = len(library)
    library[:] = [book for book in library if book['title'].lower() != title]
    
    if len(library) < initial_length:
        save_library(library)
        print(f'Book "{title}" removed successfully.')
    else:
        print(f'Book "{title}" not found in the library.')

def update_book(library):
    title = input("Enter the title of the book you want to update: ").lower()
    for book in library:
        if book['title'].lower() == title:
            print("Leave a field blank to keep it unchanged.")
            new_title = input(f"New title (current: {book['title']}): ") or book['title']
            new_author = input(f"New author (current: {book['author']}): ") or book['author']
            new_year = input(f"New year (current: {book['year']}): ") or book['year']
            new_genre = input(f"New genre (current: {book['genre']}): ") or book['genre']
            read_input = input(f"Have you read it? (yes/no, current: {'yes' if book['read'] else 'no'}): ").lower()
            new_read = book['read'] if read_input == '' else (read_input == 'yes')

            book.update({
                'title': new_title,
                'author': new_author,
                'year': new_year,
                'genre': new_genre,
                'read': new_read
            })

            save_library(library)
            print("Book updated successfully.")
            return
    print("Book not found.")

def search_library(library):
    search_by = input("Search by title or author: ").lower()
    if search_by not in ['title', 'author']:
        print("Invalid search field. Please search by 'title' or 'author'.")
        return

    search_term = input(f"Enter the {search_by}: ").lower()
    results = [book for book in library if search_term in book[search_by].lower()]

    if results:
        for book in results:
            status = 'Read' if book['read'] else "Unread"
            print(f"{book['title']} by {book['author']} | {book['year']} | {book['genre']} | {status}")
    else:
        print(f"No book found matching '{search_term}' in the {search_by} field.")

def display_all_books(library):
    if library:
        for book in library:
            status = 'Read' if book['read'] else "Unread"
            print(f"{book['title']} by {book['author']} | {book['year']} | {book['genre']} | {status}")
    else:
        print("The library is empty.")

def display_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book['read'])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

    print(f"Total books: {total_books}")
    print(f"Books read: {read_books}")
    print(f"Percentage read: {percentage_read:.2f}%")

def sort_books(library):
    sort_by = input("Sort books by title, author, or year: ").lower()
    if sort_by not in ['title', 'author', 'year']:
        print("Invalid sort field.")
        return

    sorted_library = sorted(library, key=lambda x: x[sort_by])
    print(f"\nBooks sorted by {sort_by}:")
    display_all_books(sorted_library)

def export_to_csv(library):
    csv_file = "library_export.csv"
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["title", "author", "year", "genre", "read"])
        writer.writeheader()
        writer.writerows(library)
    print(f"Library exported to {csv_file}")

def main():
    library = load_library()
    while True:
        print("\nMenu")
        print("1. Add a book") 
        print("2. Remove a book") 
        print("3. Update a book")
        print("4. Search the library") 
        print("5. Display all books") 
        print("6. Display statistics") 
        print("7. Sort books")
        print("8. Export library to CSV")
        print("9. Exit") 

        choice = input("Enter your choice: ")
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            update_book(library)
        elif choice == '4':
            search_library(library)
        elif choice == '5':
            display_all_books(library)
        elif choice == '6':
            display_statistics(library)
        elif choice == '7':
            sort_books(library)
        elif choice == '8':
            export_to_csv(library)
        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
