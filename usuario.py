class Usuario:
  # método construtor
    def __init__(self):
      self._id_usuario = 0
      self._telefone = ''
      self._nacionalidade = ''

    # método para adicionar usuário
    def adicionar_usuario(self, id_usuario):
      self._id_usuario = id_usuario
      self._telefone = input('Digite o telefone: ')
      self._nacionalidade = input('Digite a nacionalidade: ')

    # métodos get e set
    @property
    def id_usuario(self):
      return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, value):
      self._id_usuario = value

    @property
    def telefone(self):
      return self._telefone

    @telefone.setter
    def telefone(self, value):
      self._telefone = value

    @property
    def nacionalidade(self):
      return self._nacionalidade

    @nacionalidade.setter
    def nacionalidade(self, value):
      self._nacionalidade = value

  # instancio a classe Usuario e método
usuario = Usuario()
usuario.adicionar_usuario(1)
print(usuario.id_usuario)
print(usuario.telefone)
print(usuario.nacionalidade)
print('Usuário cadastrado com sucesso!')
