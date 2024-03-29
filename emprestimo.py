# Importando módulos necessários
from datetime import date

# Defininindo a classe empréstimo
class Emprestimo:

    # Quando um objeto empréstimo for instanciado, o exemplar vai ser emprestado
    def __init__(self, usuario, exemplar):
        # Defino o usuário e o exemplar ligado ao empréstimo
        self.usuario = usuario
        self.exemplar = exemplar
        self.renovacoesMaximas = exemplar.livro.num_renovacoes_max
        self.renovacoes = 0
        self.data_emprestimo = date.today()
        self.data_devolucao = None
        self.exemplar.emprestar(self)
        # Iterando a lista de livros emprestados do usuário em questão
        usuario.livrosEmprestados.append(exemplar)

    def devolver(self):
        self.exemplar.devolver()
        self.data_devolucao = date.today()
        self.usuario.livrosEmprestados.remove(self.exemplar)

    def renovar(self):
        self.renovacoes += 1  

    @property
    def estado(self):
        if self.exemplar.disponivel == True:
            return "Devolvido"
        else:
            return "Emprestado"

    def __str__(self):
        return f"\nLivro: {self.exemplar.livro.titulo}\nUsuario: {self.usuario.nome}\nData de Emprestimo: {self.data_emprestimo}\nData de devolucao: {self.data_devolucao}\nRenovacoes: {self.renovacoes}\nRenovacoes Maximas: {self.renovacoesMaximas}\nEstado: {self.estado}"