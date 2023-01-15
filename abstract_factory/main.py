from random import randint
from abstract_factory import AbstractFactory


if __name__ == '__main__':
    objecto = AbstractFactory()
    choice = randint(0, 1)
    if choice == 1:
        objecto.say_hello_on_screen()
    else:
        objecto.say_hello_at_file()
