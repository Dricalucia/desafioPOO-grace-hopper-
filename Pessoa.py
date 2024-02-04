class Pessoa:
    def __init__(self, nome, telefone, nacionalidade):
        self._nome = nome
        self._telefone = telefone
        self._nacionalidade = nacionalidade

    @property
    def nome(self):
        return self._nome

    @property
    def telefone(self):
        return self._telefone

    @property
    def nacionalidade(self):
        return self._nacionalidade