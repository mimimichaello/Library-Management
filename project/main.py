from book import Book
from library import Library


def main():
    library = Library('library.json')

    while True:
        print("Меню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания книги: ")
            book = Book(title, author, year)
            library.add_book(book)
        elif choice == "2":
            book_id = int(input("Введите ID книги для удаления: "))
            library.delete_book(book_id)
        elif choice == "3":
            query = input("Введите запрос для поиска книги(Название, Автор или Год): ")
            results = library.search_book(query)
            if results:
                for book in results:
                    print(book)
            else:
                print("Книга не найдена")
        elif choice == "4":
            library.display_books()
        elif choice == "5":
            book_id = int(input("Введите ID книги для изменения статуса: "))
            status = input("Введите новый статус книги (в наличии или выдана): ")
            library.change_status(book_id, status)
        elif choice == "6":
            break
        else:
            print("Неправильный выбор")

if __name__ == "__main__":
    main()
