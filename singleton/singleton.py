class SingletonIncremental(type):
    """
    O Singleton é um padrão de projeto criacional, que
    garante que apenas um objeto desse tipo exista e
    forneça um único ponto de acesso a ele para qualquer outro código.
    """

    _instance = dict()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance = super().__call__(*args, **kwargs)
            cls._instance[cls] = instance
        return cls._instance[cls]

