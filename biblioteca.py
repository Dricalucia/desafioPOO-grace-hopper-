# Imports necessários
from cliente import Cliente
from funcionario import Funcionario
from exemplar import Exemplar
from livro import Livro

# A classe biblioteca funcionará como um gerenciador que manipula as outras classes e o banco de dados (simulado com listas e dicionários)
class Biblioteca:

    # Método construtor da biblioteca
    def __init__(self, nome):
        # Nome recebido por parâmetro
        self._nome = nome
        # Listas e dicionários que simulam o banco de dados
        self.clientes = {}
        self.funcionarios = {}
        self.livros = {}

    # Função de cadastro do cliente no banco de dados
    def cadastrarCliente(self, idCliente, nome, telefone, nacionalidade):
        # Instanciação do novo Cliente
        novoCliente = Cliente(nome, telefone, nacionalidade)
        # Adição do novo cliente ao dicionário "livros", associando esse usuário à um ID único
        self.clientes[idCliente] = novoCliente

    # Função de cadastro do funcionário no banco de dados
    def cadastrarFuncionario(self, idFuncionario, nome, telefone, nacionalidade, cargo):
        # Instanciação do novo Funcionário
        novoFunc = Funcionario(nome, telefone, nacionalidade, cargo)
        # Adição do novo funcionário ao dicionário "funcionários", associando esse usuário à um ID único
        self.funcionarios[idFuncionario] = novoFunc

    def cadastrarLivro(self, idLivro, titulo, editora, autores, generos):
        # Instanciação do novo Funcionário
        novoLivro = Livro(titulo, editora, autores, generos)
        # Adição do novo funcionário ao dicionário "funcionários", associando esse usuário à um ID único
        self.livros[idLivro] = novoLivro
    
    # Esse método foi implementado para o cadastro de exemplares de cada livro
    def cadastrarExemplar(self, idExemplar, livro):
        novoExemplar = Exemplar(livro)
        livro.exemplares[idExemplar] = novoExemplar

    # Getter e setter do nome da biblioteca
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, value):
        self._nome = value