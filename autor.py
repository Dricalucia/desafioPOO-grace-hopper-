from pessoa import Pessoa
import random

class Autor(Pessoa):
    def __init__(self):
        # Antes um ID aleatório foi definido, mas acredito que poderia resultar em conflitos, por exemplo, um usuário poderia ter o mesmo ID que o outro
        # Uma estrutura condicional que checasse o ID poderia ser implementada, mas traria complexidade desnecessária ao código
        super().__init__() # Herdando o construtor da classe mãe (Pessoa)

    # O método de cadastrar o autor foi substituído por um método no gerenciador (biblioteca)
    # O método de deletar o autor também foi substítuído por um método no gerenciador

    # Método que printa as informações do objeto no console (também herdado da classe mãe)
    def __str__(self):
        super().__str__()