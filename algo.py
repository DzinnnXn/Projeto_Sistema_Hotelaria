from classes import *
import os

def pausar():
    os.system("pause")
    
def cls():
    os.system("cls")
    
def main():
    hotel = Hotel("Ibis", "Jundiaí - SP", "987654321")
    quartos = [
        {"tipo": "Deluxe", "qtd": 2, "capacidade": 4, "valor": 500, "desc": "Quarto de luxo: Quarto com varanda, cama de casal e hidromassagem"},
        {"tipo": "Casal", "qtd": 4, "capacidade": 2, "valor": 300, "desc": "Quarto de casal: Quarto com cama de casal"},
        {"tipo": "Solteiro", "qtd": 8, "capacidade": 1, "valor": 150, "desc": "Quarto de solteiro: Quarto com cama de solteiro"}
    ]

    s = 0 
    while s == 0:
        cls()
        print("---MENU---")
        print("01 - CADASTRAR CLIENTE")
        print("02 - DISPONIBILIDADE DE QUARTOS")
        print("03 - RESERVAR QUARTO")
        print("04 - CANCELAR RESERVA")
        print("05 - LISTAR CLIENTES")
        print("06 - LISTAR RESERVAS")
        print("00 - SAIR")
        print("--------")
        menu = int(input(">> "))
        match menu:
            case 1:
                cls()
                print("--------------------------")
                print("    CADASTRO DE CLIENTE   ")
                print("--------------------------")
                print("INFORME OS SEUS DADOS")
                id = len(hotel.cliente) + 1  
                nome = input("Nome - ")
                cpf = int(input("CPF - "))
                tel = int(input("Telefone - "))                    
                hotel.cadastrarCliente(id, nome, cpf, tel)
                print("CLIENTE CADASTRADO")
                print("--------")
                pausar()
            
            case 2:
                cls()
                print("------------------------")
                print("    QUARTO DELUXE     ")
                print("------------------------")
                print("Quantidade:", quartos[0]["qtd"])
                print("Capacidade:", quartos[0]["capacidade"])
                print("Valor:", quartos[0]["valor"])
                print("Descrição:", quartos[0]["desc"])
                print("")
                print("------------------------")
                print("    QUARTO DE CASAL     ")
                print("------------------------")
                print("Quantidade:", quartos[1]["qtd"])
                print("Capacidade:", quartos[1]["capacidade"])
                print("Valor:", quartos[1]["valor"])
                print("Descrição:", quartos[1]["desc"])
                print("")
                print("------------------------")
                print("    QUARTO SOLTEIRO     ")
                print("------------------------")
                print("Quantidade:", quartos[2]["qtd"])
                print("Capacidade:", quartos[2]["capacidade"])
                print("Valor:", quartos[2]["valor"])
                print("Descrição:", quartos[2]["desc"])
                pausar()
                
            case 3:
                cls()
                print("--- RESERVAR QUARTO ---")
                print("Escolha o tipo de quarto:")
                print("1 - Quarto Deluxe")
                print("2 - Quarto de Casal")
                print("3 - Quarto Solteiro")
                tipo_quarto = int(input(">> "))
                if tipo_quarto >= 1 and tipo_quarto <= 3:
                    nome_cliente = input("Nome do Cliente: ")
                    data_inicio = input("Data de Início da Reserva: ")
                    data_fim = input("Data de Fim da Reserva: ")
                    hotel.reservarQuarto(nome_cliente, data_inicio, data_fim, quartos[tipo_quarto - 1]["tipo"])
                else:
                    print("Opção inválida.")
                pausar()
            
            case 4:
                cls()
                print("--- CANCELAR RESERVA ---")
                nome_cliente = input("Nome do Cliente: ")
                for reserva in hotel.reservas[:]:
                    if reserva["cliente"] == nome_cliente:
                        tipo_quarto = reserva["tipo"]
                        for quarto in quartos:
                            if quarto["tipo"] == tipo_quarto:
                                quarto["qtd"] += 1
                        hotel.reservas.remove(reserva)
                        print(f"Reserva para {nome_cliente} cancelada com sucesso.")
                        break
                else:
                    print(f"Não foi encontrada nenhuma reserva para {nome_cliente}.")
                pausar()
            
            case 5:
                cls()
                hotel.listarClientes()
                pausar()
            
            case 6:
                cls()
                hotel.listarReservas()
                pausar()
            
            case 0:
                print("Saindo...")
                pausar()
                break
