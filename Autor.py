from Pessoa import *

class Autor(Pessoa):
    def __init__(self, nome, telefone, nacionalidade):
        super().__init__(nome, telefone, nacionalidade)