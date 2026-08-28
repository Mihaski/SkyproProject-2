from src.OrderProduct import OrderProduct


def test_order_product_create(product_apple):
    order = OrderProduct(product_apple, 2)

    assert order.product == product_apple
    assert order.quantity == 2


def test_order_product_total_price(product_apple):
    order = OrderProduct(product_apple, 2)
    # несмотря на, то что в продукте есть количество тут заказ и вообщем я не знаю
    assert order.total_price == "400"


def test_order_product_str(product_apple):
    order = OrderProduct(product_apple, 2)
    # несмотря на, то что в продукте есть количество тут заказ и вообщем я не знаю
    assert str(order) == "400"
