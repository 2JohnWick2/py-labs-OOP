# TODO: описать базовый класс
from typing import Union


class Vehicle:
    """
    Базовый класс для транспортных средств.
    """

    def __init__(self, brand: str, model: str, year: int):
        """
        Инициализирует объект транспортного средства.

        :param brand: Марка транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.
        """
        self._brand = brand  # Инкапсуляция для предотвращения изменения марки напрямую
        self._model = model  # Инкапсуляция модели для контроля корректности значений
        self.year = year

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        :return: Строка с описанием транспортного средства.
        """
        return f"{self._brand} {self._model} ({self.year})"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление для отладки.

        :return: Строка с атрибутами объекта.
        """
        return f"Транспортное средство(марка='{self._brand}', модель='{self._model}', год={self.year})"

    def start_engine(self) -> str:
        """
        Симулирует запуск двигателя.

        :return: Сообщение о запуске двигателя.
        """
        return f"Двигатель {self._brand} {self._model} теперь запущен."


# TODO: описать дочерний класс
class Car(Vehicle):
    """
    Дочерний класс для легковых автомобилей.
    """

    def __init__(self, brand: str, model: str, year: int, seats: int):
        """
        Инициализирует объект легкового автомобиля.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        :param seats: Количество мест в автомобиле.
        """
        super().__init__(brand, model, year)
        self.seats = seats

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        :return: Строка с описанием легкового автомобиля.
        """
        return f"{self._brand} {self._model} ({self.year}), Seats: {self.seats}"

    def start_engine(self) -> str:
        """
        Перегружает метод базового класса, добавляя информацию о типе транспортного средства.

        Причина перегрузки: необходимо уточнить, что двигатель запускается именно у легкового автомобиля.

        :return: Сообщение о запуске двигателя.
        """
        return f"Двигатель автомобиля {self._brand} {self._model} теперь запущен."

    def fold_seats(self) -> str:
        """
        Симулирует складывание сидений в автомобиле.

        :return: Сообщение о выполнении действия.
        """
        return f"Сидения в {self._brand} {self._model} теперь сложены."


if __name__ == "__main__":
    vehicle = Vehicle("GenericBrand", "GenericModel", 2000)
    print(vehicle)
    print(vehicle.start_engine())

    car = Car("Toyota", "Corolla", 2022, 5)
    print(car)
    print(car.start_engine())
    print(car.fold_seats())
