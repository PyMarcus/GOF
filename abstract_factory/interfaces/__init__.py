from abc import ABC, abstractmethod


class HelloWorldInterface(ABC):
    @abstractmethod
    def say_hello_on_screen(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def say_hello_at_file(self) -> None:
        raise NotImplementedError
