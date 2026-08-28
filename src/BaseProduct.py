from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый абстрактный класс для всех продуктов"""

    def __init__(self, name: str, description: str, price: float, quantity: float):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value
