import pytest

from src.Product import Product
from src.LawnGrass import LawnGrass


@pytest.fixture
def lawn_grass():
    return LawnGrass(
        "Газонная трава",
        "Трава для газона",
        500,
        10,
        "Россия",
        "7 дней",
        "Зеленый"
    )


def test_lawn_grass_creation(lawn_grass):
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.description == "Трава для газона"
    assert lawn_grass.price == 500
    assert lawn_grass.quantity == 10
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == "7 дней"
    assert lawn_grass.color == "Зеленый"


def test_lawn_grass_is_product(lawn_grass):
    assert isinstance(lawn_grass, Product)


def test_lawn_grass_add():
    lawn_grass_1 = LawnGrass(
        "Газонная трава",
        "Трава для газона",
        500,
        10,
        "Россия",
        "7 дней",
        "Зеленый"
    )

    lawn_grass_2 = LawnGrass(
        "Газонная трава 2",
        "Другая трава",
        300,
        5,
        "Беларусь",
        "10 дней",
        "Зеленый"
    )

    assert lawn_grass_1 + lawn_grass_2 == 6500


def test_lawn_grass_add_product():
    lawn_grass = LawnGrass(
        "Газонная трава",
        "Трава для газона",
        500,
        10,
        "Россия",
        "7 дней",
        "Зеленый"
    )

    product = Product(
        "Товар",
        "Обычный товар",
        1000,
        5
    )

    with pytest.raises(TypeError):
        lawn_grass + product