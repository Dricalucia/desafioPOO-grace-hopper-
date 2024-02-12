# Importando a biblioteca de classes abstratas
from abc import ABC, abstractmethod

# Definindo a classe Pessoa como um filho da classe ABC (Abstract Base Class)
class Pessoa(ABC):

    # Ao chamar o construtor, uma pessoa vai ser instanciada com base nos parâmetros requisitados
    def __init__(self, nome, telefone, nacionalidade):
        # Definindo atributos protegidos (a ideia é torná-los protegidos para trabalhar com setters e getters)
        self._nome = nome
        self._nacionalidade = nacionalidade
        self._telefone = telefone
        self._id = 0 # ID nulo, pois só faz sentido em conjunto com o banco de dados

    # Getters e Setters
    # Apesar de não serem frequentemente utilizados, é uma boa prática defini-los

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, value):
      self._nome = value

    @property
    def telefone(self):
        return self._telefone
    
    @telefone.setter
    def telefone(self, value):
      self._telefone = value
    
    @property
    def nacionalidade(self):
        return self._nacionalidade
    
    @nacionalidade.setter
    def nacionalidade(self, value):
      self._nacionalidade = value

    # Método de impressão dos dados do objeto
    def __str__(self):
        return f"Nome: {self.nome}\nNacionalidade: {self.nacionalidade}\nTelefone: {self.telefone}\n"
