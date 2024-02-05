class Usuario:
  # Lista para armazenar os usuários
    usuarios = []
  # método construtor
    def __init__(self):
      self._nome = ''
      self._id_usuario = 0
      self._telefone = ''
      self._nacionalidade = ''
      Usuario.usuarios.append(self)

    # método para adicionar usuário
    def adicionar_usuario(self, id_usuario):
        self._id_usuario = id_usuario
        self._nome = input('Digite o nome: ')
        self._nacionalidade = ''
        telefones_cadastrados = [] # Lista para armazenar os telefones cadastrados
        #Este é um loop infinito que continuará até que o usuário insira um número de telefone celular com 11 digitos e que não esteja na lista de telefones cadastrados
        while True:
          # Solicita ao usuário que insira um número de telefone
          self._telefone = input('Digite o telefone: ')
          # Verifica se o número de telefone tem exatamente 11 dígitos
          if len(self._telefone) == 11 and self._telefone not in telefones_cadastrados:
            break
          elif self._telefone in telefones_cadastrados:
           print("Este telefone já está cadastrado. Por favor, insira um número diferente.")
          else:
            # Se o número de telefone for inválido, imprime uma mensagem de erro e solicita ao usuário que insira o número novamente
            print('Telefone inválido. Digite novamente.')
        self._nacionalidade = input('Digite a nacionalidade: ')
    # método para deletar usuário
    def deletar_usuario(self):
      del self._nome
      del self._id_usuario
      del self._telefone
      del self._nacionalidade

    # métodos get e set
    @property
    def id_usuario(self):
      return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, value):
      self._id_usuario = value

    @property
    def nome(self):
      return self._nome

    @nome.setter
    def nome(self, value):
      self._nome = value

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

    # método de classe para mostrar usuários
    @classmethod
    def mostrar_todos_usuarios(cls):
      return cls.usuarios



# instancio a classe Usuario e método
# usuario = Usuario()
# usuario.adicionar_usuario(1)
# print(usuario.id_usuario)
# print(usuario.telefone)
# print(usuario.nacionalidade)
# usuario.deletar_usuario()
# print('Usuário cadastrado com sucesso!')

