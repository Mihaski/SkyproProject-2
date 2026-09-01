import pytest

from src.LawnGrass import LawnGrass
from src.Product import Product
from src.Smartphone import Smartphone


def test_product_from_fixt(product_apple):
    assert product_apple.name == "apple"
    assert product_apple.price == 200
    assert product_apple.description == "fruit"
    assert product_apple.quantity == 5


def test_product_str(product_apple):
    assert str(product_apple) == "apple, 200 руб. Остаток: 5 шт."


def test_product_add():
    product_1 = Product("Товар 1", "Описание", 100, 3)
    product_2 = Product("Товар 2", "Описание", 200, 4)

    assert product_1 + product_2 == 1100


def test_product_add_different_classes():
    smartphone = Smartphone("iPhone", "Смартфон", 100000, 2, 95.5, "15 Pro", 256, "Black")

    lawn_grass = LawnGrass("Газонная трава", "Трава для газона", 500, 10, "Россия", "7 дней", "Green")

    with pytest.raises(TypeError):
        smartphone + lawn_grass


def test_smartphone_add():
    smartphone_1 = Smartphone("iPhone", "Смартфон", 100000, 2, 95.5, "15 Pro", 256, "Black")

    smartphone_2 = Smartphone("Samsung", "Смартфон", 80000, 3, 95.5, "S24", 256, "Black")

    assert smartphone_1 + smartphone_2 == 440000

def test_zero_quantity_init_product():
    with pytest.raises(ValueError):
        Product('ap','fruit', 0, 0,)