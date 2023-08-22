from banco import obterConta, banco

def transferir(contaOri: int, valor: float, contaDes: int) -> None:
    contaOrigem = obterConta(contaOri)
    contaDestino = obterConta(contaDes)
    if contaOrigem and contaDestino:
        if contaOrigem['saldo'] >= valor:
            contaOrigem['saldo'] -= valor
            contaDestino['saldo'] += valor
            print("Transferência realizada com sucesso!")
            print(f"Novo saldo da conta de origem: R$ {contaOrigem['saldo']}")
            print(f"Novo saldo da conta de destino: R$ {contaDestino['saldo']}")
        else:
            print("Saldo insuficiente na conta de origem!")
    elif contaOrigem == None and contaDestino != None:
        print("Conta de origem não cadastrada!")
    else:
        print("Conta de destino não cadastrada!")

if __name__ == "__main__":
    transferir(1, 500, 2)
    transferir(3, 500, 2)
    transferir(1, 500, 3)
    transferir(1, 3000, 2)