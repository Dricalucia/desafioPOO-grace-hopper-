import random

class Autor:
    def __init__(self, id_autor, nome_autor):
        self._id_autor = id_autor
        self._nome_autor = nome_autor

    def get_id_autor(self):
        return self._id_autor

    def get_nome_autor(self):
        return self._nome_autor

    def set_id_autor(self, id_autor):
        self._id_autor = id_autor

    def set_nome_autor(self, nome_autor):
        self._nome_autor = nome_autor

    def adicionar_autor(self, id_autor, nome_autor):
        self._id_autor = id_autor
        self._nome_autor = nome_autor

    def editar_autor(self, novo_nome):
        self._nome_autor = novo_nome

    def mostrar_autor(self):
        print(f"ID do Autor: {self._id_autor}")
        print(f"Nome do Autor: {self._nome_autor}")

    def deletar_autor(self):
        self._id_autor = 0
        self._nome_autor = ''

def main():
    autor = Autor(random.randint(0, 100), "")

    menu = '''
    Menu:
    1 - Adicionar Autor
    2 - Editar Autor
    3 - Mostrar Autor
    4 - Deletar Autor
    0 - Sair
    '''

    opcao = -1

    while opcao != 0:
        print(menu)
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            id_autor = int(input("Digite o ID do autor: "))
            nome_autor = input("Digite o nome do autor: ")
            autor.adicionar_autor(id_autor, nome_autor)
            print("Autor adicionado com sucesso!")

        elif opcao == 2:
            novo_nome = input("Digite o novo nome do autor: ")
            autor.editar_autor(novo_nome)
            print("Autor editado com sucesso!")

        elif opcao == 3:
            autor.mostrar_autor()

        elif opcao == 4:
            autor.deletar_autor()
            print("Autor deletado com sucesso!")

        elif opcao == 0:
            print("Saindo do sistema.")

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
