# RegistrationFC = Employee and customer registration

class Pessoa:
    def __init__(self,nome ,cpf, data_nascimento):
        self.nome = ""
        self.cpf = ""
        self.data_nascimento = ""
    def mostrar(self):
        print(F"Olá, o meu nome é {self.nome} nasci em {self.data_nascimento} e o meu cpf é {self.cpf}")
pessoa_one = Pessoa("João","12345678910","16/11/2004")
pessoa_one.mostrar()