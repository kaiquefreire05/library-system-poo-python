import textwrap
from datetime import datetime, timedelta

class Pessoa:  # Vai servir de base para a classe Autor e Usuário
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    # Fazendo os getters

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

# Objeto Usuário
class Usuario(Pessoa):
    def __init__(self, nome, idade, id_usuario):
        super().__init__(nome, idade)
        self.id_usuario = id_usuario
        self.livros_posse = []

    def pegar_livro(self, livro):
        if livro in self.livros_disponiveis:  # Se o livro estiver na lista de livros disponiveis
            self.livros_posse.append(livro)  # Vai adicionar o livro na lista de livros em posse

    def devolver_livro(self, livro):
        if livro in self.livros_posse:
            self.livros_posse.remove(livro)  # Se o obj livro estiver na lista de livros_posse ele vai remover

# Objeto livro
class Livro:
    def __init__(self, titulo, autor, isbn):
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn  # Id no livro
        self._disponivel_para_emprestimo = True

    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def isbn(self):
        return self._isbn

    @property
    def esta_disponivel(self):
        return self._disponivel_para_emprestimo

# Objeto emprestimo
class Emprestimo:
    def __init__(self, livro, usuario):
        self.livro = livro
        self.usuario = usuario
        self._data_emprestimo = datetime.now()
        self._data_devolucao = None  # Começa com None
    
    @property
    def data_emprestimo(self):
        return self._data_emprestimo

    def realizar_emprestimo(self):
        if self.livro.esta_disponivel:  # Somente o funcionário pode usar essa função
            self._disponivel_para_emprestimo = False  # Vai ser mudado diretamente na variável
            print(f"Empréstimo realizado com sucesso em {self._data_emprestimo}.")
        else:
            print(f"Livro não está disponível para empréstimo.")

class Biblioteca:
    def __init__(self):
        self.livros_disponiveis = []
        self.usuarios_cadastrados = []
        self.historico_emprestimos = []

    def adicionar_livro(self, livro):
        self.livros_disponiveis.append(livro)
    
    def listar_livros_disponiveis(self):
        for l in self.livros_disponiveis:
            print(f"Título:\t{l.titulo}")

    def realizar_emprestimo_biblioteca(self, livro, usuario):
        if livro.esta_disponivel:
            emprestimo = Emprestimo(livro, usuario)
            self.historico_emprestimos.append(emprestimo)
            print(f"Empréstimo realizado com sucesso em {emprestimo._data_emprestimo}.")
        else:
            print(f"Livro não está disponível para empréstimo.")
            
    def criar_historico(self):
        for emp in self.historico_emprestimos:
            print(f"Livro: {emp.livro.titulo}", end=", ")
            print(f"Retirado por: {emp.usuario.nome}")


def main():
    # Criando objetos
    livro1 = Livro("O Hobbit", "J.R.R. Tolkien", "9788501006314")
    livro2 = Livro("A Guerra dos Tronos", "George R.R. Martin", "9788501006307")
    usuario1 = Usuario("Fulano", 25, 123456)
    usuario2 = Usuario("Beltrano", 30, 789012)

    # Adicionando livros à biblioteca
    biblioteca = Biblioteca()
    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)

    # Realizando empréstimos
    biblioteca.realizar_emprestimo_biblioteca(livro1, usuario1)
    biblioteca.realizar_emprestimo_biblioteca(livro2, usuario2)

    # Listando livros disponíveis
    biblioteca.listar_livros_disponiveis()

    # Listando histórico de empréstimos
    biblioteca.criar_historico()


if __name__ == "__main__":
    main()
