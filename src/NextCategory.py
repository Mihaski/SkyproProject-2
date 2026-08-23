from Category import Category


class NextCategory:
    """Итератор по продуктам категории"""

    def __init__(self, category: Category):
        self.category = category
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.category.products):
            raise StopIteration

        product = self.category.products[self.index]
        self.index += 1

        return product