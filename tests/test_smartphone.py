import pytest

from src.Product import Product
from src.Smartphone import Smartphone


@pytest.fixture
def smartphone():
    return Smartphone("iPhone 15", "Смартфон Apple", 100000, 2, 95.5, "15 Pro", 256, "Black")


def test_smartphone_creation(smartphone):
    assert smartphone.name == "iPhone 15"
    assert smartphone.description == "Смартфон Apple"
    assert smartphone.price == 100000
    assert smartphone.quantity == 2
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "15 Pro"
    assert smartphone.memory == 256
    assert smartphone.color == "Black"


def test_smartphone_is_product(smartphone):
    assert isinstance(smartphone, Product)


def test_smartphone_add():
    smartphone_1 = Smartphone("iPhone 15", "Смартфон Apple", 100000, 2, 95.5, "15 Pro", 256, "Black")

    smartphone_2 = Smartphone("Samsung S24", "Смартфон Samsung", 80000, 3, 95.5, "S24", 256, "Black")

    assert smartphone_1 + smartphone_2 == 440000


def test_smartphone_add_product():
    smartphone = Smartphone("iPhone 15", "Смартфон Apple", 100000, 2, 95.5, "15 Pro", 256, "Black")

    product = Product("Товар", "Обычный товар", 1000, 5)

    with pytest.raises(TypeError):
        smartphone + product
