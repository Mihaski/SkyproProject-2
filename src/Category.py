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

    def add_product(self, product: Product):
        """Добавляет товар в категорию."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """геттер для списка продуктов"""
        result = []
        for product in self.__products:
            result.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return str(result)

