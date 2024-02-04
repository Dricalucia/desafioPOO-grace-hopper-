from datetime import date

class Emprestimo:
    def __init__(self, usuario, exemplar):
        self.usuario = usuario
        self.exemplar = exemplar
        self.data_emprestimo = date.today()
        self.data_devolucao = None
        self.estado_exemplar = "emprestado"

    def devolver_exemplar(self):
        self.exemplar.disponivel = True
        self.data_devolucao = date.today()
        self.estado_exemplar = "devolvido"