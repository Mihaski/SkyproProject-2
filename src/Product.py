class Product:
    """Моделька продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: float):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, dict_params: dict, list_products: list[Product]) -> Product:
        """Создает новый товар или увеличивает количество."""
        new_product = cls(**dict_params)
        return new_product
