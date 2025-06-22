class NaoEncontradoNaListaException(Exception):
    def __init__(self, mensagem =""):
        super().__init__('Nao coseguimos encontrar ' + mensagem + ' na lista')