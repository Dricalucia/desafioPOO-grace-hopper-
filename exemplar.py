# Criação da classe exemplar, seria como uma representação física da classe Livro
class Exemplar:

    # Construtor
    def __init__(self, livro):
        self.livro = livro
        self.disponivel = True