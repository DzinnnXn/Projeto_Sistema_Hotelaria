class Quarto:
    def __init__(self, tipo, qtd, capacidade, valor, desc):
        self.tipo = tipo
        self.qtd = qtd
        self.capacidade = capacidade
        self.valor = valor
        self.desc = desc

    def reservar(self):
        if self.qtd > 0:
            self.qtd -= 1
            return True
        else:
            return False

    def cancelarReserva(self):
        self.qtd += 1

class Hotel:
    def __init__(self, nome, endereco, cnpj):
        self.nome = nome
        self.endereco = endereco
        self.cnpj = cnpj
        self.clientes = {}
        self.reservas = []
        self.quartos = {
            "Deluxe": Quarto("Deluxe", 2, 4, 500, "Quarto de luxo: Quarto com varanda, cama de casal e hidromassagem"),
            "Casal": Quarto("Casal", 4, 2, 300, "Quarto de casal: Quarto com cama de casal"),
            "Solteiro": Quarto("Solteiro", 8, 1, 150, "Quarto de solteiro: Quarto com cama de solteiro")
        }

    def cadastrarCliente(self, id, nome, cpf, tel):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.tel = tel
        self.clientes[self.id] = [self.nome, self.cpf, self.tel]

    def listarClientes(self):
        for chave, valor in self.clientes.items():
            print(f"ID:{chave} - Nome: {valor[0]} - CPF: {valor[1]} - Telefone: {valor[2]}")

    def reservarQuarto(self, nome_cliente, data_inicio, data_fim, tipo_quarto):
        quarto = self.quartos.get(tipo_quarto)
        if quarto:
            if quarto.reservar():
                self.reservas.append({"cliente": nome_cliente, "data_inicio": data_inicio, "data_fim": data_fim, "tipo": tipo_quarto})
                print(f"Quarto {tipo_quarto} reservado para {nome_cliente} de {data_inicio} a {data_fim}.")
            else:
                print(f"Quarto {tipo_quarto} indisponível para reserva.")
        else:
            print("Tipo de quarto inválido.")

    def listarReservas(self):
        if self.reservas:
            print("Reservas do quarto:")
            for reserva in self.reservas:
                print(f"Cliente: {reserva['cliente']}, Data de Início: {reserva['data_inicio']}, Data de Fim: {reserva['data_fim']}")
        else:
            print("Nenhuma reserva para este quarto.")

    def cancelarReserva(self, nome_cliente):
        for reserva in self.reservas[:]:
            if reserva["cliente"] == nome_cliente:
                tipo_quarto = reserva["tipo"]
                quarto = self.quartos.get(tipo_quarto)
                if quarto:
                    quarto.cancelarReserva()
                self.reservas.remove(reserva)
                print(f"Reserva para {nome_cliente} cancelada com sucesso.")
                break
        else:
            print(f"Não foi encontrada nenhuma reserva para {nome_cliente}.")

    def disponibilidadeQuarto(self):
        for tipo_quarto, quarto in self.quartos.items():
            print(f"Quarto {tipo_quarto} - Disponíveis: {quarto.qtd}, Capacidade: {quarto.capacidade}")