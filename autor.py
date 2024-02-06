import random
class Autor:
    def __init__(self):
        self._id_autor = random.randint(0, 100)
        self._nome_autor = ''

    # método para adicionar autor
    def adicionar_autor(self, _id_autor):
        self._id_autor = _id_autor
        self._nome_autor = input('Digite o nome do Autor: ')


    # método para editar autor
    def editar_autor(self, novo_nome):
        self._nome_autor = novo_nome 

    # método para mostrar autor
    def mostrar_autor(self):
        print(f"ID do Autor: {self._id_autor}")
        print(f"Nome do Autor: {self._nome_autor}")
    
    # método para deletar autor
    def deletar_autor(self):
        self._id_autor = 0
        self._nome_autor = ''

    @property
    def nome_autor(self):
        return self._nome_autor

    @nome_autor.setter
    def nome_autor(self, value):
        self._nome_autor = str(value)



autor = Autor()
# autor.mostrar_autor()
# autor.adicionar_autor(random)
# print(usuario.id_usuario)

# autor.mostrar_autor()
#print(autor._nome_autor)

# autor.editar_autor('Novo')
# autor.mostrar_autor()
print(autor._id_autor, autor._nome_autor)

# autor.deletar_autor()
# autor.mostrar_autor()
# print(autor._id_autor,autor._nome_autor)

