class ContaBancaria:
    def __init__(self, id, titular, saldo=0):
        self.id = id
        self.titular = titular
        self.__saldo = saldo        # atributo privado (encapsulamento)
        print(f"Conta {self.id} criada com sucesso. Saldo atual de R${self.__saldo:,.2f}")

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo."

    @property
    def saldo(self):                # getter
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):         # setter com validação
        if valor < 0:
            print("Erro: saldo não pode ficar negativo!")
        else:
            self.__saldo = valor

    def depositar(self, valor):
        self.saldo += valor         # usa o setter por trás dos panos
        print(f"Depósito de R${valor:,.2f} autorizado na conta {self.id}")

    def sacar(self, valor):
        if valor > self.__saldo:
            print(f"Saque NEGADO de R${valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} autorizado na conta {self.id}")


class ContaPoupanca(ContaBancaria):   # HERANÇA: ContaPoupanca é uma ContaBancaria
    def __init__(self, id, titular, saldo=0, taxa_rendimento=0.005):
        super().__init__(id, titular, saldo)   # reaproveita o __init__ da mãe
        self.taxa_rendimento = taxa_rendimento

    def render(self):
        rendimento = self.saldo * self.taxa_rendimento
        self.saldo += rendimento
        print(f"Rendimento de R${rendimento:,.2f} aplicado na conta {self.id}")

    def __str__(self):                # sobrescreve o __str__ da mãe
        return super().__str__() + f" (Poupança, taxa de {self.taxa_rendimento*100:.2f}%)"


# ---- testando ----
c1 = ContaBancaria(id=112, titular="Gustavo", saldo=3000)
c1.depositar(500)
c1.sacar(2_000_000)
print(c1)

print("-" * 50)

p1 = ContaPoupanca(id=200, titular="Ana", saldo=1000, taxa_rendimento=0.01)
p1.depositar(200)
p1.render()
print(p1)