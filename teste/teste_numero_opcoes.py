from abc import ABC, abstractmethod

class TesteNumeroOpcoes(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def teste_numero_opcoes(self, opcao, valores_validos = None):
        try:
            if opcao not in valores_validos:
                raise ValueError
            return opcao
        except ValueError:
            self.mostra_mensagem("Opção inválida, escolha novamente.")
