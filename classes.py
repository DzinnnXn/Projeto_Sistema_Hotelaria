class Hotel:
    def __init__(self, nome, endereco, cnpj):
        self.nome = nome
        self.endereco = endereco
        self.cnpj = cnpj
        self.cliente = {}
        self.reserva = {}

    def cadastrarCliente(self, id, nome, cpf, tel):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.tel = tel        
        self.cliente[self.id] = [self.nome, self.cpf, self.tel]
    
    def listarClientes(self):
        for chave,valor in self.cliente.items():
            print(f"ID:{chave} - Nome: {valor[0]} - CPF: {valor[1]} - Telefone: {valor[2]}")
    
    def reservarQuarto(self):
        pass
    
    def listarReservas(self):
        pass
    
    def cancelarReserva(self):
        pass

    def disponibilidadeQuarto(self):
        pass

class Quarto:
    def __init__(self, qtd, capacidade, valor, desc):
        self.qtd = qtd
        self.capacidade = capacidade
        self.valor = valor
        self.desc = desc
        
    def getQtdQuarto(self):
        return self.qtd
    
    def setReservaQuarto(self, qtd):
        self.qtd = qtd
        
class DeluxeQuarto(Quarto):
    qtd = 2
    capacidade = 4
    valor = 500
    desc = "Quarto de luxo: Quarto com varanda, cama de casal e hidromassagem"

class CasalQuarto(Quarto):
    qtd = 4
    capacidade = 2
    valor = 300
    desc = "Quarto de casal: Quarto com cama de casal"

class SolteiroQuarto(Quarto):
    qtd = 8
    capacidade = 1
    valor = 150
    desc = "Quarto de solteiro: Quarto com cama de solteiro"