class Livro:
    def __init__(self, titulo, editora, renovacoes_maximas=None):
        self.titulo = titulo
        self.editora = editora
        self.renovacoes_maximas = renovacoes_maximas
        self.autores = []
        self.generos = []
        self.exemplares_disponiveis = []

    def adicionar_autor(self, autor):
        self.autores.append(autor)

    def adicionar_genero(self, genero):
        self.generos.append(genero)

    def adicionar_exemplar(self, exemplar):
        self.exemplares_disponiveis.append(exemplar)