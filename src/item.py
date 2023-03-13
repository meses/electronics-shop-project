
import csv
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    @staticmethod
    def string_to_number(data: str) -> int:
        return int(float(data))


    @classmethod
    def instantiate_from_csv(cls, path_file='../src/items.csv'):
        with open(path_file, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row['price'] = Item.string_to_number(row['price'])
                row['quantity'] = Item.string_to_number(row['quantity'])
                name, price, quantity = row['name'], row['price'], row['quantity']
                cls.all.append((name, price, quantity))
        #return cls(reader)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 10:
            self.__name = name
        else:
            raise Exception("Длина наименования товара превышает 10 символов.")

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
