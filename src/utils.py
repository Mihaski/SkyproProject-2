import json
from json import JSONDecodeError

from Category import Category


def load_data_from_json(json_path: str = "./data/products.json") -> list[Category]:
    """Читает JSON-файл и возвращает список категорий."""
    try:
        with open(json_path, encoding="utf-8") as json_file:
            data = json.load(json_file)
    except JSONDecodeError as e:
        print(f"Ошибка при чтении JSON: {e}")
        return []
    except FileNotFoundError as e:
        print(f"Файл не найден: {e}")
        return []

    try:
        return [
            Category(
                category["name"],
                category["description"],
                category["products"]
            )
            for category in data
        ]
    except KeyError as e:
        print(f"В JSON отсутствует обязательное поле: {e}")
        return []
