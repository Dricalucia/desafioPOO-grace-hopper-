import sqlite3
from datetime import datetime, timedelta


#conectar com o banco de dados
def conexao():
    con = sqlite3.connect('bancobiblioteca')
    return con

#Função para selecionar id do livro
def get_id_livro(livro):
    with conexao() as con:
         #Executa consulta SQL pra obter id do livro com base no título fornecido
         cursorLivro = con.cursor()
         cursorLivro.execute("SELECT id_livro FROM livro WHERE titulo = ?", (livro,))
         #Recupera todos os ids dos livros 
         idLivros = cursorLivro.fetchall()
         #Itera sobre os id dos livros retornados
         for id in idLivros:
             # Retorna o primeiro ID encontrado (se houver algum)
             idLivro = id[0]
             return idLivro

#Funço para selecionar id do usuário
def get_id_usuario(nome):
    with conexao() as con:
         # Executa consulta SQL para obter o id do usuário com base no nome fornecido
         cursorUsuario = con.cursor()
         cursorUsuario.execute("SELECT usuario.id_usuario FROM usuario JOIN pessoa ON usuario.id_usuario = pessoa.id_pessoa\
                                WHERE pessoa.nome= ?", (nome,))
        #Recupera todos os IDs dos usuários correspondentes ao nome fornecido
         idUsuarios = cursorUsuario.fetchall()
         #Itera sobre os IDs dos usuários retornados
         for id in idUsuarios:
             #Retorna o primeiro ID encontrado (se houver algum)
             idUsuario = id[0]
             return idUsuario

#Função para selecionar id do autor
def get_id_autor(nome):
    with conexao() as con:
         #Executa uma consulta SQL para obter o ID do autor com base no nome fornecido
         cursorAutor = con.cursor()
         cursorAutor.execute("SELECT autor.id_autor FROM autor JOIN pessoa ON autor.id_autor = pessoa.id_pessoa\
                                WHERE pessoa.nome= ?", (nome,))
         # Recupera todos os IDs dos autores correspondentes ao nome fornecido
         idAutores = cursorAutor.fetchall()
         # Itera sobre os IDs dos autores retornados
         for id in idAutores:
              # Retorna o primeiro ID encontrado (se houver algum)
             idAutor = id[0]
             return idAutor

#Função para selecionar id exemplar
def get_id_exemplar(livro):
    with conexao() as con:
         # Executa uma consulta SQL para obter o ID do exemplar com base no título do livro fornecido
         cursorExemplar = con.cursor()
         cursorExemplar.execute("SELECT exemplar.id_exemplar FROM exemplar JOIN livro ON exemplar.id_livro = livro.id_livro\
                                 WHERE livro.titulo= ?", (livro,))
         # Recupera todos os IDs dos exemplares correspondentes ao título do livro fornecido
         idExemplares = cursorExemplar.fetchall()
         # Itera sobre os IDs dos exemplares retornados
         for id in idExemplares:
             # Retorna o primeiro ID encontrado (se houver algum)
             idExemplar = id[0]
             return idExemplar

# Função para obtém o ID do usuário e do exemplar usando as funções get_id_usuario e get_id_exemplar
def get_id_emprestimo(nomeUsuario, tituloLivro):
        idUsuario = get_id_usuario(nomeUsuario)
        idExemplar = get_id_exemplar(tituloLivro)
        with conexao() as con:
         # Executa uma consulta SQL para obter o ID do empréstimo com base no ID do usuário e do exemplar
         cursorEmprestimo = con.cursor()
         cursorEmprestimo.execute("SELECT emprestimo.id_emprestimo \
                                   FROM emprestimo JOIN usuario ON emprestimo.id_usuario = usuario.id_usuario \
                                                   JOIN pessoa ON usuario.id_usuario = pessoa.id_pessoa \
                                                   JOIN exemplar ON exemplar.id_exemplar = emprestimo.id_exemplar \
                                  WHERE usuario.id_usuario = ? \
                                    AND exemplar.id_exemplar = ?", (idUsuario, idExemplar))
        # Recupera todos os IDs dos empréstimos correspondentes
        idEmprestimos = cursorEmprestimo.fetchall()
        # Retorna os IDs dos empréstimos encontrados
        return idEmprestimos

# Função inserir Livro
def inserir_livro(titulo,editora):
    with conexao() as con:
         # Executa uma consulta SQL para inserir um novo livro na tabela 'livro'    
         con.execute("INSERT INTO livro(titulo, editora)\
                     VALUES (?, ?)",(titulo, editora))

#Inserindo titulo do livro e editora na tabela livro  
inserir_livro('O Hobbit', 'HaperCollins')
inserir_livro('O Senhor dos Anéis - Sociedade do Anel', 'HaperCollins')
inserir_livro('A Chama Gêmea', 'Livros Modernos')
inserir_livro('Códigos e Sombras', 'Editora Futura')
inserir_livro('Entre Mundos', 'Mundo Literário')
inserir_livro('Tramas Cruzadas', 'Edições Intrigantes')
inserir_livro('Conexões Invisíveis', 'Conexão Cultural')

# Função inserir genero do livro
def inserir_genero(genero):
    with conexao() as con:
        # Executa uma consulta SQL para inserir um novo gênero na tabela 'genero'    
         con.execute("INSERT INTO genero(genero) VALUES (?)", (genero,))

#Inserindo Genero na tabela genero
inserir_genero('Romance')
inserir_genero('Suspense')
inserir_genero('Ficção Científica')
inserir_genero('Aventura')
inserir_genero('Drama')
inserir_genero('Crime')
inserir_genero('Fantasia')
inserir_genero('Mistério')

# Função inserir genero_livro
def inserir_genero_livros(livro, genero):
    #Chamar funcao get_id_livro pata obter o Id do livro
    idLivro = get_id_livro(livro)
    with conexao() as con: 
        #Encontrar na base o id de um genero ou uma lista de generos       
        cursorGenero = con.cursor()
        # Para cada gênero na lista de gêneros fornecida
        for vGeneros in genero:
            # Executa uma consulta SQL para obter o ID do gênero a partir do seu nome
            cursorGenero.execute("SELECT id_genero FROM genero WHERE genero = ?", (vGeneros,))
            idGeneros = cursorGenero.fetchall()
            # Para cada ID de gênero retornado
            for idg in idGeneros:
                idGenero = idg[0]
                 #Inserir dados na tabela genero_livro, fazendo a associação entre livro e genero(s)              
                con.execute("INSERT INTO genero_livro(\
                            id_livro, id_genero) VALUES (?, ?)", (idLivro, idGenero))
              
#Chamando a função inserir_genero_livro   
inserir_genero_livros('O Hobbit', ['Fantasia', 'Aventura'])
inserir_genero_livros('Entre Mundos', ['Aventura', 'Fantasia'])
inserir_genero_livros('O Senhor dos Anéis - Sociedade do Anel', ['Fantasia', 'Aventura'])
inserir_genero_livros('A Chama Gêmea', ['Romance', 'Mistério'])
inserir_genero_livros('Códigos e Sombras', ['Suspence', 'Ficção Científica'])
inserir_genero_livros('Tramas Cruzadas', ['Drama', 'Suspense'])
inserir_genero_livros('Conexões Invisíveis', ['Ficção Científica', 'Romance'])

# Função inserir Pessoa e retorna o ID da pessoa inserida.
def inserir_pessoa(nome, telefone, nacionalidade):
      with conexao() as con:  
        cursorPessoa = con.cursor()
        cursorPessoa.execute("INSERT INTO pessoa(\
                             nome, telefone, nacionalidade)\
                             VALUES (?, ?, ?)",(nome, telefone, nacionalidade))
# Obter o ID da pessoa inserida
        id_pessoa = cursorPessoa.lastrowid
        return id_pessoa

#Função inserir Usuário
def inserir_usuario(nome, telefone, nacionalidade):
    id_pessoa = inserir_pessoa(nome, telefone, nacionalidade)
    with conexao() as con:
        cursorUsuario= con.cursor()
        cursorUsuario.execute("INSERT INTO usuario(\
                      id_usuario) VALUES (?)",(id_pessoa,))
        
#Funcao inserir um Autor ou vários autores
def inserir_autor(nome):
    for vNomes in nome:
        id_pessoa = inserir_pessoa(vNomes, None, None)
        with conexao() as con:
            cursorAutor= con.cursor()
            cursorAutor.execute("INSERT INTO autor(\
                id_autor) VALUES (?)", (id_pessoa,))

#Chamando a funcao inserir_usuario e passando os dados do usuáario
inserir_usuario(nome='Adriana', telefone='94067583', nacionalidade='Brasileira')
inserir_usuario(nome='Anaísa', telefone='94067584', nacionalidade='Brasileira')
inserir_usuario(nome='Andréia', telefone='94067585', nacionalidade='Brasileira')
inserir_usuario(nome='Caroline', telefone='94067581', nacionalidade='Brasileira')
inserir_usuario(nome='Cintia', telefone='94067586', nacionalidade='Brasileira')
inserir_usuario(nome='Luciane', telefone='94067587', nacionalidade='Brasileira')
inserir_usuario(nome='Marina', telefone='94067588', nacionalidade='Brasileira')
inserir_usuario(nome='Nathália', telefone='94067589', nacionalidade='Brasileira')
inserir_usuario(nome='Terezinha', telefone='94067580', nacionalidade='Brasileira')
inserir_usuario(nome='Vanessa', telefone='94067581', nacionalidade='Brasileira')
inserir_usuario(nome='Vitória', telefone='94067581', nacionalidade='Brasileira')


#Chamando a funcao inserir_autor e passando os dados do autor          
inserir_autor(['Ana Silva', 'J.R.R. Tolkien', 'João Pereira', 'Camila Pereira', 'Miguel Santos','Maria Oliveira', 'Carlos Santos','Rafaela Souza', 'Pedro Alves', 'Laura Lima', 'Rodrigo Costa'])

# Funcao inserir autor_livro
def inserir_autor_livros(livro, autor):
    #Chamar funcao get_id_livro
    idLivro = get_id_livro(livro)
    #Encontrar na base o id de um autor ou uma lista de autores        
    with conexao() as con:
        cursorAutor = con.cursor()
        for vAutores in autor:
            cursorAutor.execute("SELECT autor.id_autor FROM autor JOIN pessoa ON autor.id_autor = pessoa.id_pessoa\
                                 WHERE pessoa.nome= ?", (vAutores,))
            idAutor = cursorAutor.fetchall()
            for ida in idAutor:
                idAutor = ida[0]
                #Inserir dados na tabela autor_livro, fazendo a associação entre livro e autor(es)              
                con.execute("INSERT INTO autor_livro(\
                            id_livro, id_autor) VALUES (?, ?)", (idLivro, idAutor))
              
#Chamando a função inserir_autor_livro   
inserir_autor_livros('O Hobbit', ['J.R.R. Tolkien'])
inserir_autor_livros('Entre Mundos', ['Rafaela Souza', 'Pedro Alves'])
inserir_autor_livros('O Senhor dos Anéis - Sociedade do Anel', ['J.R.R. Tolkien'])
inserir_autor_livros('A Chama Gêmea', ['Ana Silva', 'João Pereira'])
inserir_autor_livros('Códigos e Sombras', ['Maria Oliveira', 'Carlos Santos'])
inserir_autor_livros('Tramas Cruzadas', ['Laura Lima', 'Rodrigo Costa'])
inserir_autor_livros('Conexões Invisíveis', ['Camila Pereira', 'Miguel Santos'])

#Funcao inserir exemplares
def inserir_exemplar(livro,total_exemplar, total_disponivel,max_renovacao):
    #Chamar funcao get_id_livro
    idLivro = get_id_livro(livro)
    with conexao() as con:
        con.execute("INSERT INTO exemplar(\
                    id_livro, total_exemplar, total_disponivel,max_renovacao)\
                     VALUES (?, ?, ?, ?)", (idLivro, total_exemplar, total_disponivel,max_renovacao))
        
#Chamando a função inserir_exemplar
inserir_exemplar('O Hobbit', 3, 3, 1)
inserir_exemplar('O Senhor dos Anéis - Sociedade do Anel', 2, 2, 1)
inserir_exemplar('Entre Mundos', 4, 4, 1)
inserir_exemplar('A Chama Gêmea', 2, 2, 1)
inserir_exemplar('Códigos e Sombras', 2, 2, 1)
inserir_exemplar('Tramas Cruzadas', 6, 6, 1)
inserir_exemplar('Conexões Invisíveis', 1, 1, 1)

#Funcao inserir emprestimo
def fazer_emprestimo(nomeUsuario, livro, data_emprestimo, data_devolucao, estado):
    #chamando as funcoes get_usuario e get_exemplar
    idUsuario = get_id_usuario(nomeUsuario)
    idExemplar = get_id_exemplar(livro)
    with conexao() as con:
        con.execute("INSERT INTO emprestimo(\
                    id_usuario, id_exemplar, data_emprestimo, data_devolucao, estado)\
                     VALUES (?, ?, ?, ?, ?)", (idUsuario, idExemplar, data_emprestimo, data_devolucao, estado))
        # Desincrementa a quantidade de exemplares disponíveis do livro emprestado
        con.execute("UPDATE exemplar SET total_disponivel = (total_disponivel - 1) WHERE id_exemplar = ?", (idExemplar,))

#Definindo data do emprestimo e da devolução
data_emprestimo = datetime.now()
data_devolucao = data_emprestimo + timedelta(days=10)
# Definindo uma data de devolução passada
data_devolucao_passada = data_emprestimo - timedelta(days=10)

#Chamando a funcao emprestimo e inserindo dados na tabela de emprestimo
fazer_emprestimo('Caroline','O Hobbit',data_emprestimo, data_devolucao,'Indisponível')
fazer_emprestimo('Anaísa','Entre Mundos',data_emprestimo, data_devolucao,'Indisponível')
fazer_emprestimo('Adriana','O Senhor dos Anéis - Sociedade do Anel',data_emprestimo, data_devolucao,'Indisponível')
fazer_emprestimo('Andréia','Conexões Invisíveis',data_emprestimo, data_devolucao,'Indisponível')
fazer_emprestimo('Cintia','Códigos e Sombras',data_emprestimo, data_devolucao,'Indisponível')
fazer_emprestimo('Luciane','Entre Mundos',data_emprestimo, data_devolucao,'Indisponível')
fazer_emprestimo('Marina','Entre Mundos',data_emprestimo, data_devolucao,'Indisponível')
fazer_emprestimo('Vitória','Tramas Cruzadas',data_emprestimo, data_devolucao,'Indisponível')

#Inserindo  alguns emprestimos com datas antigas
fazer_emprestimo('Caroline','Tramas Cruzadas',data_emprestimo, data_devolucao_passada,'Indisponível')
fazer_emprestimo('Caroline','O Senhor dos Anéis - Sociedade do Anel',data_emprestimo, data_devolucao_passada,'Indisponível')

#Funcao Inserir dados na tabela biblioteca para gerar um historico/controle de todas as atividades da biblioteca.
def inserir_biblioteca():
    with conexao() as con:
        cursorBiblioteca = con.cursor()
        cursorBiblioteca.execute("SELECT 1 AS 'id_biblioteca', \
                                        emprestimo.id_emprestimo, \
                                        usuario.id_usuario, \
                                        livro.id_livro \
                                        FROM emprestimo\
                                            JOIN usuario ON emprestimo.id_usuario = usuario.id_usuario \
                                            JOIN pessoa ON usuario.id_usuario = pessoa.id_pessoa \
                                            JOIN exemplar ON exemplar.id_exemplar = emprestimo.id_exemplar \
                                            JOIN livro ON exemplar.id_livro = livro.id_livro")
        
        historico = cursorBiblioteca.fetchall()
        for linha in historico:
            idBiblioteca ,idUsuario, idLivro, idEmprestimo = linha
            con.execute("INSERT INTO biblioteca(\
                    id_biblioteca, id_usuario, id_livro, id_emprestimo)\
                     VALUES (?, ?, ?, ?)", (idBiblioteca,idUsuario, idLivro, idEmprestimo))
        
#chamando a funcao inserir_biblioteca
inserir_biblioteca()
