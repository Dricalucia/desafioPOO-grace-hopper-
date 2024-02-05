from livrocopy import *
from Genero import *
from usuariocopy import *
from autor import *
from Exemplar import *
from Emprestimo import *

#import random

# Exemplo de uso do sistema
autor1 = Autor("Francisco Saravia", "123456789", "Brasileiro")
autor2 = Autor("Jose Marcelo", "987654321", "Argentino")

usuario1 = Usuario("Marina", "111222333", "Brasileira")
usuario2 = Usuario("Lili", "111222333", "Brasileira")

genero1 = Genero("Ficção Científica")
genero2 = Genero("Suspense")
genero3 = Genero("Terror")
genero4 = Genero("Romance")

livro1 = Livro("Harry Potter", "Editora Pax", renovacoes_maximas=3)
livro1.adicionar_autor(autor1)
livro1.adicionar_autor(autor2)
livro1.adicionar_genero(genero1)
livro1.adicionar_genero(genero2)

livro2 = Livro("Meu amigo", "Editora Lacerda", renovacoes_maximas=2)
livro2.adicionar_autor(autor2)
livro2.adicionar_genero(genero3)
livro2.adicionar_genero(genero4)


exemplar1 = Exemplar()
exemplar2 = Exemplar()

livro1.adicionar_exemplar(exemplar1)
livro1.adicionar_exemplar(exemplar2)

emprestimo1 = Emprestimo(usuario1, exemplar1)
emprestimo2 = Emprestimo(usuario2, exemplar2)

print(f"Estado do exemplar antes da devolução: {livro1.exemplares_disponiveis[0].disponivel}")

# print(f"Estado do exemplar antes da devolução: {livro2.exemplares_disponiveis[1].disponivel}")

emprestimo1.devolver_exemplar()
print(f"Estado do exemplar após a devolução: {livro1.exemplares_disponiveis[0].disponivel}")




# # Função que chama o menu de usuário
# def menuUsuario():
#     print("\n# Menu - Usuarios #")
#     print("- Digite 1 para cadastrar um usuario")
#     print("- Digite 2 para alterar um usuario")
#     print("- Digite 3 para deletar um usuario")
#     print("- Digite 4 para listar os usuarios cadastrados")
#     print("- Digite 0 para sair do sistema")

#     # Recebe a opcao do usuario
#     opcao = input("Digite a opção desejada: ")

#     if opcao == '1':
#         id_usuario = random.randint(0, 100)
#         print(f"O ID do usuário é: {id_usuario}")
#         usuario = Usuario()
#         usuario.adicionar_usuario(id_usuario)
#     elif opcao == '2':
#         id_usuario = input("Digite o ID do usuário a ser alterado: ")
#         # Aqui você pode chamar o método para alterar o usuário
#     elif opcao == '3':
#         id_usuario = input("Digite o ID do usuário a ser deletado: ")
#         # Aqui você pode chamar o método para deletar o usuário
#     elif opcao == '4':
#         todos_usuarios = Usuario.mostrar_todos_usuarios()
#         for usuario in todos_usuarios:
#             print(usuario.id_usuario, usuario.telefone, usuario.nacionalidade)
#     elif opcao == '0':
#         pass
#     else:
#         print("Opção inválida. Tente novamente.")

# # Função que chama o menu de livros
# def menuLivros():
#     # Printa as opcoes ao usuario
#     print("\n# Menu - Livros #")
#     print("- Digite 1 para cadastrar um livro")
#     print("- Digite 2 para alterar um livro")
#     print("- Digite 3 para deletar um livro")
#     print("- Digite 4 para listar os livros cadastrados")
#     print("- Digite 0 para sair do sistema")
    
#     # Recebe a opcao do usuario
#     opcao = int(input())

#     # Condicoes, cada uma vai chamar uma funcao definida anteriormente
#     if opcao == 1:
#         # Instancia o objeto
#         livro = Livro() # Estamos apenas instanciando um livro, mas precisamos cadastrá-lo no estoque da biblioteca
    
#     elif opcao == 2:
#         # A funcao chamada aqui deve alterar as caracteristicas do livro por meio de setters definidos na classe Livro
#         pass

#     elif opcao == 3:
#         # A funcao chamada aqui deve chamar o destrutor definido na classe Livro
#         pass

#     elif opcao == 4:
#         # A funcao chamada aqui deve listar os livros cadastrados no sistema, funcao definida na classe Biblioteca
#         pass
    
#     elif opcao == 0:
#         return

#     else:
#         print("Opcao invalida. Tente novamente.")

# # Função que chama o menu biblioteca
# def menuBiblioteca():
#     print("\n# Menu - Biblioteca #")
#     print("- Digite 1 para realizar um emprestimo")
#     print("- Digite 2 para realizar a devolucao de um livro")
#     print("- Digite 3 para listar o historico de emprestimos")
#     print("- Digite 0 para sair do sistema")

#     # Recebe a opcao do usuario
#     opcao = int(input())

#     if opcao == 1:
#         pass
    
#     elif opcao == 2:
#         pass

#     elif opcao == 3:
#         pass

#     elif opcao == 0:
#         pass

#     else:
#         print("Opcao invalida. Tente novamente.")

# # Menu geral
# def main():

#     while True:
#         print("\n# Sistema de Biblioteca #")
#         print("- Digite 1 para o menu de usuarios")
#         print("- Digite 2 para o menu de livros")
#         print("- Digite 3 para atividades da biblioteca")
#         print("- Digite 0 para sair do sistema")

#         opcao = int(input())

#         # Menu usuario
#         if opcao == 1:
#             menuUsuario()

#         # Menu livros
#         elif opcao == 2:
#             menuLivros()

#         # Menu biblioteca
#         elif opcao == 3:
#             menuBiblioteca()

#         # Sair do sistema
#         elif opcao == 0:
#             break

#         # Caso invalido
#         else:
#             print("Numero invalido.")

# main()