from banco import *
from operacoes.transferencia import transferir
from operacoes.saque import sacar
from operacoes.consulta import consultarSaldo
from operacoes.deposito import depositar

def menu():
    while True:
        print("------ BEM VINDO AO BANCO INFINITY ------")
        print("1 - Adicionar conta")
        print("2 - Alterar nome")
        print("3 - Consultar conta")
        print("4 - Remover conta")
        print("5 - Listar contas")
        print("6 - Realizar saque")
        print("7 - Realizar depósito")
        print("8 - Consultar saldo")
        print("9 - Realizar transferência")
        print("10 - Sair")
        opcao = int(input("Selecione uma opção: "))

        if opcao == 1:
            nome = input("Digite o nome do cliente: ")
            saldo = input("Digite o saldo inicial: ")
            adicionarConta(nome, saldo)
            print(banco)

        elif opcao == 2:
            conta = int(input("Digite o número da conta: "))
            novo_nome = input("Digite o novo nome do cliente: ")
            atualizarNome(conta, novo_nome)
            print(banco)

        elif opcao == 3:
            conta = int(input("Digite o número da conta: "))
            print(obterConta(conta))

        elif opcao == 4:
            conta = int(input("Digite o número da conta: "))
            deletarConta(conta)

        elif opcao == 5:
            listarContas()

        elif opcao == 6:
            conta = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor que deseja sacar: "))
            sacar(conta, valor)

        elif opcao == 7:
            conta = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor que deseja depositar: R$ "))
            depositar(conta, valor)

        elif opcao == 8:
            conta = int(input("Digite o número da conta: "))
            consultarSaldo(conta)

        elif opcao == 9:
            contaOri = int(input("Digite o número da conta de origem: "))
            valor = float(input("Digite o valor que se deseja transferir: R$ "))
            contaDes = int(input("Digite o número da conta de destino: "))
            transferir(contaOri, valor, contaDes)

        elif opcao == 10:
            break

if __name__ == "__main__": # Executa somente a página que se está editando, sem esse comando todos os arquivos seriam executados
    menu()