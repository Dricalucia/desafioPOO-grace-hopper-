# Importando as classes necessárias
from livro import Livro
from usuario import Usuario
from funcionario import Funcionario
from exemplar import Exemplar
from emprestimo import Emprestimo
from biblioteca import Biblioteca

# Observações:
# Métodos abstratos também não foram implementados.
# Setters, getters e atributos privados/protegidos também não foram implementados.

# Instanciando o gerenciador
biblioteca = Biblioteca("PyLib")

# Cadastro de usuários
# Ordem: ID, Nome, Telefone, Nacionalidade
biblioteca.cadastrarUsuario(1, 'Ana', 123456789, 'Brasileira')
biblioteca.cadastrarUsuario(2, 'João', 123456789, 'Mexicano')
biblioteca.cadastrarUsuario(3, 'Marcos', 123456789, 'Argentino')

# Cadastro de funcionários
# Ordem: ID, Nome, Telefone, Nacionalidade e Cargo
biblioteca.cadastrarFuncionario(1, 'Eva', 11112222, 'Brasileira', 'Gerente')
biblioteca.cadastrarFuncionario(2, 'Carlos', 11112222, 'Espanhol', 'Assistente')

# Cadastro de livros
# Ordem: ID, Título, Editora, Autores, Gêneros, Número máximo de renovações e Número de exemplares
biblioteca.cadastrarLivro(1, "Harry Potter e o Cálice de Fogo", "Editora A", ["JK Rowling"], ["Aventura", "Ficção"], 2, 3)
biblioteca.cadastrarLivro(2, "Dom Casmurro", "Editora B", ["Machado de Assis"], ["Romance"], 2, 2)

# Testando possíveis erros com ID's já existentes
biblioteca.cadastrarUsuario(1, 'Clara', 123456789, 'Brasileira')
biblioteca.cadastrarFuncionario(1, 'Maria', 11112222, 'Brasileira', 'Bibliotecária')
biblioteca.cadastrarLivro(2, "O Pequeno Príncipe", "Editora C", ["Antoine de Saint-Exupéry"], ["Literatura Infantil", "Fábula"], 2, 2)

# Impressão dos resultados
biblioteca.listarUsuarios()
biblioteca.listarFuncionarios()
biblioteca.listarLivros()
biblioteca.listarExemplares()
biblioteca.listarEmprestimos()

# Emprestando livros
# Ordem: ID do Usuário, ID do Livro e ID do Exemplar
biblioteca.emprestarLivro(1, 1, 1)
biblioteca.emprestarLivro(1, 2, 1)
biblioteca.emprestarLivro(2, 2, 0)

# Impressão dos resultados
biblioteca.listarExemplares()
biblioteca.listarEmprestimos()
biblioteca.listarUsuarios()

# Devolvendo livros
# Ordem: ID do Exemplar e ID do Livro
biblioteca.devolverLivro(1, 1)
biblioteca.devolverLivro(1, 2)

# Renovando livros
# Ordem: ID do Exemplar e ID do Livro
biblioteca.renovarLivro(0, 2)

# Impressão de resultados
biblioteca.listarExemplares()
biblioteca.listarEmprestimos()
biblioteca.listarUsuarios()

# Testando erros de renovação de um livro já devolvido
biblioteca.renovarLivro(1, 2)

# Testando limite de renovação
biblioteca.renovarLivro(0, 2)
biblioteca.renovarLivro(0, 2)
biblioteca.renovarLivro(0, 2)

# Impressão de resultados
biblioteca.listarExemplares()
biblioteca.listarEmprestimos()
biblioteca.listarUsuarios()