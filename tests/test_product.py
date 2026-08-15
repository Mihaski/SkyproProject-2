def test_product_from_fixt(product_apple):
    assert product_apple.name == "apple"
    assert product_apple.price == 123.12
    assert product_apple.description == "fruit"
    assert product_apple.quantity == 1.3
