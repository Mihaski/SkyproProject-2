from src.BaseOrderCategory import BaseOrderCategory


class OrderProduct(BaseOrderCategory):
    """ссылка на то, какой товар был куплен, количество купленного товара, а также итоговая стоимость.
    Только один товар."""

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.total_price = self.__str__()

    def __str__(self):
        return f"{self.product.price * self.quantity}"
