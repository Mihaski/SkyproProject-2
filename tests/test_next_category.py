import pytest

from src.Category import Category
from src.NextCategory import NextCategory
from src.Product import Product


@pytest.fixture
def category():
    products = [
        Product("Телефон", "Смартфон", 50000, 10),
        Product("Ноутбук", "Ноутбук", 100000, 5),
        Product("Мышь", "Компьютерная мышь", 3000, 20),
    ]

    return Category("Электроника", "Электронные товары", products)


def test_iterator_returns_category_iterator(category):
    iterator = NextCategory(category)

    assert iter(iterator) is iterator


def test_iterator_returns_products_in_order(category):
    iterator = NextCategory(category)

    assert next(iterator).name == "Телефон"
    assert next(iterator).name == "Ноутбук"
    assert next(iterator).name == "Мышь"


def test_iterator_raises_stop_iteration(category):
    iterator = NextCategory(category)

    next(iterator)
    next(iterator)
    next(iterator)

    with pytest.raises(StopIteration):
        next(iterator)


def test_iterator_works_with_for(category):
    products = list(NextCategory(category))

    assert len(products) == 3
    assert products[0].name == "Телефон"
    assert products[1].name == "Ноутбук"
    assert products[2].name == "Мышь"
