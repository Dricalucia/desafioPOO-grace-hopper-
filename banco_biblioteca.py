#Banco de Dados - Gerenciamento de Biblioteca
import sqlite3

conectar = sqlite3.connect('bancobiblioteca')

cursor = conectar.cursor()

# Criação das Tabelas>

#Tabela pessoa
cursor.execute('CREATE TABLE pessoa( \
               id_pessoa INTEGER PRIMARY KEY AUTOINCREMENT, \
               nome VARCHAR(50) NOT NULL, \
               telefone VARCHAR (15), \
               nacionalidade VARCHAR (30));')

#Tabela usuario
cursor.execute('CREATE TABLE usuario(\
               id_usuario INTEGER PRIMARY KEY, \
               FOREIGN KEY(id_usuario) REFERENCES pessoa(id_pessoa));')

#Tabela autor
cursor.execute('CREATE TABLE autor(\
               id_autor INTEGER PRIMARY KEY AUTOINCREMENT,\
               FOREIGN KEY(id_autor) REFERENCES pessoa(id_pessoa));')

#Tabela livro
cursor.execute('CREATE TABLE livro(\
               id_livro INTEGER PRIMARY KEY AUTOINCREMENT, \
               titulo VARCHAR(50),\
               editora VARCHAR(50));')

#Tabela autor_livro
cursor.execute('CREATE TABLE autor_livro(\
               id_autor INTEGER,\
               id_livro INTEGER, \
               PRIMARY KEY (id_autor, id_livro),\
               FOREIGN KEY(id_autor) REFERENCES autor(id_autor),\
               FOREIGN KEY(id_livro) REFERENCES livro(id_livro));')
#Tabela genero
cursor.execute('CREATE TABLE genero(\
               id_genero INTEGER PRIMARY KEY AUTOINCREMENT,\
                genero VARCHAR(30));')

#Tabela genero_livro
cursor.execute('CREATE TABLE genero_livro(\
               id_livro INTEGER,\
               id_genero INTEGER,\
               PRIMARY KEY (id_livro, id_genero),\
               FOREIGN KEY(id_livro) REFERENCES livro(id_livro),\
               FOREIGN KEY(id_genero) REFERENCES genero(id_genero));')

#Tabela exemplar
cursor.execute('CREATE TABLE exemplar(\
               id_exemplar INTEGER PRIMARY KEY AUTOINCREMENT,\
               id_livro INTEGER,\
               total_exemplar INTEGER,\
               total_disponivel INTEGER, \
               max_renovacao INTEGER,\
               FOREIGN KEY(id_livro) REFERENCES livro(id_livro));')

#Tabela emprestimos
cursor.execute('CREATE TABLE emprestimo(\
               id_emprestimo INTEGER PRIMARY KEY AUTOINCREMENT,\
               id_usuario INTEGER,\
               id_exemplar INTEGER,\
               data_emprestimo DATETIME,\
               data_devolucao DATETIME,\
               estado varchar (30),\
               FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario),\
               FOREIGN KEY(id_exemplar) REFERENCES exemplar(id_exemplar));')

#Tabela biblioteca
cursor.execute('CREATE TABLE biblioteca(\
               id_biblioteca INTEGER,\
               id_usuario INTEGER,\
               id_livro INTEGER,\
               id_emprestimo INTEGER,\
               PRIMARY KEY (id_biblioteca, id_usuario, id_livro, id_emprestimo),\
               FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario),\
               FOREIGN KEY(id_livro) REFERENCES livro(id_livro),\
               FOREIGN KEY(id_emprestimo) REFERENCES emprestimo(id_emprestimo));')

conectar.commit()
conectar.close()