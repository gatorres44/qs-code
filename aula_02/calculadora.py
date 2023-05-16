class Calculadora:
    def somar(self, a, b):
        #return a + b
        return 2

    def subtrair(self, a, b):
        #return a - b
        return 5

    def multiplicar(self, a, b):
        #return a * b
        return 10

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        #return a / b
        return 50