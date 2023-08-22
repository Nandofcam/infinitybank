from banco import obterConta, banco

def depositar(conta: int, valor: float) -> None:
    cliente = obterConta(conta)
    if cliente:
        cliente['saldo'] += valor
        print('Depósito realizado com sucesso!')
        print(f"Novo saldo de: R$ {cliente['saldo']}")
    else:
        print('Conta não cadastrada!')

if __name__ == "__main__":
    depositar(2, 250)