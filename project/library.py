import json
import os

from book import Book


class Library:
    """
    Класс для работы с библиотекой книг.
    """
    def __init__(self, filename):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        """
        Загрузка книг из файла JSON.
        """
        try:
            if os.path.exists(self.filename):
                with open(self.filename, "r") as f:
                    return [Book(**book) for book in json.load(f)]
            else:
                return []
        except Exception as e:
            print(f"Ошибка загрузки книг: {e}")
            return []

    def save_books(self):
        """
        Сохранение книг в файл JSON.
        """
        try:
            with open(self.filename, "w") as f:
                json.dump([book.__dict__ for book in self.books], f, indent=4)
        except Exception as e:
            print(f"Ошибка сохранения книг: {e}")

    def add_book(self, book):
        """
        Добавление новой книги в библиотеку.
        """
        try:
            book.id = len(self.books) + 1
            self.books.append(book)
            self.save_books()
        except Exception as e:
            print(f"Ошибка добавления книги: {e}")

    def delete_book(self, book_id):
        """
        Удаление книги из библиотеки по идентификатору.
        """
        try:
            for book in self.books:
                if book.id == book_id:
                    self.books.remove(book)
                    self.save_books()
                    return
        except Exception as e:
            print(f"Ошибка удаления книги: {e}")

    def search_book(self, query):
        """
        Поиск книги в библиотеке по запросу.
        """
        try:
            results = []
            for book in self.books:
                if query in book.title or query in book.author or query in str(book.year):
                    results.append(book)
                else:
                    print("Книга не найдена")
            return results
        except Exception as e:
            print(f"Ошибка поиска книги: {e}")
            return []

    def display_books(self):
        """
        Отображение всех книг в библиотеке.
        """
        try:
            for book in self.books:
                print(book)

        except Exception as e:
            print(f"Ошибка отображения книг: {e}")

    def change_status(self, book_id, status):
        """
        Изменение статуса книги в библиотеке.
        """
        try:
            for book in self.books:
                if book.id == book_id:
                    book.status = status
                    self.save_books()
                    return
            print("Книга не найдена")
        except Exception as e:
            print(f"Ошибка изменения статуса книги: {e}")
