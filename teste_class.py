"""class saudação:
    def exibir_mensagem(self):
        print("olá,mundo")
objeto = saudação()
objeto.exibir_mensagem"""

class Amigo:
    def __init__(self):
        self.nome = ""
        self.idade = 0
    def apresentar (self, seu_nome, sua_idade):
        self.nome = seu_nome
        self.idade = sua_idade
    def define_nome(self, novo_nome):
        self.nome = novo_nome
    def define_idade(self,novo_idade):
        self.idade = novo_idade
    def mostra_nome(self):
        print(f"Nome: {self.nome}")
    def mostra_idade(self):
        print(f"Idade: {self.idade}")

pessoa1 = Amigo()
pessoa1.apresentar("João",25)
pessoa1.define_nome("Maria")
pessoa1.define_idade(12)
pessoa1.mostra_nome()
pessoa1.mostra_idade()

pessoa2 = Amigo()
pessoa2.apresentar("João",25)
pessoa2.mostra_nome()
pessoa2.mostra_idade()
