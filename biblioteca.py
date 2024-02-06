# A classe biblioteca funcionará como um gerenciador de todas as outras classes
class Biblioteca:

    def __init__(self, nome):
        self._nome = nome

    def listarEmprestimos(self):
        # Esse método deve acessar o banco de dados que contém os empréstimos e printar: data de empréstimo, data de devolução e estado do exemplar
        pass

    def listarUsuarios(self):
        # O mesmo que a classe anterior, mas com usuarios
        pass

    def listarLivros(self): # O livro difere do exemplar, pois o exemplar é uma espécie de concretização desse livro, com ID e estado
        pass

    def listarAutores(self):
        pass

    def listarExemplaresDisponiveis(self):
        pass

    def listarExemplares(self):
        pass
    
    # Getter e setter do nome
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self):
        self._nome = input("Digite o novo nome: ")