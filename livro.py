# Importando bibliotecas necessárias
from exemplar import Exemplar

# Definindo a classe Livro
class Livro:

    # O construtor vai instanciar objetos do tipo Livro recebendo os atributos por parâmetro
    def __init__(self, titulo, editora, autores, generos):
        # Definindo valores de quantidade fixa
        self._titulo = titulo
        self._editora = editora
        # Os valores de quantidade variável não vão utilizar loops para sua iteração, no próprio código iremos adicionar as listas
        self._autores = autores
        self._generos = generos
        # Cada Livro terá uma lista de exemplares, para ficar mais fácil de entender, imagine os exemplares como várias cópias de um Livro
        # mas todas sendo diferentes, como uma espécie de manifestação física
        # Exemplo: Existe a entidade do livro Harry Potter, e teremos 5 exemplares desse livro
        # O livro em SI não pode ser tocado, ele é uma espécie de modelo, já os exemplares podem sim ser tocados e emprestados
        self.exemplares = {}

    # Setters e getters só fazem sentido com atributos protegidos ou privados, por isso os atributos serão privados
    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        self._titulo = value

    @property
    def editora(self):
        return self._editora

    @editora.setter
    def editora(self, value):
        self._editora = value

    @property
    def generos(self):
        return self._generos

    @generos.setter
    def generos(self, value):
        self._generos = value  

    @property
    def autores(self):
        return self._autores

    @autores.setter
    def autores(self, value):
        self._autores = value    
    
    @property
    def qntd_exemplar(self):
        return len(self.exemplares)

    # Métodos implementados para adição de elementos nas listas
    def adicionar_autor(self, autor):
        self.autores.append(autor)

    def adicionar_genero(self, genero):
        self.generos.append(genero)

    def __str__(self):
        return f"Nome do livro: {self._titulo}\nNome da editora: {self._editora}\nGeneros: {self._generos}\nAutores: {self._autores}\nQuantidade de exemplares: {self.qntd_exemplar}"