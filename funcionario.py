# Importando bibliotecas necessárias
from pessoa import Pessoa

# Classe funcionario definida como classe filha de Pessoa
# Foi criada para utilizarmos o conceito de classe abstrata
class Funcionario(Pessoa):

    # Método construtor herda da classe mãe
    def __init__(self, nome, telefone, nacionalidade, cargo):
        super().__init__(nome, telefone, nacionalidade)
        self.cargo = cargo

    # Método de impressão herdado da classe mãe
    def __str__(self):
        return super().__str__() + f'\nCargo: {(self.cargo)}'