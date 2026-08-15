import pytest

from Product import Product


@pytest.fixture
def product_apple():
    return Product("apple", "fruit", 123.12, 1.3)


def test_product_from_fixt(product_apple):
    assert product_apple.name == "apple"
    assert product_apple.price == 123.12
    assert product_apple.description == "fruit"
    assert product_apple.quantity == 1.3
