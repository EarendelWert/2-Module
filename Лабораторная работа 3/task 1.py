class Book:
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self._pages = value

    def __str__(self):
        return f"Книга {self.name} (бумажная). Автор {self.author}, страниц: {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (float, int)):
            raise TypeError("Продолжительность должна быть числом.")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = float(value)

    def __str__(self):
        return f"Книга {self.name} (аудио). Автор {self.author}, продолжительность: {self.duration} часов"


# Примеры использования
paper_book = PaperBook("Типичный случай","Виктор Стариков", 189)
audio_book = AudioBook("1984", "Джордж Оруэлл", 11.5)

print(paper_book)
print(audio_book)

# Проверка свойств
try:
    paper_book.pages = -50
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    audio_book.duration = "девять часов"
except TypeError as e:
    print(f"Ошибка: {e}")
