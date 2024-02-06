class Exemplar:
    def __init__(self, id_exemplar, id_livro, total_exemplar, qtd_disponivel, nr_maximo_renovacao):
        self.id_exemplar = id_exemplar
        self.id_livro = id_livro
        self.total_exemplar = total_exemplar
        self.qtd_disponivel = qtd_disponivel
        self.nr_maximo_renovacao = nr_maximo_renovacao
        self.disponivel = True

    def adicionar_exemplar(self, total, disponivel):
        self.total_exemplar += total
        self.qtd_disponivel += disponivel

    def excluir_exemplar(self):
        self.total_exemplar -= 1
        if self.total_exemplar == 0:
            self.qtd_disponivel = 0
            self.disponivel = False

    def alterar_exemplar(self, id_exemplar, id_livro, total_exemplar, qtd_disponivel, nr_maximo_renovacao):
        self.id_exemplar = id_exemplar
        self.id_livro = id_livro
        self.total_exemplar = total_exemplar
        self.qtd_disponivel = qtd_disponivel
        self.nr_maximo_renovacao = nr_maximo_renovacao

    def definir_numero_maximo_renovacoes(self, nr_maximo_renovacao):
        self.nr_maximo_renovacao = nr_maximo_renovacao