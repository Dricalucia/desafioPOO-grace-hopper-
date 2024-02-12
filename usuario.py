# Importando as bibliotecas necessárias
from pessoa import Pessoa

# Classe Usuario definida como classe filha de Pessoa
class Usuario(Pessoa):

    def __init__(self, nome, telefone, nacionalidade):
        # Método construtor herdado da classe mãe
        super().__init__(nome, telefone, nacionalidade)
        # Criação de um atributo próprio da classe Usuario, uma lista que mostrará os livros atualmente emprestados
        self.livrosEmprestados = []

    def __str__(self):
        # O método de impressão é herdado da classe mãe, mas também há a adição da string que imprime os livros emprestados ao usuário
        return super().__str__() + f'Livros emprestados: {", ".join(self.livrosEmprestados)}\n'