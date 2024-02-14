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
        # Nos dicionários (definido por chaves) teremos o seguinte padrão:
        '''
        Estrutura padrão: dicionario = {'key1':'value1', 'key2':'value2'}
        Exenplo de estrutura utilizada no código: conjunto = {'idUsuario1' : 'Usuario1',
                                                    'idUsuario2' : 'Usuario2'}
        Onde a chave é o código de identificação do objeto no BD (ID) e o valor é o próprio objeto 
        '''
        self.usuarios = {}
        self.funcionarios = {}
        self.livros = {}
        # Já a lista de empréstimos não terá id, apenas a lista de objetos do tipo "Emprestimo"
        self.emprestimos = []

    # Função de cadastro do usuario no banco de dados
    def cadastrarUsuario(self, idUsuario, nome, telefone, nacionalidade):
        # Checa se o ID já está sendo usado
        if idUsuario in self.usuarios:
            print(f"# Erro: O usuário de ID {idUsuario} já está cadastrado!")
        else:
            # Instanciação do novo Usuario
            novoUsuario = Usuario(nome, telefone, nacionalidade)
            # Adição do novo usuario ao dicionário "livros", associando esse usuário à um ID único
            self.usuarios[idUsuario] = novoUsuario
            print(f"# Sistema: Usuário de ID {idUsuario} cadastrado com sucesso!")

    # Função de cadastro do funcionário no banco de dados
    def cadastrarFuncionario(self, idFuncionario, nome, telefone, nacionalidade, cargo):
        # Checa se o ID já está sendo usado
        if idFuncionario in self.funcionarios:
            print(f"# Erro: O funcionário de ID {idFuncionario} já está cadastrado!")
        else:
            # Instanciação do novo Funcionário
            novoFunc = Funcionario(nome, telefone, nacionalidade, cargo)
            # Adição do novo funcionário ao dicionário "funcionários", associando esse usuário à um ID único
            self.funcionarios[idFuncionario] = novoFunc
            print(f"# Sistema: Funcionário de ID {idFuncionario} cadastrado com sucesso!")

    def cadastrarLivro(self, idLivro, titulo, editora, autores, generos, nRenovacoes, nExemplares):
        # Checa se o ID já está sendo usado
        if idLivro in self.livros:
            print(f"# Erro: O livro de ID {idLivro} já está cadastrado!")
        else:
            # Instanciação do novo livro
            novoLivro = Livro(titulo, editora, autores, generos, nRenovacoes, nExemplares)
            # Adição do novo livro ao dicionário "livros", associando esse objeto à um ID único
            self.livros[idLivro] = novoLivro
            print(f"# Sistema: Livro de ID {idLivro} cadastrado com sucesso!")
    
    # Função que lista os usuários
    def listarUsuarios(self):
        print("-----------------------------------------")
        print("# Lista de usuários da biblioteca:")
        # Tradução literal do comando: Para cada chave (idUsuario, int) e seu valor associado (usuario, objeto do tipo Usuario) nos itens
        # do dicionário "usuarios", faça:
        for idUsuario, usuario in self.usuarios.items():
            # Imprima o ID e o usuário
            # Aqui, quando imprimimos o "usuario", estamos chamando a função __str__ do objeto, definida na classe Usuario
            print(f"ID: {idUsuario}")
            print(f"{usuario}\n")
        print("-----------------------------------------")
    
    # Função que lista os funcionários (mesma lógica anterior)
    def listarFuncionarios(self):
        print("-----------------------------------------")
        print("# Lista de funcionários da biblioteca:")
        for idFuncionario, funcionario in self.funcionarios.items():
            print(f"ID: {idFuncionario}")
            print(f"{funcionario}\n")
        print("-----------------------------------------")

    # Função que lista os livros (mesma lógica anterior)
    def listarLivros(self):
        print("-----------------------------------------")
        print("# Lista de livros da biblioteca:")
        for idLivro, livro in self.livros.items():
            print(f"ID: {idLivro}")
            print(f"{livro}\n")
        print("-----------------------------------------")

    # Função que lista os exemplares DISPONÍVEIS
    def listarExemplares(self):
        print("-----------------------------------------")
        print("# Lista de exemplares disponiveis da biblioteca:")
        # Esse loop está percorrendo todos os itens do dic. livros
        for idLivro, livro in self.livros.items():
            # Já esse loop está percorrendo o dicionário de exemplares associado a cada livro
            for idExemplar, exemplar in livro.exemplares.items():
                # Verifica se o exemplar está disponível, e se sim, printa os dados no console
                if exemplar.esta_disponivel():
                    print(f"ID do exemplar: {idExemplar}, ID e Nome do livro: {idLivro} {livro.titulo} ")
        print("-----------------------------------------")
    # Explicando a lógica do código acima:
    # Primeiro, busque todos os livros disponíveis
    # Depois, busque os exemplares de cada livro
    # Verifique se o exemplar está disponível

    # Listando os empréstimos realizados
    def listarEmprestimos(self):
        print("-----------------------------------------")
        print("# Lista de emprestimos realizados na biblioteca:")
        # Percorre a lista e imprime
        for emprestimo in self.emprestimos:
            print(emprestimo)
        print("-----------------------------------------")

    # Função de empréstimo do Livro
    def emprestarLivro(self, idUsuario, idLivro, idEexemplar):
        # Verificando se o exemplar está disponível
        if not self.livros[idLivro].exemplares[idEexemplar].esta_disponivel():
            print(f"# Erro: O exemplar com ID {idEexemplar} do livro de ID {idLivro} não está disponível!")
        else:
            # Atribuindo os objetos à variáveis locais para facilitar a compreensão
            # A var "usuario" recebe o objeto Usuario associado ao ID recebido no parâmetro da func
            usuario = self.usuarios[idUsuario]
            # A var "exemplar" recebe o objeto Exemplar associado ao ID recebido no parâmetro da func
            # A func exemplares_disponiveis foi definida dentro da classe, ela retorna um dicionário com todos os exemplares disponíveis
            # de um certo livro, identificado pelo "idLivro", passado por parâmetro
            exemplar = self.exemplares_disponiveis(idLivro)[idEexemplar]
            # Instanciando um objeto do tipo Emprestimo
            emprestimo = Emprestimo(usuario, exemplar)
            # Adicionando o emprestimo à lista de registro da biblioteca
            self.emprestimos.append(emprestimo)
            # Chamando a funcao de emprestimo do exemplar e associando esse exemplar a um emprestimo
            exemplar.emprestar(emprestimo)
            print(f"# Sistema: O exemplar de ID {idEexemplar} do livro de ID {idLivro} foi emprestado com sucesso!")

    # Função que devolve o livro
    # Primeiro recebemos por parâmetro o id do livro e o id do exemplar (Esses dois precisam trabalhar em conjunto)
    # pois o id do exemplar só faz sentido com o id do livro associado a esse exemplar
    def devolverLivro(self, idExemplarDevolvido, idLivroDevolvido):
        # Verificando se o exemplar está realmente emprestado
        if self.livros[idLivroDevolvido].exemplares[idExemplarDevolvido].esta_disponivel():
            print("# Erro: O livro não foi emprestado e portanto não pode ser devolvido!")
        else:
            # Para cada item no dicionário de livros
            for idLivro, livro in self.livros.items():
                # Se o ID desse livro for igual ao id do livro a ser devolvido
                if idLivro == idLivroDevolvido:
                    # Percorra a lista de exemplares desse livro
                    for idExemplar, exemplar in livro.exemplares.items():
                        # Se o ID do exemplar for igual ao id do exemplar a ser devolvido
                        if idExemplar == idExemplarDevolvido:
                            exemplar.emprestimoAssociado.devolver()
                            print(f"# Sistema: Exemplar de ID {idExemplarDevolvido} do livro de ID {idLivroDevolvido} foi devolvido com sucesso!")
                            break

    # A função de renovar segue a mesma lógica que a função anterior
    def renovarLivro(self, idExemplarRenovado, idLivroRenovado):
        # Verificando se o exemplar está realmente emprestado
        exemplar = self.livros[idLivroRenovado].exemplares[idExemplarRenovado]
        if exemplar.esta_disponivel():
            print("# Erro: O livro não foi emprestado e portanto não pode ser renovado!")

        elif exemplar.emprestimoAssociado.renovacoes >= exemplar.emprestimoAssociado.renovacoesMaximas:
            print("# Erro: O livro atingiu o máximo de renovações e portanto não pode ser renovado! O livro foi automaticamente devolvido.")
            exemplar.emprestimoAssociado.devolver()

        else:
            for idLivro, livro in self.livros.items():
                if idLivro == idLivroRenovado:
                    for idExemplar, exemplar in livro.exemplares.items():
                        if idExemplar == idExemplarRenovado:
                            exemplar.emprestimoAssociado.renovar()
                            print(f"# Sistema: Exemplar de ID {idLivroRenovado} do livro de ID {idLivroRenovado} foi renovado com sucesso!")
                            break

    # Função que retorna os exemplares disponíveis de um certo livro
    # Primeiro passamos por parâmetro o id do livro procurado
    def exemplares_disponiveis(self, idLivroProcurado):
        # Criando um dicionário que será preenchido no loop
        exemplares_disponiveis = {}
        # Para cada item no dicionário de livros FAÇA
        for idLivro, livro in self.livros.items():
            # Se o id desse livro for igual ao id do livro procurado (passado por parâmetro) FAÇA
            if idLivro == idLivroProcurado:
                # Para cada exemplar no dicionário de exemplares desse livro FAÇA
                for idExemplar, exemplar in livro.exemplares.items():
                    # Verifique se ele está disponível
                    if exemplar.esta_disponivel():
                        # Se sim, adicione ao dicionário de exemplares disponíveis
                        exemplares_disponiveis[idExemplar] = exemplar
        # Retorne o dicionário
        return exemplares_disponiveis