# Importando as classes necessárias
from livro import Livro
from usuario import Usuario
from funcionario import Funcionario
from exemplar import Exemplar
from emprestimo import Emprestimo
from biblioteca import Biblioteca

# Observações:
# Por questões de simplificação, tratamento de erros não foram implementados, ou seja,
# consideramos que sempre serão passados argumentos válidos em qualquer situação.
# Métodos abstratos também não foram implementados.
# Setters, getters e atributos privados/protegidos também não foram implementados.
# O tempo máximo de empréstimo de um livro foi definido com o padrão de 14 dias.

# Instanciando o gerenciador
biblioteca = Biblioteca("PyLib")

biblioteca.cadastrarUsuario(1, 'Ana', 123456789, 'Brasileira')
biblioteca.cadastrarUsuario(2, 'João', 123456789, 'Mexicano')
biblioteca.cadastrarUsuario(3, 'Marcos', 123456789, 'Argentino')

biblioteca.cadastrarFuncionario(1, 'Eva', 11112222, 'Brasileira', 'Gerente')
biblioteca.cadastrarFuncionario(2, 'Carlos', 11112222, 'Espanhol', 'Assistente')

biblioteca.cadastrarLivro(1, "Harry Potter e o Cálice de Fogo", "Editora A", ["JK Rowling"], ["Aventura", "Ficção"], 2, 3)
biblioteca.cadastrarLivro(2, "Dom Casmurro", "Editora B", ["Machado de Assis"], ["Romance"], 2, 2)

biblioteca.listarUsuarios()
biblioteca.listarFuncionarios()
biblioteca.listarLivros()
biblioteca.listarExemplares()

biblioteca.emprestarLivro(1, 1, 1)
biblioteca.emprestarLivro(1, 2, 1)
biblioteca.emprestarLivro(2, 2, 0)

biblioteca.listarExemplares()
biblioteca.listarEmprestimos()
biblioteca.listarUsuarios()

biblioteca.devolverLivro(1, 1)

biblioteca.listarExemplares()
biblioteca.listarEmprestimos()
biblioteca.listarUsuarios()

biblioteca.renovarLivro(1, 2)

biblioteca.listarExemplares()
biblioteca.listarEmprestimos()
biblioteca.listarUsuarios()