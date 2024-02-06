from pessoa import Pessoa
import random

class Autor(Pessoa):
    def __init__(self):
        # Antes um ID aleatório foi definido, mas acredito que poderia resultar em conflitos, por exemplo, um usuário poderia ter o mesmo ID que o outro
        # Uma estrutura condicional poderia ser implementada, mas traria complexidade desnecessária ao código
        super().__init__()

    # O método de adicionar autor foi substituído pelo método de cadastrar o autor no banco de dados
    def cadastrar(self):
        self._id_autor = ''
        pass
    
    # método para deletar autor
    def deletar(self):
        del self._nome
        del self._id
        del self._telefone
        del self._nacionalidade

    def __str__(self):
        super().__str__()