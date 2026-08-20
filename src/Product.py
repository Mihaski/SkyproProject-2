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

        for product in list_products:
            if product.name.lower() == new_product.name.lower():
                product.quantity += new_product.quantity
                product.price = max(product.price, new_product.price)
                return product

        return new_product
