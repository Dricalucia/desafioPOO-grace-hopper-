import sqlite3
from datetime import datetime, timedelta

# Conecta com o banco de dados
def conexao():
    con = sqlite3.connect('bancobiblioteca')
    return con

# Lista todos os livros, exemplares e total de exemplares disponíveis
def mostrar_livros_disponiveis():
    with conexao() as con:
        cursor = con.cursor()
        #Executa a consulta SQL
        cursor.execute('SELECT livro.titulo, exemplar.total_exemplar, exemplar.total_disponivel\
                    FROM livro JOIN exemplar ON livro.id_livro = exemplar.id_livro \
                    WHERE exemplar.total_disponivel > 0')
    #Retorna os resultados da consulta    
        livros_disponiveis = cursor.fetchall()
        return livros_disponiveis

print("***Total de Livros disponíveis***")
        #sobre os livros disponíveis e os imprime
for livros_disponiveis in mostrar_livros_disponiveis():
    titulo, total_exemplar, total_disponivel = livros_disponiveis
    print(f'\n Livro: {titulo} \n Total de exemplares: {total_exemplar} \n Total diponível para emprestimo: {total_disponivel} \n')        

#Chama a função para mostrar todos os livros
#mostrar_livros_disponiveis()

#Função para encontrar todos os livros emprestados no momento
def mostrar_livros_emprestados():
    with conexao() as con:
        cursor = con.cursor()
        cursor.execute('SELECT pessoa.nome AS nome_usuario,\
                       livro.titulo AS titulo_livro,\
                       emprestimo.data_emprestimo,\
                        emprestimo.data_devolucao\
                    FROM emprestimo\
                    JOIN usuario ON emprestimo.id_usuario = usuario.id_usuario\
                    JOIN exemplar ON emprestimo.id_exemplar = exemplar.id_exemplar\
                    JOIN livro ON exemplar.id_livro = livro.id_livro\
                    JOIN pessoa ON usuario.id_usuario = pessoa.id_pessoa;')
    #Retorna os resultados da consulta     
    livros_emprestados = cursor.fetchall()
    return livros_emprestados
print("***Livros Emprestados***")

#Itera sobre os livros emprestados e os imprime
for livros_emprestados in mostrar_livros_emprestados():
    nome_usuario, titulo_livro, data_emprestimo, data_devolucao = livros_emprestados
    print(f'\n O(a) usuário(a): {nome_usuario} \n Efetuou o empéstimo do Livro: {titulo_livro} \n Na data: {data_emprestimo}\n Com devolução prevista para: {data_devolucao} \n')

#Chama a função que mostra os livros emprestados.
mostrar_livros_emprestados()

#Função localizar os livros escritos por um autor específico.
def localizar_livro_por_autor(nome_autor):
    with conexao() as con:
        cursor = con.cursor()
        #Executa a consulta SQL
        cursor.execute('SELECT pessoa.nome AS nome_autor,\
                               livro.titulo AS titulo_livro\
                        FROM pessoa\
                        JOIN autor ON pessoa.id_pessoa = autor.id_autor\
                        JOIN autor_livro ON autor.id_autor = autor_livro.id_autor\
                        JOIN livro ON autor_livro.id_livro = livro.id_livro\
                        WHERE pessoa.nome = ?', (nome_autor,)) 
        #Retorna os resultados da consulta
        livro_por_autor = cursor.fetchall()
        if livro_por_autor:
            return livro_por_autor
        else:
            print('Nenhum Livro encontrado par o autor especificado.')
        return []
    
#Função para exibir os resultados
def resultado_livro_por_autor(livro_por_autor):  
        print('***Livro por autor ***')
        for nome_autor, titulo_livro in livro_por_autor:
         print(f'\n O(a) Autor(a): {nome_autor} \n Escreveu o Livro: {titulo_livro} \n')

 # Chama a função para localizar livros por autor especifico e exibe os resultados
livro_por_autor = localizar_livro_por_autor('J.R.R. Tolkien')
if livro_por_autor:
    resultado_livro_por_autor(livro_por_autor)


#Verificar o número de exemplares disponíveis de um determinado livro.
def localizar_exemplar_disponivel(nome_livro):
    with conexao() as con:
        cursor = con.cursor()
        #Executa a consulta SQL
        cursor.execute('SELECT livro.titulo, exemplar.total_disponivel\
                        FROM livro \
                        JOIN exemplar ON livro.id_livro = exemplar.id_livro \
                        WHERE livro.titulo = ?', (nome_livro,))
        #Retorna os resultados da consulta
        exemplar_disponivel = cursor.fetchall()
        if exemplar_disponivel:
            return exemplar_disponivel
        else:
            print('Nenhum exemplar encontrado para o livro informado.')
        return None 
#Função para exibir os resultados
def resultado_exemplar_disponivel(exemplar_disponivel):  
        print('***Exemplares disponíveis: ***')
        for titulo_livro, total_disponivel in exemplar_disponivel:
         print(f'\n O Livro {titulo_livro} \n tem {total_disponivel} exemplar(es) disponível(is) para emprestimo.\n')

#Nome do livro que vamos verificar 'O Hobbit'
nome_livro = 'O Hobbit'

 # Chama a função para localizar livros por autor especifico e exibe os resultados
exemplar_disponivel = localizar_exemplar_disponivel(nome_livro)
if exemplar_disponivel:
    resultado_exemplar_disponivel(exemplar_disponivel)

# Mostrar os empréstimos em atraso
# Definindo a data atual
data_atual = datetime.now()

# Consulta SQL para selecionar os livros em atraso
with conexao() as con:
    cursor = con.cursor()
    cursor.execute('SELECT livro.titulo, emprestimo.data_devolucao, emprestimo.estado\
                    FROM emprestimo \
                    JOIN livro ON emprestimo.id_exemplar  = livro.id_livro \
                    WHERE emprestimo.data_devolucao < ?', (data_atual,))
    
    # Obtém os resultados da consulta
    livros_atrasados = cursor.fetchall()

# Exibe os livros em atraso
print("***Livros em atraso***\n")
if livros_atrasados:
    for livro in livros_atrasados:
        print(f"Título: {livro[0]},\n Data de Devolução: {livro[1]},\n Estado: {livro[2]}\n")
else:
    print("Não há livros em atraso.")