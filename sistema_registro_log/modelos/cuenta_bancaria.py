class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        """
        Constructor:
        Inicializa la cuenta bancaria con el titular y saldo inicial.
        """
        self.titular = titular
        self.saldo = saldo_inicial
        print(f"[INIT] Cuenta creada para {self.titular} con saldo ${self.saldo}")

    def depositar(self, monto):
        self.saldo += monto
        print(f"Depósito exitoso. Saldo actual: ${self.saldo}")

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro exitoso. Saldo actual: ${self.saldo}")
        else:
            print("Fondos insuficientes.")

    def mostrar_saldo(self):
        print(f"Titular: {self.titular} | Saldo: ${self.saldo}")

    def __del__(self):
        """
        Destructor:
        Registra cuando la cuenta deja de existir.
        Puede ejecutarse al finalizar el programa.
        """
        print(f"[DEL] La cuenta de {self.titular} ha sido cerrada.")
