from livro import *
from genero import *

def cadastrarLivro():
    titulo = input("Digite o nome do livro: ")
    editora = input("Digite o nome do editora: ")
    exemplares = input("Digite a quantidade de exemplares: ")
    autores = []
    generos = []
    while True:
        autor = input("Digite os autores: ")
        if autor == '0':
            break
        else:
            autores.append(autor)
    while True:
        genero = input("Digite os generos: ")
        if genero == '0':
            break
        else:
            generos.append(genero)
    livro = Livro(titulo, editora, autores, generos, exemplares)
    print("Livro cadastrado com sucesso!\n")
    return livro

def menuUsuario():
    print("\n# Menu - Usuarios #")
    print("- Digite 1 para cadastrar um usuario")
    print("- Digite 2 para alterar um usuario")
    print("- Digite 3 para deletar um usuario")
    print("- Digite 4 para listar os usuarios cadastrados")
    print("- Digite 0 para sair do sistema")

    # Recebe a opcao do usuario
    opcao = int(input())

    if opcao == 1:
        pass
    
    elif opcao == 2:
        pass

    elif opcao == 3:
        pass

    elif opcao == 4:
        pass

    elif opcao == 0:
        pass

    else:
        print("Opcao invalida. Tente novamente.")

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
        cadastrarLivro()
    
    elif opcao == 2:
        # A funcao chamada aqui deve alterar as caracteristicas do livro por meio de setters definidos na classe Livro
        pass

    elif opcao == 3:
        # A funcao chamada aqui deve chamar o destrutor definido na classe Livro
        pass

    elif opcao == 4:
        # A funcao chamada aqui deve listar os livros cadastrados no sistema, funcao definida na classe Biblioteca
        pass

    elif opcao == 0:
        pass

    else:
        print("Opcao invalida. Tente novamente.")

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

main()