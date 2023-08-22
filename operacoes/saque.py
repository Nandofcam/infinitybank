from banco import obterConta, banco

def sacar(conta: int, valor: float) -> None:
    cliente = obterConta(conta)
    if cliente:
        if cliente['saldo'] >= valor:
            cliente['saldo'] -= valor
            print('Saque realizado com sucesso!')
            print(f"Seu novo saldo é de: R${cliente['saldo']}")
        else:
            print('Saldo insuficiente!')
            print(f"Saldo atual de: R${cliente['saldo']}")
    else:
        print('Conta não cadastrada!')

if __name__ == '__main__': # Executa somente a página que se está editando, sem esse comando todos os arquivos seriam executados
    sacar(1, 1000)
    print(banco)