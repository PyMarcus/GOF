from pizzaria.interfaces import PizzariaInterface
from datetime import datetime


class Pizzaria(PizzariaInterface):
    def __init__(self, date: int):
        assert date != 6, AssertionError("Pizzaria Fechada!")
        self.__date = date
        self.__igredients_a = ['calabresa']
        self.__igredients_b = ['presunto']
        self.__pizzaiolo_a = 'A'
        self.__pizzaiolo_b = 'B'

    def is_open(self) -> bool:
        return True

    def is_close(self) -> bool:
        return False

    def get_ingredients(self) -> list[str]:
        if self.__date % 2 == 0:
            return self.__igredients_a
        return self.__igredients_b

    def choice_pizzaiolo(self) -> str:
        if self.__date % 2 == 0:
            return self.__pizzaiolo_a
        return self.__pizzaiolo_b

    def pizza_today(self):
        print(f"A pizza é de {self.get_ingredients()[0]}")
        print(f"Preparada pelo chefe {self.choice_pizzaiolo()}")


if __name__ == '__main__':
    day = datetime.weekday(datetime.now())
    pizzaria = Pizzaria(day)
    pizzaria.pizza_today()
