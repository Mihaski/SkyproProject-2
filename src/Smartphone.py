from src.Product import Product


class Smartphone(Product):
    """Моделька продукта смартфон"""

    def __init__(self,
                 name: str,
                 description: str,
                 price: float,
                 quantity: float,
                 efficiency: str,
                 model: str,
                 memory: str,
                 color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
