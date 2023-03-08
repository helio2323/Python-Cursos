import abc

class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor: float) -> float: ...

    def depositar(self, valor: float)-> float:
        self.saldo += valor
        self.detalhes(f'DEPÓSITO {valor}')

    def detalhes(self, msg: str='') -> None:
        print(f'O seu saldo é {self.saldo:.2f} {msg}')

class ContaPoupanca(Conta):

        def sacar(self, valor):
            valor_pos_saque = self.saldo - valor

            if valor_pos_saque < 0:
                self.detalhes('Você não tem saldo suficiente para realizar este saque...')
                return self.saldo 
            elif valor_pos_saque >= 0:
                self.saldo -= valor
                self.detalhes(f'SAQUE {valor}')
                return self.saldo 
class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float=0, limite: float=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque < limite_maximo:
            self.detalhes(f'Você não tem saldo suficiente para realizar este saque... seu limite máximo é de {self.limite:.2f}')
            return self.saldo 
        elif valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'SAQUE {valor}')
            return self.saldo                

if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222, 50) 
    cp1.sacar(40)
    cp1.depositar(150)
    cp1.detalhes()
    print("##")
    cc1 = ContaCorrente(111, 222, 0, 100) 
    cc1.sacar(120)
 