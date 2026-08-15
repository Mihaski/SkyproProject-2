import json

from Category import Category


def load_data_from_json() -> list[dict]:
    """читает json возвращает данные о категориях и продуктах"""
    with open('./data/products.json') as json_file:
        data = json.load(json_file)

    result = []

    for catefory in data:
        result.append(Category(catefory["name"], catefory["description"], catefory["products"]))

    return result
