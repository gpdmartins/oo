class Cliente:

    def __init__(self, nome, limite):
        self.__nome = nome
        self.__limite = limite

    @property
    def nome(self):
        print("chamando @property nome()")
        return self.__nome.title()
    @property
    def limite(self):
        return self.__limite

    @nome.setter
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome

    @limite.setter
    def limite(self, limite):
        print("chamando setter limite()")
        self.__limite = limite
