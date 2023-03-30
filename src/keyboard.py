from src.item import Item

class MixinLanguage:

    def __init__(self, language="EN"):
        self.__language = language

    @property
    def language(self):
        return self.__language


    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self


class KeyBoard(Item, MixinLanguage):
    """Класс для товара Клавиатура"""
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        MixinLanguage.__init__(self)




