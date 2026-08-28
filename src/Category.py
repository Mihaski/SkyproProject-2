from src.Product import Product


class Category:
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
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1

    @property
    def products(self) -> list[Product]:
        return self.__products
