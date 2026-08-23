from src.Product import Product


def test_product_from_fixt(product_apple):
    assert product_apple.name == "apple"
    assert product_apple.price == 200
    assert product_apple.description == "fruit"
    assert product_apple.quantity == 5


def test_product_str(product_apple):
    assert str(product_apple) == "apple, 200 руб. Остаток: 5 шт."


def test_product_add(product_apple):
    product_2 = Product("Ноутбук", "Ноутбук", 100000, 5)

    assert product_apple + product_2 == 501000
