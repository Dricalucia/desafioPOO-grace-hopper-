# Importando bibliotecas necessárias
from exemplar import Exemplar

# Definindo a classe Livro
class Livro:

    # O construtor vai instanciar objetos do tipo Livro recebendo os atributos por parâmetro
    def __init__(self, titulo, editora, autores, generos, num_renovacoes_max, num_exemplares):
        # Definindo valores de quantidade fixa
        self.titulo = titulo
        self.editora = editora
        # Os valores de quantidade variável não vão utilizar loops para sua iteração, no próprio código iremos adicionar as listas
        self.autores = autores
        self.generos = generos
        self.num_renovacoes_max = num_renovacoes_max
        self.num_exemplares = num_exemplares
        # Cada Livro terá uma lista de exemplares, para ficar mais fácil de entender, imagine os exemplares como várias cópias de um Livro
        # mas todas sendo diferentes, como uma espécie de manifestação física
        # Exemplo: Existe a entidade do livro Harry Potter, e teremos 5 exemplares desse livro
        # O livro em SI não pode ser tocado, ele é uma espécie de modelo, já os exemplares podem sim ser tocados e emprestados
        self.exemplares = {}
        # Criação dos objetos do tipo Exemplar, a quantidade será definida pelo parâmetro recebido no construtor do Livro
        for i in range(num_exemplares):
            self.exemplares[i] = Exemplar(self)

    def __str__(self):
        return f"Nome do livro: {self.titulo}\nNome da editora: {self.editora}\nGeneros: {self.generos}\nAutores: {self.autores}\nQuantidade de exemplares: {self.num_exemplares}\nNumero de renovacoes maximas: {self.num_renovacoes_max}"