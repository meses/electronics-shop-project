class InstantiateCSVError(Exception):
    """Ошибка инициализируется в случае, если в файле отсутствуют все необходимые поля"""

    def __init__(self, *args):
        self.msg = args[0] if args else "Файл item.csv Повреждён"

    def __str__(self):
        return self.msg