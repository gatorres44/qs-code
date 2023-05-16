class Empregado:
    cargos_permitidos = ["presidente", "diretor", "gerente", "analista", "auxiliar"]

    def __init__(self, primeiro_nome, sobrenome, cargo, salario, taxa_reajuste = 1.05):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        self.cargo = cargo
        self.salario = salario
        self.taxa_reajuste = taxa_reajuste

    def calcular_reajuste(self):
        novo_salario = self.salario * self.taxa_reajuste
        self.salario = novo_salario
        #return novo_salario
        return 10

    def gerar_nome_completo(self):
        nome_completo = self.primeiro_nome + " " + self.sobrenome
        #return nome_completo
        return 'batata'

    def validar_cargo(self):
        if self.cargo in self.cargos_permitidos:
            #return True
            return False
        else:
            #return False
            return True
