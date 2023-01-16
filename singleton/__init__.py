from singleton import SingletonIncremental


class Incremental(metaclass=SingletonIncremental):
    def __init__(self, limit):
        self.__limit = limit
        self.__count = 0

    def incremental(self):
        for n in range(self.__limit):
            self.__count += n
            print(f"Incremental {self.__count}")


if __name__ == '__main__':
    print("PRIMEIRA E UNICA INSTANCIA A SER ALOCADA NA MEMORIA")
    incremental1 = Incremental(10)
    incremental1.incremental()
    print("SEGUNDA INSTANCIA NÃO ALTERADA, INICIA DE ONDE PAROU")
    incremental2 = Incremental(13)
    incremental2.incremental()
