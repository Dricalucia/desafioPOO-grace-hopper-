# Importando as bibliotecas necessárias
from pessoa import Pessoa

# Classe Cliente definida como classe filha de Pessoa
class Cliente(Pessoa):

    def __init__(self, nome, telefone, nacionalidade):
        # Método construtor herdado da classe mãe
        super().__init__(nome, telefone, nacionalidade)
        # Criação de um atributo próprio da classe Cliente, uma lista que mostrará os livros atualmente emprestados ao usuário
        self.livros = []

    # Os métodos getters e setters não precisam de implementação, pois são herdados da classe mãe

    def __str__(self):
        # O método de impressão é herdado da classe mãe, mas também há a adição da string que imprime os livros emprestados ao usuário
        return super().__str__() + f'\nLivros emprestados: {", ".join(self.livros)}'
