class Livro:
    livros = []  # Lista para armazenar os livros cadastrados

    # Construtor - instancia objetos do tipo Livro recebendo os atributos deste pelo usuário
    def __init__(self):
        # Acredito que talvez devêssemos utilizar o atributo ID, para trackear o livro
        # Definindo valores de quantidade fixa
        self._id_livro = len(Livro.livros) + 1
        self._titulo = input("Digite o nome do livro: ")
        self._editora = input("Digite o nome do editora: ")
        self._exemplares = input("Digite a quantidade de exemplares: ")
        # Definindo valores de quantidade variável
        autores = []
        generos = []
        # Loop de iteração de autores (torna-se interessante pensar como iremos usar objetos Autor, no lugar de strings)
        while True:
            autor = input("Digite os autores (0 para parar o processo): ")
            if autor == '0':
                break
            else:
                autores.append(autor)
        # Loop de iteração de generos
        while True:
            genero = input("Digite os generos (0 para parar o processo): ")
            if genero == '0':
                break
            else:
                generos.append(genero)
        # Definindo listas
        self._autores = autores
        self._generos = generos
        Livro.livros.append(self)  # Adicionando o livro à lista de livros
        print("Livro cadastrado com sucesso!\n")

    # Setters e getters só fazem sentido com atributos protegidos ou privados, por isso transformei os atributos em privados
    @property
    def id_livro(self):
        return self._id_livro
    
    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, novo_titulo):
#        novoTitulo = input("Digite o novo titulo do livro: ")
        self._titulo = novo_titulo

    @property
    def editora(self):
        return self._editora

    @editora.setter
    def editora(self, nova_editora):
#        novaEditora = input("Digite a nova editora do livro: ")
        self._editora = nova_editora

    @property
    def exemplares(self):
        return self._exemplares

    @exemplares.setter
    def exemplares(self, quantidadeExemplares):
 #       quantidadeExemplares = int(input("Digite a nova quantidade de exemplares: "))
        self._exemplares = quantidadeExemplares

    @property
    def generos(self):
        return self._generos

    @generos.setter
    def generos(self, novosGeneros):
        self._generos = novosGeneros  

    @property
    def autores(self):
        return self._autores

    @autores.setter
    def autores(self, novosAutores):
        self._autores = novosAutores    

#    def __del__(self):
#        print(f"Livro {self._titulo} deletado com sucesso.")
    
    def deletar_livro(self):
        Livro.livros.remove(self)
        print(f"Livro {self._titulo} deletado com sucesso.")

    def __str__(self):
       return f"ID do livro: {self._id_livro}\nNome do livro: {self._titulo}\nNome da editora: {self._editora}\nGeneros: {self._generos}\nAutores: {self._autores}\nQuantidade de exemplares: {self._exemplares}"

    