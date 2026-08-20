from src.Product import Product


class Category:
    """Моделька категорий"""

    # Атрибуты
    category_count = 0
    product_count = 0

    def __init__(self, name_category: str, description_category: str, list_products: list[Product]):
        self.name = name_category
        self.description = description_category
        self.__products = list_products
        Category.category_count += 1
        Category.product_count += len(self.__products)


    def add_product(self, product: Product) -> None:
        """Добавляет товар в категорию."""
        self.__products.append(product)
        Category.product_count += 1
