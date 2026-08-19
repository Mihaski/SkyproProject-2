import pytest

from src.Product import Product


@pytest.fixture
def product_apple():
    return Product("apple", "fruit", 123.12, 1.3)
