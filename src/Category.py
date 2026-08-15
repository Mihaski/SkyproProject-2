from Product import Product


class Category:
    """Моделька категорий"""
    # Атрибуты
    category_count = 0
    product_count = 0

    def __init__(self, name_category: str, description_category: str, list_categories: list[Product]):
        self.name = name_category
        self.description = description_category
        self.products = list_categories
        Category.category_count += 1
        Category.product_count += len(self.products)
