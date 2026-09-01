from src.BaseOrderCategory import BaseOrderCategory
from src.OrderAddException import OrderAddException
from src.Product import Product


class Category(BaseOrderCategory):
    """Моделька категорий"""

    # Атрибуты
    category_count = 0
    product_count = 0

    def __init__(self, name_category: str, description_category: str, products: list[Product]):
        """Метод для инициализации экземпляра класса. Задаем значения свойствам экземпляра."""
        self.name = name_category
        self.description = description_category
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        total_count_products = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_count_products} шт."

    def add_product(self, product: Product):
        """Добавляет товар в категорию."""
        try:
            if product.quantity == 0:
                raise OrderAddException("Нельзя добавить товар с нулевым количеством.")

            if isinstance(product, Product):
                self.__products.append(product)
                Category.product_count += 1

        except OrderAddException as e:
            print(e)

        else:
            print("Товар успешно добавлен.")

        finally:
            print("Обработка добавления товара завершена.")

    @property
    def products(self) -> list[Product]:
        return self.__products

    def middle_price(self):
        try:
            average_cost = 0
            count = 0
            for product in self.__products:
                count += 1
                average_cost += product.price
            return average_cost / count
        except ZeroDivisionError:
            return 0
