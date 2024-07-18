class Book:
    """
    Класс для описания книги.
    """
    def __init__(self, title, author, year):
        self.id = None
        self.title = title
        self.author = author
        self.year = year
        self.status = "в наличии"

    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}, Author: {self.author}, Year: {self.year}, Status: {self.status}"
