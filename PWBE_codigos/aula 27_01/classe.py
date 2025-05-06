
class Cachorro:
    def __init__(self, nome, raca, cor, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def latir(self):
        print(f"{self.nome} diz: au au")
    
    def correr(self):
        print(f"{self.nome} correu {self.idade} km")

    
cachorro_da_luana = Cachorro("Pituco", "Vira-Lata", "Caramelo", 15)

cachorro_da_luana.correr()

###############################################################################

class Livro:
    def __init__(self, categoria, titulo, autor, personagens, indicacao):
        self.genero = categoria
        self.titulozinho = titulo
        self.escritor = autor
        self.indicacao = indicacao
        self.personagens = personagens

    
    def abrir(self, pagina):
        print(f"O livro {self.titulozinho} foi aberto na página {pagina}")

    def __str__(self):
        return f"{self.titulozinho} do genero {self.genero} escrito por {self.escritor}"
    
livro_da_kamila = Livro("Romance", "Crepúsculo", "J.K Rowling", ["Bela", "Edward"], 14)
livro_da_kamila.abrir(10)

print(livro_da_kamila)