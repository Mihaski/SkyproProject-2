from src.BaseOrderCategory import BaseOrderCategory
from src.OrderAddException import OrderAddException


class OrderProduct(BaseOrderCategory):
    """ссылка на то, какой товар был куплен, количество купленного товара, а также итоговая стоимость.
    Только один товар."""

    def __init__(self, product, quantity):

        try:
            if quantity == 0:
                raise OrderAddException("Нельзя добавить товар в заказ с нулевым количеством.")

            self.product = product
            self.quantity = quantity
            self.total_price = self.__str__()

        except OrderAddException as e:
            print(e)

        else:
            print("Товар успешно добавлен в заказ.")

        finally:
            print("Обработка добавления товара в заказ завершена.")

    def __str__(self):
        return f"{self.product.price * self.quantity}"
