from abc import ABC, abstractmethod


class PizzariaInterface(ABC):
    @abstractmethod
    def is_open(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def is_close(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_ingredients(self) -> list[str]:
        raise NotImplementedError

    @abstractmethod
    def choice_pizzaiolo(self) -> str:
        raise NotImplementedError
