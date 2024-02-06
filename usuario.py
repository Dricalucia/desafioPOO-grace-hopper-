# Importando bibliotecas necessárias
from pessoa import Pessoa
import random

# Classe usuário definida como classe filha de Pessoa
class Usuario(Pessoa):

  # Método construtor herdará da classe mãe
  def __init__(self):
    super().__init__()

  # IMPLEMENTAR! Método para cadastrar o usuário no banco de dados
  def cadastrar(self):
    # O id deve ser baseado na quantidade de usuários já cadastrados no banco de dados
    # IMPLEMENTAR! Devemos fazer uma checagem na contagem e assim, definir o id desse novo usuário
    self._id = ''
    # IMPLEMENTAR! Cadastro no banco de dados

  # IMPLEMENTAR! Método para excluir o usuário no banco de dados
  def deletar(self):
    del self._nome
    del self._id
    del self._telefone
    del self._nacionalidade

  # Métodos getters e setters não são necessários, pois herdam de sua classe mãe

  def __str__(self):
    super().__str__()