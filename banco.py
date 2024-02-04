import sqlite3

conexao = sqlite3.connect('banco-de-dados')
cursor = conexao.cursor()

##Tabela de Autores
cursor.execute('CREATE TABLE Autor(autor_id INT AUTO_INCREMENT PRIMARY KEY,nome_autor VARCHAR(255) NOT NULL,nacionalidade VARCHAR(100));')

##Tabela de Gêneros
cursor.execute('CREATE TABLE Genero(genero_id INT AUTO_INCREMENT PRIMARY KEY,nome_genero VARCHAR(50) NOT NULL);')

##Tabela de Livros
cursor.execute('CREATE TABLE Livro(livro_id INT AUTO_INCREMENT PRIMARY KEY,titulo VARCHAR(255) NOT NULL,editora VARCHAR(100),renovacoes_maximas INT, FOREIGN KEY (editora) REFERENCES Autor(autor_id));')

##Tabela de Livros_Generos (relacionamento muitos-para-muitos)
cursor.execute('CREATE TABLE Livro_Genero(livro_id INT,genero_id INT,PRIMARY KEY (livro_id, genero_id),FOREIGN KEY (livro_id) REFERENCES Livro(livro_id),FOREIGN KEY (genero_id) REFERENCES Genero(genero_id));')

##Tabela de Exemplares
cursor.execute('CREATE TABLE Exemplar(exemplar_id INT AUTO_INCREMENT PRIMARY KEY,livro_id INT,disponivel BOOLEAN NOT NULL DEFAULT TRUE, FOREIGN KEY (livro_id) REFERENCES Livro(livro_id));')

##Tabela de Usuários
cursor.execute('CREATE TABLE Usuario(usuario_id INT AUTO_INCREMENT PRIMARY KEY, nome_usuario VARCHAR(255) NOT NULL,telefone VARCHAR(15) NOT NULL,nacionalidade VARCHAR(100) NOT NULL);')

##Tabela de Empréstimos
cursor.execute('CREATE TABLE Emprestimo(emprestimo_id INT AUTO_INCREMENT PRIMARY KEY,usuario_id INT,exemplar_id INT,data_emprestimo DATE NOT NULL,data_devolucao DATE,estado_exemplar VARCHAR(15) NOT NULL, FOREIGN KEY (usuario_id) REFERENCES Usuario(usuario_id),FOREIGN KEY (exemplar_id) REFERENCES Exemplar(exemplar_id));')

cursor.execute

conexao.commit()
conexao.close