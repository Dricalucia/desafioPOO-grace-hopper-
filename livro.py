class Livro:

    # Construtor que inicializa os atributos padrões
    # Se a função não tivesse sido definida, ainda assim o objeto seria instanciado com valores padrões
    def __init__(self):
        self._titulo = None
        self._editora = None
        self._exemplares = 0
        self._autores = []
        self._generos = []

    # O método cadastraLivro está sendo utilizado como uma espécie de construtor, mas não instacia o objeto, apenas reatribui
    # os valores aos atributos de acordo com a vontade do usuário
    def cadastraLivro(self):
        # Acredito que talvez devêssemos utilizar o atributo ID, para trackear o livro
        # Definindo valores de quantidade fixa
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
        print("Livro cadastrado com sucesso!\n")

    # Setters e getters só fazem sentido com atributos protegidos ou privados, por isso transformei os atributos em privados
    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self):
        novoTitulo = input("Digite o novo titulo do livro: ")
        self._titulo = novoTitulo

    @property
    def editora(self):
        return self._editora

    @editora.setter
    def editora(self):
        novaEditora = input("Digite a nova editora do livro: ")
        self._editora = novaEditora

    @property
    def exemplares(self):
        return self._exemplares

    @exemplares.setter
    def exemplares(self):
        quantidadeExemplares = int(input("Digite a nova quantidade de exemplares: "))
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

    def __del__(self):
        print(f"Livro {self._titulo} deletado com sucesso.")

    def __str__(self):
        print(f"Nome do livro: {self._titulo}\nNome da editora: {self._editora}\nGeneros: {self._generos}\nAutores: {self._autores}\nQuantidade de exemplares: {self._exemplares}")