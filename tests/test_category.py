import pytest

from src.Category import Category


@pytest.fixture
def category_fruit(product_apple):
    return Category("friut", "many type of fruits", [product_apple, product_apple, product_apple])


def test_catefory_from_fixt(category_fruit, product_apple):
    assert category_fruit.name == "friut"
    assert category_fruit.description == "many type of fruits"
    assert category_fruit.products == [product_apple, product_apple, product_apple]


def test_catefory_count(product_apple):
    test_stat_2 = Category("vegetable", "many type of vegetables", [product_apple, product_apple, product_apple])
    # на самом деле не важно какую вызывать убрать
    # причем если одинаковые делать объекты - не будет новый создан...
    # 2 потому что фикстурой уже 1 есть

    assert test_stat_2.category_count == 2


def test_product_count_category(product_apple, category_fruit):
    test_state = category_fruit
    # 1 это фикстура в test_catefory_from_fixt
    # 2 в test_catefory_count test_stat_2
    # 3 в этой функ. test_state
    # Итого 9 по 3 в каждой
    assert test_state.product_count == 9

    test_state.products = [product_apple, product_apple, product_apple, product_apple]
    # Ниче не изменяется если другой передавать т.к. меняется в момент инициализации - создания объекта
    assert test_state.product_count == 9

    test_stat_2 = Category(
        "fruit", "many type of fruits", [product_apple, product_apple, product_apple, product_apple, product_apple]
    )
    # еще один и тут 5 добавляется и 9+5 = 14
    # тоесть если надо другую логику чтобы менялся счетчик надо переместить или вынести его
    assert test_stat_2.product_count == 14
