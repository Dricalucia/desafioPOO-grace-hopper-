from emprestimo import Emprestimo

# Criação da classe exemplar, seria como uma representação física da classe Livro
class Exemplar:

    # Construtor
    def __init__(self, livro):
        self.livro = livro
        self.disponivel = True
        self.emprestimoAssociado = None

    def esta_disponivel(self):
        return self.disponivel
    
    def emprestar(self, emprestimo):
        self.disponivel = False
        self.emprestimoAssociado = emprestimo

    def devolver(self):
        self.disponivel = True
        self.emprestimoAssociado = None

    def __str__(self):
        return(f"Exemplar de {self.livro.titulo}")