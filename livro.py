class Livro:

    def __init__(self, titulo, editora, generos, autores, exemplares):
        self.titulo = titulo
        self.editora = editora
        self.generos = generos
        self.autores = autores
        self.exemplares = exemplares
        print("Livro instanciado com sucesso!")

    def __del__(self):
        print("Livro deletado com sucesso!")
    
    def __str__(self):
        print(f"Nome do livro: {self.titulo}\nNome da editora: {self.editora}\nGeneros: {self.generos}\nAutores: {self.autores}\nQuantidade de exemplares: {self.exemplares}")