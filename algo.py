from classes import *
import os

def pausar():
    os.system("pause")
    
def cls():
    os.system("cls")
    
def main():
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
        print("")
        print("Qual opção deseja?")
        menu = int(input(">> "))
        match menu:
            case 1:
                cls()
                pausar()
            
            case 2:
                cls()
                pausar()
            
            case 3:
                cls()
                pausar()
            
            case 4:
                cls()
                pausar()
            
            case 5:
                cls()
                pausar()
            
            case 6:
                cls()
                pausar()
            
            case 0:
                print("Saindo...")
                pausar()
                break
            
    