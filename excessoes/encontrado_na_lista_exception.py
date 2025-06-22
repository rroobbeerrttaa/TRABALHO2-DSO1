class EncontradoNaListaException(Exception):
    def __init__(self):
        super().__init__("Voce já tem isso cadastrado, tente outro!")
