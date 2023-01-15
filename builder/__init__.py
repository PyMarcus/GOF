from abc import abstractmethod, ABC


class Builder(ABC):
    """
    O Builder é um padrão de projeto criacional que permite a
    você construir objetos complexos passo a passo. O padrão
    permite que produza diferentes tipos e representações
    de um objeto usando o mesmo código de construção
    """
    @property
    @abstractmethod
    def product(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def product_part_a(self, part) -> None:
        raise NotImplementedError

    @abstractmethod
    def product_part_b(self, part) -> None:
        raise NotImplementedError


class Product:
    def __init__(self):
        self.part = []

    def add(self, part):
        self.part.append(part)

    def print(self):
        for n in self.part:
            print(n)


class ConcretBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.producto = Product()
        return self.producto

    @property
    def product(self) -> Product:
        p = self.reset()
        self.producto = p
        return p

    def product_part_a(self, part) -> None:
        self.producto.add(part)

    def product_part_b(self, part) -> None:
        self.producto.add(part)


if __name__ == '__main__':
    cb = ConcretBuilder()
    cb.product_part_a('A')
    cb.product_part_b('B')
    cb.producto.print()
