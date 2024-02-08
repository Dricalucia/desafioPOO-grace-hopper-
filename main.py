from livro import *
from genero import *
from usuario import *
from autor import *
from exemplar import *
from emprestimo import *

import random

# Função que chama o menu de usuário
def menuUsuario():
    print("\n# Menu - Usuarios #")
    print("- Digite 1 para cadastrar um usuario")
    print("- Digite 2 para alterar um usuario")
    print("- Digite 3 para deletar um usuario")
    print("- Digite 4 para listar os usuarios cadastrados")
    print("- Digite 0 para sair do sistema")

    # Recebe a opcao do usuario
    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        id_usuario = random.randint(0, 100)
        print(f"O ID do usuário é: {id_usuario}")
        usuario = Usuario()
        usuario.adicionar_usuario(id_usuario)
    elif opcao == '2':
        for usuario in Usuario.usuarios:
            print(usuario.id_usuario, usuario.nome, usuario.telefone, usuario.nacionalidade)
        #solicitar ao usuário que digite o ID do usuário a ser alterado
        id_usuario = int(input("Digite o ID do usuário a ser alterado: "))

        # Procurar o usuário com o ID digitado
        for usuario in Usuario.usuarios:
            if usuario.id_usuario == id_usuario:
                # Chamar o método para alterar o usuário
                novo_nome = input("Digite o novo nome: ")
                novo_telefone = input("Digite o novo telefone: ")
                nova_nacionalidade = input("Digite a nova nacionalidade: ")
                # Editar o usuário
                usuario.editar_usuario(id_usuario, novo_nome, novo_telefone, nova_nacionalidade)
                # Mostrar o usuário alterado
                print(usuario.id_usuario, usuario.nome, usuario.telefone, usuario.nacionalidade)
                break
        else:
            print("Usuário não encontrado.")
        # Aqui você pode chamar o método para alterar o usuário
    elif opcao == '3':
        id_usuario = input("Digite o ID do usuário a ser deletado: ")
        # Aqui você pode chamar o método para deletar o usuário
    elif opcao == '4':
        todos_usuarios = Usuario.mostrar_todos_usuarios()
        for usuario in todos_usuarios:
            print(usuario.id_usuario, usuario.nome, usuario.telefone, usuario.nacionalidade)
    elif opcao == '0':
        pass
    else:
        print("Opção inválida. Tente novamente.")

# Função que chama o menu de livros
def menuLivros():
    

    # Printa as opcoes ao usuario
    print("\n# Menu - Livros #")
    print("- Digite 1 para cadastrar um livro")
    print("- Digite 2 para alterar um livro")
    print("- Digite 3 para deletar um livro")
    print("- Digite 4 para listar os livros cadastrados")
    print("- Digite 0 para sair do sistema")

    # Recebe a opcao do usuario
    opcao = int(input())

    # Condicoes, cada uma vai chamar uma funcao definida anteriormente
    if opcao == 1:
        # Instancia o objeto
        livro = Livro() # Estamos apenas instanciando um livro, mas precisamos cadastrá-lo no estoque da biblioteca

    elif opcao == 2:
        # A funcao chamada aqui deve alterar as caracteristicas do livro por meio de setters definidos na classe Livro
        #pass
        print("Livros cadastrados:")
        for livro in Livro.livros:
            print(f"ID: {livro.id_livro}, Título: {livro.titulo}")

        id_livro = int(input("Digite o ID do livro a ser alterado: "))

        for livro in Livro.livros:
            if livro.id_livro == id_livro:
                print(livro.id_livro, livro._titulo)

                novo_titulo = input("Digite o novo título do livro: ")
                nova_editora = input("Digite a nova editora do livro: ")
                quantidadeExemplares = int(input("Digite a nova quantidade de exemplares: "))

                print("Autores atuais:", livro.autores) # Listar os autores atuais
                novos_autores = []
                while True:
                    autor = input("Digite os autores (0 para parar o processo): ")
                    if autor == '0':
                        break
                    else:
                        novos_autores.append(autor)
                
                print("Gêneros atuais:", livro.generos)
                novos_generos = []
                while True:
                    genero = input("Digite o novo gênero (0 para parar): ")
                    if genero == '0':
                        break
                    novos_generos.append(genero)
                
                livro.titulo = novo_titulo
                livro.editora = nova_editora
                livro.exemplares = quantidadeExemplares
                livro.autores = novos_autores
                livro.generos = novos_generos

                # Livro alterado
                print(f"ID: {livro.id_livro}\nTítulo: {livro.titulo}\nEditora: {livro.editora}\nN° Exemplares: {livro.exemplares}\nAutores: {livro.autores}\nGêneros: {livro.generos}")
                break
            else:
                print("Livro não encontrado.")

    elif opcao == 3:
        # A funcao chamada aqui deve chamar o destrutor definido na classe Livro
        #pass
        print("Livros cadastrados:")
        for livro in Livro.livros:
            print(f"ID: {livro.id_livro}, Título: {livro.titulo}")

        id_livro = int(input("Digite o ID do livro a ser deletado: "))
        for livro in Livro.livros:
            if livro.id_livro == id_livro:
                Livro.livros.remove(livro)
                print("Livro deletado com sucesso.")
                break
            else:
                print("Livro não encontrado.")

    elif opcao == 4:
        # A funcao chamada aqui deve listar os livros cadastrados no sistema, funcao definida na classe Biblioteca
        for livro in Livro.livros:
            print(livro)

    elif opcao == 0:
        return

    else:
        print("Opcao invalida. Tente novamente.")

# Função que chama o menu biblioteca
def menuBiblioteca():
    print("\n# Menu - Biblioteca #")
    print("- Digite 1 para realizar um emprestimo")
    print("- Digite 2 para realizar a devolucao de um livro")
    print("- Digite 3 para listar o historico de emprestimos")
    print("- Digite 0 para sair do sistema")

    # Recebe a opcao do usuario
    opcao = int(input())

    if opcao == 1:
        pass
    
    elif opcao == 2:
        pass

    elif opcao == 3:
        pass

    elif opcao == 0:
        pass

    else:
        print("Opcao invalida. Tente novamente.")

# Menu geral
def main():

    while True:
        print("\n# Sistema de Biblioteca #")
        print("- Digite 1 para o menu de usuarios")
        print("- Digite 2 para o menu de livros")
        print("- Digite 3 para atividades da biblioteca")
        print("- Digite 0 para sair do sistema")

        opcao = int(input())

        # Menu usuario
        if opcao == 1:
            menuUsuario()

        # Menu livros
        elif opcao == 2:
            menuLivros()

        # Menu biblioteca
        elif opcao == 3:
            menuBiblioteca()

        # Sair do sistema
        elif opcao == 0:
            break

        # Caso invalido
        else:
            print("Numero invalido.")

if __name__ == "__main__":
    main()