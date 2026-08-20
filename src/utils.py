import json

from src.Product import Product
from src.Category import Category


def load_data_from_json(file_path: str = "data/products.json") -> list[Category]:
    try:
        with open(file_path, encoding="utf-8") as file:
            data = json.load(file)

        categories = []

        for category_data in data:
            products = []

            for product_data in category_data["products"]:
                product = Product.new_product(product_data)
                products.append(product)

            category = Category(category_data["name"], category_data["description"], products)

            categories.append(category)

        return categories

    except FileNotFoundError as e:
        print(f"Файл не найден: {e}")
        return []
