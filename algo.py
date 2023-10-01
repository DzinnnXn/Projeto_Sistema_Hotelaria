from classes import *
import os

def pausar():
    os.system("pause")

def cls():
    os.system("cls")

def main():
    hotel = Hotel("Ibis", "Jundiaí - SP", "987654321")

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
                id = len(hotel.clientes) + 1
                nome = input("Nome - ")
                cpf = int(input("CPF - "))
                tel = int(input("Telefone - "))
                hotel.cadastrarCliente(id, nome, cpf, tel)
                print("CLIENTE CADASTRADO")
                print("--------")
                pausar()

            case 2:
                cls()
                hotel.disponibilidadeQuarto()
                pausar()
                
            case 3:
                cls()
                print("--- RESERVAR QUARTO ---")
                print("Escolha o tipo de quarto:")
                print("1 - Quarto Deluxe")
                print("2 - Quarto de Casal")
                print("3 - Quarto Solteiro")
                tipo_quarto = input(">> ")
                if tipo_quarto in ["1", "2", "3"]:
                    nome_cliente = input("Nome do Cliente: ")
                    data_inicio = input("Data de Início da Reserva (dd/mm/aaaa): ")
                    data_fim = input("Data de Fim da Reserva (dd/mm/aaaa): ")
                    tipo_quarto = {
                        "1": "Deluxe",
                        "2": "Casal",
                        "3": "Solteiro"
                    }.get(tipo_quarto)

                    if tipo_quarto:
                        hotel.reservarQuarto(nome_cliente, data_inicio, data_fim, tipo_quarto)
                    else:
                        print("Opção inválida.")
                else:
                    print("Opção inválida.")
                pausar()

            case 4:
                cls()
                print("--- CANCELAR RESERVA ---")
                nome_cliente = input("Nome do Cliente: ")
                hotel.cancelarReserva(nome_cliente)
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
