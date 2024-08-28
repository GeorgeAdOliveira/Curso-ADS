class Livro:
    def __init__(self, titulo, autor, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel


class SistemaBiblioteca:
    def __init__(self):
        self.livros = []

    def cadastrar_livro(self, titulo, autor):
        livro = Livro(titulo, autor)
        self.livros.append(livro)
        print(f'O livro "{titulo}" de {autor} foi cadastrado.')

    def excluir_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                self.livros.remove(livro)
                print(f'O livro "{titulo}" foi excluído.')
                return
        print(f'O livro "{titulo}" não foi encontrado.')

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower() and livro.disponivel:
                livro.disponivel = False
                print(f'O livro "{titulo}" foi emprestado.')
                return
        print(f'O livro "{titulo}" não está disponível para empréstimo ou não foi encontrado.')

    def entregar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower() and not livro.disponivel:
                livro.disponivel = True
                print(f'O livro "{titulo}" foi entregue.')
                return
        print(f'O livro "{titulo}" não foi encontrado ou não está emprestado.')

    def listar_livros(self):
        for livro in self.livros:
            status = "Disponível" if livro.disponivel else "Emprestado"
            print(f'Título: {livro.titulo}, Autor: {livro.autor}, Status: {status}')

# Exemplo de uso
biblioteca = SistemaBiblioteca()

biblioteca.cadastrar_livro("Dom Casmurro", "Machado de Assis")
biblioteca.cadastrar_livro("1984", "George Orwell")

biblioteca.listar_livros()

biblioteca.emprestar_livro("Dom Casmurro")

biblioteca.listar_livros()

biblioteca.entregar_livro("Dom Casmurro")

biblioteca.listar_livros()

biblioteca.excluir_livro("1984")

biblioteca.listar_livros()
