class VideoGame:
    """
    Базовый класс для всех видеоигр.
    """
    def __init__(self, title: str, genre: str, release_year: int, platforms: list) -> None:
        """
        Инициализация видеоигры.
        :param title: Название видеоигры.
        :param genre: Жанр видеоигры.
        :param release_year: Год выпуска видеоигры.
        :param platforms: Список платформ, на которых доступна игра.
        """
        self.__title = title  # Инкапсуляция, чтобы предотвратить изменение названия извне
        self.__genre = genre  # Инкапсуляция, чтобы предотвратить изменение жанра извне
        self.release_year = release_year
        self.platforms = platforms  # Список платформ, на которых доступна игра

    def start_game(self) -> str:
        """
        Запуск видеоигры.
        """
        return f"Запускается игра: {self.__title}."

    def add_platform(self, platform: str) -> None:
        """
        Добавление платформы, на которой доступна игра.
        """
        self.platforms.append(platform)

    def __str__(self) -> str:
        """
        Строковое представление видеоигры.
        """
        return f"{self.__title} ({self.release_year}) - Жанр: {self.__genre}; Платформы: {', '.join(self.platforms)}"

    def __repr__(self) -> str:
        """
        Официальное строковое представление видеоигры.
        """
        return f"VideoGame(title='{self.__title}'; genre='{self.__genre}'; release_year={self.release_year}; platforms={self.platforms})"


class ActionGame(VideoGame):
    """
    Класс для экшен-игр, дочерний от видеоигры.
    """
    def __init__(self, title: str, release_year: int, multiplayer: bool, platforms = list) -> None:
        """
        Инициализация экшен-игры.
        :param title: Название экшен-игры.
        :param release_year: Год выпуска экшен-игры.
        :param multiplayer: Наличие многопользовательского режима.
        :param platforms: Список платформ, на которых доступна игра.
        """
        super().__init__(title, "Экшен", release_year, platforms)  # Вызов конструктора базового класса
        self.multiplayer = multiplayer

    def start_game(self) -> str:
        """
        Запуск экшен-игры.
        """
        mode = "многопользовательский" if self.multiplayer else "однопользовательский"
        return f"{super().start_game()} Это {mode} режим."

    def __str__(self) -> str:
        """
        Строковое представление экшен-игры.
        """
        return f"{super().__str__()}; Многопользовательский режим: {self.multiplayer}"

    def __repr__(self) -> str:
        """
        Официальное строковое представление экшен-игры.
        """
        return f"ActionGame(title='{self._VideoGame__title}'; release_year={self.release_year}; multiplayer={self.multiplayer}; platforms={self.platforms})"


class RPG(VideoGame):
    """
    Класс для ролевых игр, дочерний от видеоигры.
    """
    def __init__(self, title: str, release_year: int, character_classes: list, platforms: list) -> None:
        """
        Инициализация ролевой игры.
        :param title: Название ролевой игры.
        :param release_year: Год выпуска ролевой игры.
        :param character_classes: Список классов персонажей в игре.
        :param platforms: Список платформ, на которых доступна игра.
        """
        super().__init__(title, "Ролевая игра", release_year, platforms)  # Вызов конструктора базового класса
        self.__character_classes = character_classes  # Инкапсуляция, чтобы предотвратить изменение классов извне

    def start_game(self) -> str:
        """
        Запуск ролевой игры.
        """
        return f"{super().start_game()}"

    def get_character_classes(self) -> list:
        """
        Получить доступные классы персонажей.
        """
        return self.__character_classes

    def __str__(self) -> str:
        """
        Строковое представление ролевой игры.
        """
        return f"{super().__str__()}; Доступные классы: {', '.join(self.__character_classes)}"

    def __repr__(self) -> str:
        """
        Официальное строковое представление ролевой игры.
        """
        return f"RPG(title='{self._VideoGame__title}'; release_year={self.release_year}; character_classes={self.__character_classes}; platforms={self.platforms})"


# Пример использования:
action_game = ActionGame("Call of Duty", 2021, True, ["PC", "PS5", "Xbox One"])
print(action_game.start_game()) # Запускается игра: Call of Duty. Это многопользовательский режим.
print(action_game) # Call of Duty (2021) - Жанр: Экшен; Платформы: PC, PS5, Xbox One; Многопользовательский режим: True

role_playing_game = RPG("Baldur's gate 3", 2023, ["Маг", "Воин", "Лучник"], ["PC", "PS5", "Xbox One"])
print(role_playing_game.start_game()) # Запускается игра: Baldur's gate 3.
print(role_playing_game) # Baldur's gate 3 (2023) - Жанр: Ролевая игра; Платформы: PC, PS5, Xbox One; Доступные классы: Маг, Воин, Лучник