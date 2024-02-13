# Importando a biblioteca de classes abstratas
# Essa classe foi criada para usarmos uma classe abstrata no sistema
from abc import ABC

# Definindo a classe Pessoa como um filho da classe ABC (Abstract Base Class)
class Pessoa(ABC):

    # Ao chamar o construtor, uma pessoa vai ser instanciada com base nos parâmetros requisitados
    def __init__(self, nome, telefone, nacionalidade):
        self.nome = nome
        self.telefone = telefone
        self.nacionalidade = nacionalidade

    # Getters e Setters não foram implementados por questão de simplificação

    # Método de impressão dos dados do objeto
    def __str__(self):
        return f"Dados:\nNome: {self.nome}\nNacionalidade: {self.nacionalidade}\nTelefone: {self.telefone}\n"