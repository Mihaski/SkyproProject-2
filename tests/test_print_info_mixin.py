from src.Product import Product
from src.Smartphone import Smartphone


def test_print_info_mixin(capsys):
    Product("Продукт1", "Описание продукта", 1200, 10)

    captured = capsys.readouterr()

    assert captured.out == (
        "Product('Продукт1', 'Описание продукта', 1200, 10)\n"
    )


def test_print_info_mixin_creates_product():
    product = Product(
        "Продукт1",
        "Описание продукта",
        1200,
        10
    )

    assert product.name == "Продукт1"
    assert product.description == "Описание продукта"
    assert product.price == 1200
    assert product.quantity == 10


def test_print_info_mixin_smartphone(capsys):
    Smartphone(
        "iPhone 15",
        "Смартфон Apple",
        100000,
        2,
        95.5,
        "15 Pro",
        256,
        "Black"
    )

    captured = capsys.readouterr()

    assert captured.out == (
        "Smartphone('iPhone 15', 'Смартфон Apple', 100000, 2)\n"
    )
