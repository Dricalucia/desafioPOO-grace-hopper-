from emprestimo import Emprestimo

# Criação da classe exemplar, seria como uma representação física da classe Livro
class Exemplar:

    # Construtor
    def __init__(self, livro):
        self.livro = livro
        self.disponivel = True

    def esta_disponivel(self):
        return self.disponivel
    
    def emprestar(self):
        self.disponivel = False

    def devolver(self):
        self.disponivel = True

    def __str__(self):
        return(f"Exemplar de {self.livro.titulo}")