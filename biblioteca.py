# Imports necessários
from usuario import Usuario
from funcionario import Funcionario
from exemplar import Exemplar
from livro import Livro
from emprestimo import Emprestimo

# A classe biblioteca funcionará como um gerenciador que manipula as outras classes e o banco de dados (simulado com listas e dicionários)
class Biblioteca:

    # Método construtor da biblioteca
    def __init__(self, nome):
        # Nome recebido por parâmetro
        self.nome = nome
        # Listas e dicionários que simulam o banco de dados
        self.usuarios = {}
        self.funcionarios = {}
        self.livros = {}
        self.emprestimos = []

    # Função de cadastro do usuario no banco de dados
    def cadastrarUsuario(self, idUsuario, nome, telefone, nacionalidade):
        # Instanciação do novo Usuario
        novoUsuario = Usuario(nome, telefone, nacionalidade)
        # Adição do novo usuario ao dicionário "livros", associando esse usuário à um ID único
        self.usuarios[idUsuario] = novoUsuario

    # Função de cadastro do funcionário no banco de dados
    def cadastrarFuncionario(self, idFuncionario, nome, telefone, nacionalidade, cargo):
        # Instanciação do novo Funcionário
        novoFunc = Funcionario(nome, telefone, nacionalidade, cargo)
        # Adição do novo funcionário ao dicionário "funcionários", associando esse usuário à um ID único
        self.funcionarios[idFuncionario] = novoFunc

    def cadastrarLivro(self, idLivro, titulo, editora, autores, generos, nRenovacoes, nExemplares):
        # Instanciação do novo Funcionário
        novoLivro = Livro(titulo, editora, autores, generos, nRenovacoes, nExemplares)
        # Adição do novo funcionário ao dicionário "funcionários", associando esse usuário à um ID único
        self.livros[idLivro] = novoLivro
        print("Livro cadastrado com sucesso!")
    
    def listarUsuarios(self):
        print("\nLista de usuários da biblioteca:")
        for idUsuario, usuario in self.usuarios.items():
            print(f"ID: {idUsuario}, {usuario}")

    def listarFuncionarios(self):
        print("\nLista de funcionários da biblioteca:")
        for idFuncionario, funcionario in self.funcionarios.items():
            print(f"ID: {idFuncionario}, {funcionario}")

    def listarLivros(self):
        print("\nLista de livros da biblioteca:")
        for idLivro, livro in self.livros.items():
            print(f"ID: {idLivro}, {livro}")

    def listarExemplares(self):
        print("\nLista de exemplares disponiveis da biblioteca:")
        for idLivro, livro in self.livros.items():
            for idExemplar, exemplar in livro.exemplares.items():
                if exemplar.esta_disponivel():
                    print(f"Nome do livro: {livro.titulo} ID do exemplar: {idExemplar}")

    def emprestarLivro(self, idUsuario, idEexemplar):
        # Se o exemplar estiver disponível
        usuario = self.usuarios[idUsuario]
        exemplar = self.exemplares_disponiveis()[idEexemplar]
        emprestimo = Emprestimo(usuario, exemplar)
        self.emprestimos.append(emprestimo)
        exemplar.emprestar()

    def devolverLivro(self, idExemplar):
        for emprestimo in self.emprestimos:
            if emprestimo.exemplar.id == idExemplar:
                emprestimo.devolver()

    def renovarLivro(self, idExemplar):
        for emprestimo in self.emprestimos:
            if emprestimo.exemplar.id == idExemplar:
                emprestimo.renovar()

    def exemplares_disponiveis(self, idLivro):
        exemplares_disponiveis = {}
        for idLivro, livro in self.livros.items():
            for idExemplar, exemplar in livro.exemplares.items():
                if exemplar.esta_disponivel():
                    exemplares_disponiveis[idExemplar] = exemplar
        return exemplares_disponiveis