
import sqlite3

conexao = sqlite3.connect('banco-de-dados')
cursor = conexao.cursor()

#cursor.execute('CREATE TABLE usuario (id_usuario INTEGER PRIMARY KEY, nome VARCHAR (100), telefone INT, nacionalidade VARCHAR(100));')
cursor.execute('CREATE TABLE livro (id_livro INTEGER PRIMARY KEY, titulo VARCHAR (200), editora VARCHAR (200));')

cursos.execute

conexao.commit()
conexao.close