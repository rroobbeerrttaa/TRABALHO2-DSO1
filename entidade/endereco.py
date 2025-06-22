class Endereco:
    def __init__(self, cep: str = "", rua: str = "", numero: str = ""):
        self.__cep = cep
        self.__rua = rua
        self.__numero = numero

    @property
    def cep(self):
        return self.__cep
    
    @property
    def rua(self):
        return self.__rua
    
    @property
    def numero(self):
        return self.__numero
    
    @cep.setter
    def cep(self, cep):
        self.__cep = cep
    
    @rua.setter
    def rua(self, rua):
        self.__rua = rua
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero
