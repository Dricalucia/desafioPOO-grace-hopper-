import sqlite3

# Conecta com o banco de dados
def conexao():
    con = sqlite3.connect('bancobiblioteca')
    return con

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

#Função para atualizar um registro (marcar livro como disponível):
def marcar_livro_como_disponivel(nomeUsuario, tituloLivro):
    id_emprestimo = get_id_emprestimo(nomeUsuario, tituloLivro)
    idExemplar = get_id_exemplar(tituloLivro)
    with conexao() as con:
        cursor = con.cursor()
        for id in id_emprestimo:
            #Executa a consulta SQL para atualizar o estado do empréstimo
            cursor.execute("UPDATE emprestimo SET estado = 'Disponível' WHERE id_emprestimo = ?", (id[0],))
            # Incrementa a quantidade de exemplares disponíveis do livro emprestado
            con.execute("UPDATE exemplar SET total_disponivel = (total_disponivel + 1) WHERE id_exemplar = ?", (idExemplar,))
            print(f'O Livro {tituloLivro}, foi devolvido pelo(a) usuário(a) {nomeUsuario} e está disponível para emprestimo.')

#função pra excluir um registro (remover genero)
def remover_genero(nome_genero):
    with conexao() as con:
        cursor = con.cursor()
        # Executa a consulta SQL para excluir um genero
        cursor.execute("DELETE FROM genero WHERE genero = ?", (nome_genero,))


marcar_livro_como_disponivel('Caroline', 'O Hobbit')
remover_genero('Crime')
print('O genero escolhido foi deletado com sucesso.')