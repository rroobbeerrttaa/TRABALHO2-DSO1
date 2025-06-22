from abc import ABC, abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, numero: str, celular: int):
        self.__nome = nome
        self.__numero = numero
        self.__celular = celular
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def celular(self):
        return self.__celular
    
    @celular.setter
    def celular(self, celular):
        self.__celular = celular