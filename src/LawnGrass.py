from src.Product import Product


class LawnGrass(Product):
    """Моделька продукта газонная трава"""

    def __init__(self,
                 name: str,
                 description: str,
                 price: float,
                 quantity,
                 country: str,
                 germination_period: str,
                 color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
