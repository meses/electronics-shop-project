from src.item import Item

class Phone(Item):

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_count):
        if type(new_count) == int and new_count > 0:
            self.__number_of_sim = new_count
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    @staticmethod
    def validate_number_of_sim(value):
        if type(value) == int and value > 0:
            return value
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __init__(self, name: str, price: float, quantity: int, count_sim_card: int):
        # Вызываем метод базового класса
        super().__init__(name, price, quantity)
        # Дополнительный код
        self.validate_number_of_sim(count_sim_card)
        self.__number_of_sim = count_sim_card

    def __add__(self, other):
        """Сложение количества товаров"""
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise TypeError("Аргуметы должны быть объектами класса Item или его наследниками")

    def __radd__(self, other):
        """Сложение количества товаров в обратном порядке аргументов"""
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise TypeError("Аргуметы должны быть объектами класса Item или его наследниками")

    def __repr__(self):
        return f'{self.__class__.__name__}(\'{self.name}\', {self.price}, {self.quantity}, {self.__number_of_sim})'

    def __str__(self):
        return self.name
