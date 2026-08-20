import pytest

from src.Category import Category


@pytest.fixture(autouse=True)
def reset_category_counters():
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def category_fruit(product_apple):
    return Category("friut", "many type of fruits", [product_apple, product_apple, product_apple])


def test_catefory_from_fixt(category_fruit):
    assert category_fruit.name == "friut"
    assert category_fruit.description == "many type of fruits"


def test_add_product(product_apple, category_fruit):
    old_count = category_fruit.product_count

    category_fruit.add_product(product_apple)

    assert category_fruit.product_count == old_count + 1


def test_catefory_count(product_apple):
    test_stat_2 = Category("vegetable", "many type of vegetables", [product_apple, product_apple, product_apple])

    assert test_stat_2.category_count == 1


def test_product_count_category(product_apple, category_fruit):
    test_state = category_fruit

    assert test_state.product_count == 3

    test_state.add_product(product_apple)

    assert test_state.product_count == 4
