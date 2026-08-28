import pytest

from src.BaseProduct import BaseProduct
from src.Product import Product


def test_base_product_is_abstract():
    with pytest.raises(TypeError):
        # noinspection abstract-class
        BaseProduct("Продукт", "Описание", 1000, 10)


def test_base_product_attributes():
    product = Product("Продукт", "Описание продукта", 1000, 10)

    assert product.name == "Продукт"
    assert product.description == "Описание продукта"
    assert product.price == 1000
    assert product.quantity == 10


def test_base_product_price_getter():
    product = Product("Продукт", "Описание", 1000, 10)

    assert product.price == 1000


def test_base_product_price_setter(capsys):
    product = Product("Продукт", "Описание", 1000, 10)

    product.price = 1500

    assert product.price == 1500


def test_base_product_price_setter_invalid(capsys):
    product = Product("Продукт", "Описание", 1000, 10)

    product.price = -500

    captured = capsys.readouterr()

    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 1000


def test_base_product_abstract_methods():
    assert "__str__" in BaseProduct.__abstractmethods__
    assert "__add__" in BaseProduct.__abstractmethods__
