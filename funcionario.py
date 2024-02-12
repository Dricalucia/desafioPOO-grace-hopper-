# Importando bibliotecas necessárias
from pessoa import Pessoa

# Classe funcionario definida como classe filha de Pessoa
# Foi criada para utilizarmos o conceito de classe abstrata
class Funcionario(Pessoa):

    # Método construtor herda da classe mãe
    def __init__(self, nome, telefone, nacionalidade, cargo):
        super().__init__(nome, telefone, nacionalidade)
        self._cargo = cargo

    # Métodos getters e setters não precisam de implementação, pois herdam de sua classe mãe

    # Entretanto, o método getter e setter de cargo precisa ser implementado pois é algo próprio da classe funcionario
    @property
    def cargo(self): # O id só faz sentido em conjunto com o banco de dados
        return self._cargo

    @cargo.setter
    def cargo(self, value):
        self._cargo = value

    # Método de impressão herdado da classe mãe
    def __str__(self):
        return super().__str__() + f'\nCargo: {(self.cargo)}'