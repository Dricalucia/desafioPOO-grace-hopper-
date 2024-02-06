# Importando biblioteca de classes abstratas
from abc import ABC, abstractmethod

# Definindo a classe pessoa como um filho da classe ABC (Abstract Base Class)
class Pessoa(ABC):

    # Ao chamar o construtor, uma pessoa vai ser instanciada solicitando ao usuário o nome, telefone e nacionalidade
    def __init__(self):
        # Definindo atributos protegidos
        self._nome = input("Digite o nome: ")
        self._nacionalidade = input("Digite a nacionalidade")
        # Chama o próprio método que checa o telefone digitado e atribui ao objeto
        self.checar_telefone()

    # Método de checagem do telefone
    def checar_telefone(self):
       # Este é um loop infinito que continuará até que o usuário insira um número de telefone celular com 11 digitos e que não esteja na lista de telefones cadastrados
        while True:
            # Solicita ao usuário que insira um número de telefone
            self._telefone = input('Digite o telefone: ')
            # IMPLEMENTAR! Puxar os telefones já cadastrados no banco de dados
            telefones_cadastrados = []
            # Verifica se o número de telefone tem exatamente 11 dígitos
            if len(self._telefone) == 11 and self._telefone not in telefones_cadastrados:
                break
            elif self._telefone in telefones_cadastrados:
                print("Este telefone já está cadastrado. Por favor, insira um número diferente.")
            else:
                # Se o número de telefone for inválido, imprime uma mensagem de erro e solicita ao usuário que insira o número novamente
                print('Telefone inválido. Digite novamente.')

    # Esse método será definido como abstrato pois cada classe terá uma forma diferente de cadastrar no banco de dados 
    @abstractmethod
    def cadastrar(self):
       pass
    
    # Método para deletar usuário do banco de dados
    @abstractmethod
    def deletar(self):
        pass

    # Getters e Setters
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

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

    def __str__(self):
        print("Nome: {self._nome}")
        print("Nacionalidade: {self._Nacionalidade}")
        print("Telefone: {self._Telefone}")
        print("ID: {self._id}")