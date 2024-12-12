# TODO Написать 3 класса с документацией и аннотацией типов

import doctest

class Tree:
    def __init__(self, species: str, height: float, age: int):
        """

        :param species: Вид дерева
        :param height: Высота дерева в метрах
        :param age: Возраст дерева в годах

        Примеры:
        >>> tree = Tree("Birch", 10.0, 20)
        >>> tree.species
        'Birch'
        >>> tree.height
        10.0
        >>> tree.age
        20
        """
        if not isinstance(species, str):
            raise TypeError("Вид должен быть строкой")
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")

        self.species = species
        self.height = height
        self.age = age
        self.fruits = []  # Список плодов на дереве

    def grow(self, years: int) -> str:
        """Увеличение высоты дерева за определенное количество лет."""
        if years <= 0:
            return "Количество лет должно быть положительным числом."
        self.height += years * 0.5  # Предположим, что дерево растет на 0.5 метра в год
        self.age += years
        return f"Дерево {self.species} выросло на {self.height:.2f} метров высоту и сейчас ему {self.age} год(лет)."

    def add_fruit(self, fruit: str) -> str:
        """Добавить плод на дерево."""
        self.fruits.append(fruit)
        return f"На дереве {self.species} выросло {fruit}."

    def harvest_fruits(self) -> str:
        """Собрать все плоды с дерева."""
        if not self.fruits:
            return "На дереве нет плодов."
        harvested = ', '.join(self.fruits)
        self.fruits.clear()
        return f"Собранные фрукты: {harvested}."


class Table:
    def __init__(self, material: str, height: float, width: float):
        """

        :param material: Материал стола
        :param height: Высота стола в сантиметрах
        :param width: Ширина стола в сантиметрах

        Примеры:
        >>> table = Table("metal", 75.0, 120.0)
        >>> table.material
        'metal'
        >>> table.height
        75.0
        >>> table.width
        120.0
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой")
        if height <= 0 or width <= 0:
            raise ValueError("Высота и ширина должны быть положительными числами")

        self.material = material
        self.height = height
        self.width = width
        self.items = []  # Список предметов на столе

    def place_item(self, item: str) -> str:
        """Положить предмет на стол."""
        self.items.append(item)
        return f"Предмет {item} был помещен на {self.material} стол."

    def clear_table(self) -> str:
        """Очистить стол от всех предметов."""
        if not self.items:
            return "Стол пустой."
        self.items.clear()
        return "Стол теперь чистый."


class YouTube:
    def __init__(self, name: str, user_count: int):
        """

        :param name: Название канала на YouTube
        :param user_count: Количество подписчиков

        Примеры:
        >>> youtube_channel = YouTube("Channel", 1000000)
        >>> youtube_channel.name
        'Channel'
        >>> youtube_channel.user_count
        1000000
        """
        if not isinstance(name, str):
            raise TypeError("Название должно быть строкой")
        if user_count < 0:
            raise ValueError("Количество подписчиков должно быть неотрицательным")

        self.name = name
        self.user_count = user_count

    def upload_video(self, title: str) -> str:
        """Загрузить видео на канал."""
        return f"Видео под названием '{title}' загружено на {self.name}."

    def subscribe(self, subscriber_name: str) -> str:
        """Подписаться на канал."""
        self.user_count += 1
        return f"{subscriber_name} подписался на канал {self.name}."


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации