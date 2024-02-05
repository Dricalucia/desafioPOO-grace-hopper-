class Autor:
    def _init_(self):
        self._id_autor = 0
        self._nome_autor = ''

    # método para adicionar autor
    def adicionar_autor(self, _id_autor, _nome_autor):
        self._id_autor = _id_autor
        self._nome_autor = _nome_autor

autor = Autor()
autor.adicionar_autor(4, 'alberto')
print(autor._id_autor, autor._nome_autor)