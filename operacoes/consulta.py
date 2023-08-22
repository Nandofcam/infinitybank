from banco import obterConta, banco

def consultarSaldo(conta: int) -> None:
    cliente = obterConta(conta)
    if cliente:
        print(f"Seu saldo é de R$ {cliente['saldo']}")
    else:
        print("Conta não cadastrada!")

if __name__ == "__main__":
    consultarSaldo(1)