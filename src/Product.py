class Product:
    """Моделька продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: float):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is not type(self):
            raise TypeError("Можно складывать товары только одного класса\\подкласса")
        return self.price * self.quantity + other.price * other.quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value):
        if 0 < value:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, dict_params: dict, products=None) -> Product:
        """Создает новый товар или увеличивает количество."""
        if products is None:
            products = []
        new_product = cls(**dict_params)

        for product in products:
            if product.name.lower() == new_product.name.lower():
                product.quantity += new_product.quantity
                product.price = max(product.price, new_product.price)
                return product

        return new_product
