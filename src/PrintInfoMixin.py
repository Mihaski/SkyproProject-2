class PrintInfoMixin:
    """печатает в консоль информацию о том, от какого класса и с какими параметрами был создан объект."""

    def __init__(self, *args, **kwargs):
        print(f"{self.__class__.__name__}{args}")
        super().__init__(*args, **kwargs)
