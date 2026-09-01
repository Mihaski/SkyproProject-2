class OrderAddException(Exception):
    """Исключение при добавлении товара с нулевым количеством."""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Неизвестная ошибка добавления."

    def __str__(self):
        return self.message
