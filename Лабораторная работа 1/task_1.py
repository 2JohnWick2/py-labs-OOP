# TODO: Подробно описать три произвольных класса
import doctest

# TODO: описать класс


class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Инициализация книги с названием, автором и количеством страниц.

        :param title: Название книги (строка)
        :param author: Автор книги (строка)
        :param pages: Количество страниц в книге (положительное целое число)

        :Example:
        >>> book = Book("1984", "Джордж Оруэлл", 300)
        """
        self.title = title
        self.author = author
        self.set_pages(pages)

    def set_pages(self, pages: int) -> int:
        """
        Устанавливает количество страниц в книге с валидацией.

        :param pages: Количество страниц в книге.
        :raises ValueError: Если количество страниц меньше или равно нулю.

        :Example:
        >>> book = Book("1984", "Джордж Оруэлл", 300)
        >>> book.set_pages(400)
        >>> book.pages
        400
        """
        if pages <= 0:
            raise ValueError(
                "Количество страниц должно быть положительным числом")
        self.pages = pages

    def read(self, pages_read: int = 1) -> int:
        """
        Читаем определенное количество страниц в книге.

        :param pages_read: Количество страниц, которые вы хотите прочитать.
        :raises ValueError: Если количество страниц для чтения больше, чем доступное количество.
        :return: Количество оставшихся страниц в книге.

        :Example:
        >>> book = Book("1984", "Джордж Оруэлл", 300)
        >>> book.read(50)
        250
        """
        if not isinstance(pages_read, int) or pages_read < 0:
            raise ValueError(
                "Количество страниц для чтения не может быть отрицательным")
        if pages_read > self.pages:
            raise ValueError(
                "Невозможно прочитать больше страниц, чем есть в книге")
        self.pages -= pages_read
        return self.pages

    def get_info(self) -> str:
        """
        Получить информацию о книге.

        :return: Информация о книге в формате строки.
        :rtype: str

        :Example:
        >>> book = Book("1984", "Джордж Оруэлл", 300)
        >>> book.get_info()
        'Название: 1984, Автор: Джордж Оруэлл, Страниц: 300'
        """
        return f"Название: {self.title}, Автор: {self.author}, Страниц: {self.pages}"


# TODO: описать ещё класс


class Tree:
    def __init__(self, species: str, height: float, age: int):
        """
        Инициализация дерева с видом, высотой и возрастом.

        :param species: Вид дерева (например, "ель", "дуб")
        :param height: Высота дерева в метрах (положительное число)
        :param age: Возраст дерева в годах (положительное целое число)
        """
        self.species = species
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: float) -> int:
        """
        Устанавливает высоту дерева с валидацией.

        :param height: Высота дерева в метрах.
        :raises ValueError: Если высота меньше или равна нулю.

        :Example:
        >>> tree = Tree("ель", 5, 10)
        >>> tree.set_height(7)
        >>> tree.height
        7
        """
        if not isinstance(height, (int, float)) or height < 0:
            raise ValueError("Высота дерева должна быть положительным числом")
        self.height = height

    def set_age(self, age: int) -> int:
        """
        Устанавливает возраст дерева с валидацией.

        :param age: Возраст дерева в годах.
        :raises ValueError: Если возраст меньше или равен нулю.

        :Example:
        >>> tree = Tree("дуб", 10, 20)
        >>> tree.set_age(25)
        >>> tree.age
        25
        """
        if age <= 0:
            raise ValueError("Возраст дерева должен быть положительным числом")
        self.age = age

    def grow(self, years: int = 1) -> None:
        """
        Увеличивает высоту дерева на заданное количество лет.

        :param years: Количество лет роста дерева. По умолчанию 1 год.
        :raises ValueError: Если количество лет не положительное.
        :return: None



        :Example:
        >>> tree = Tree("ель", 5, 10)
        >>> tree.grow(2)
        >>> tree.height
        6.0
        """
        if years <= 0:
            raise ValueError(
                "Количество лет роста должно быть положительным числом")
        self.height += years * 0.5  # Дерево растет на 0.5 метра в год


# TODO: и ещё один


class Car:
    """
    Класс, описывающий автомобиль.
    """

    def __init__(self, brand: str, year: int, mileage: float):
        """
        Инициализация объекта класса Car.

        :param brand (str): Марка автомобиля (не может быть пустой строкой).
        :param year (int): Год выпуска автомобиля (должен быть положительным числом).
        :param mileage (float): Пробег автомобиля (не может быть отрицательным).

        :raises ValueError: Если марка пуста, год выпуска не положителен или пробег отрицательный.
        """
        if not brand:
            raise ValueError("Марка автомобиля не может быть пустой.")
        if year <= 0:
            raise ValueError(
                "Год выпуска автомобиля должен быть положительным.")
        if mileage < 0:
            raise ValueError("Пробег автомобиля не может быть отрицательным.")

        self.brand = brand
        self.year = year
        self.mileage = mileage

    def drive(self, distance: float) -> None:
        """
        Проехать заданное расстояние, увеличивая пробег автомобиля.

        :param distance: Расстояние, которое автомобиль проедет. Должно быть больше 0.

        :raises ValueError: Если distance <= 0.

        Пример:
        >>> c = Car("Toyota", 2010, 50000)
        >>> c.drive(150)
        >>> c.mileage
        50150
        """
        if distance <= 0:
            raise ValueError("Расстояние должно быть положительным числом.")
        self.mileage += distance

    def calculate_age(self, current_year: int) -> int:
        """
        Рассчитать возраст автомобиля.

        :param current_year: Текущий год (должен быть больше или равен году выпуска).

        :raises ValueError: Если текущий год меньше года выпуска автомобиля.

        Returns:
            int: Возраст автомобиля в годах.

        Пример:
        >>> c = Car("Honda", 2000, 100000)
        >>> c.calculate_age(2020)
        20
        """
        if current_year < self.year:
            raise ValueError(
                "Текущий год не может быть меньше года выпуска автомобиля.")
        return current_year - self.year

    def tune_up(self, factor: float = 1.1) -> str:
        """
        Произвести сервисное обслуживание (условно), которое улучшит некоторые показатели автомобиля.
        Для примера, допустим, что после обслуживания условно уменьшается пробег пропорционально
        фактору обслуживания (мы представим, что так считаются условные издержки).

        :param factor: Коэффициент обслуживания. Должен быть больше 0.
                       По умолчанию 1.1 (улучшение на 10%).

        :raises ValueError: Если factor <= 0.

        Returns:
            str: Сообщение о выполненном обслуживании.

        Пример:
        >>> c = Car("Ford", 2015, 80000)
        >>> c.tune_up()
        'Обслуживание выполнено, пробег уменьшен с 80000 до 72727.27 км.'
        """
        if factor <= 0:
            raise ValueError("Фактор обслуживания должен быть больше 0.")
        old_mileage = self.mileage
        # Условно уменьшим пробег, чтобы показать улучшения за счет обслуживания.
        # Для примера: новая величина = старый пробег / factor
        self.mileage = old_mileage / factor
        return f"Обслуживание выполнено, пробег уменьшен с {old_mileage} до " f"{self.mileage:.2f} км."


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
