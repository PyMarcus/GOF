from interfaces import HelloWorldInterface


class AbstractFactory(HelloWorldInterface):
    """
    O Abstract Factory é um padrão de projeto criacional que permite que você
    produza famílias de objetos relacionados sem ter que
    especificar suas classes concretas.
    """
    def __init__(self) -> None:
        pass

    def say_hello_on_screen(self) -> None:
        print("Hello, world!")

    def say_hello_at_file(self) -> None:
        with open('output.txt', 'w') as file:
            file.write('Hello, world!')
