# Importando as classes necessárias
from livro import Livro
from cliente import Cliente
from funcionario import Funcionario
from exemplar import Exemplar
from emprestimo import Emprestimo
from biblioteca import Biblioteca

# Observações:
# Por questões de simplificação, tratamento de erros não foram implementados, ou seja,
# consideramos que sempre serão passados argumentos válidos em qualquer situação.
# Métodos abstratos também não foram implementados.

# Implementar: renovações máximas

# Instanciando o gerenciador
biblioteca = Biblioteca("PyLib")