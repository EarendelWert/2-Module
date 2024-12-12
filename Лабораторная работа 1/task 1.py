# TODO Написать 3 класса с документацией и аннотацией типов

import doctest

class Tree:
    def __init__(self, species: str, height: float, age: int):
        """
        Создание и подготовка к работе объекта "Дерево".

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

    def grow(self, years: int) -> None:
        """
        Увеличение высоты дерева за определенное количество лет.

        :param years: Количество лет для роста
        :raise ValueError: Если количество лет не положительное

        Примеры:
        >>> tree = Tree("Birch", 10.0, 20)
        >>> tree.grow(5)
        >>> tree.height
        12.5
        """
        if years <= 0:
            raise ValueError("Количество лет должно быть положительным числом.")
        self.height += years * 0.5  # Дерево растет на 0.5 метра в год
        self.age += years

    def add_fruit(self, fruit: str) -> None:
        """
        Добавление плода на дерево.

        :param fruit: Название плода

        Примеры:
        >>> tree = Tree("Birch", 10.0, 20)
        >>> tree.add_fruit("Apple")
        >>> tree.fruits
        ['Apple']
        """
        self.fruits.append(fruit)

    def harvest_fruits(self) -> list:
        """
        Сбор всех плодов с дерева.

        :return: Список собранных плодов

        Примеры:
        >>> tree = Tree("Birch", 10.0, 20)
        >>> tree.add_fruit("Apple")
        >>> tree.add_fruit("Pear")
        >>> tree.harvest_fruits()
        ['Apple', 'Pear']
        >>> tree.fruits  # После сбора плодов список должен быть пустым
        []
        """
        harvested = self.fruits.copy()
        self.fruits.clear()
        return harvested


class Table:
    def __init__(self, material: str, height: float, width: float):
        """
        Создание и подготовка к работе объекта "Стол".

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

    def place_item(self, item: str) -> None:
        """
        Положить предмет на стол.

        :param item: Название предмета

        Примеры:
        >>> table = Table("wood", 75.0, 120.0)
        >>> table.place_item("Book")
        >>> table.items
        ['Book']
        """
        self.items.append(item)

    def clear_table(self) -> None:
        """
        Очистить стол от всех предметов.

        Примеры:
        >>> table = Table("wood", 75.0, 120.0)
        >>> table.place_item("Book")
        >>> table.clear_table()
        >>> table.items
        []
        """
        self.items.clear()


class YouTube:
    def __init__(self, name: str, user_count: int):
        """
        Создание и подготовка к работе объекта "Канал на YouTube".

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
        """
        Загрузить видео на канал.

        :param title: Название видео
        :return: Сообщение о загрузке видео

        Примеры:
        >>> youtube_channel = YouTube("Channel", 1000000)
        >>> youtube_channel.upload_video("My First Video")
        'Видео под названием 'My First Video' загружено на Channel.'
        """
        return f"Видео под названием '{title}' загружено на {self.name}."

    def subscribe(self) -> None:
        """
        Подписаться на канал. Увеличивает количество подписчиков на 1.

        Примеры:
        >>> youtube_channel = YouTube("Channel", 1000000)
        >>> youtube_channel.subscribe()
        >>> youtube_channel.user_count
        1000001
        """
        self.user_count += 1


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
