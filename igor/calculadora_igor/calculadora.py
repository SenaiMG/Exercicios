class Calculadora:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def soma(self):
        return self.num1 + self.num2
       
    def subtracao(self):
        return self.num1 - self.num2
       
    def multiplicacao(self):
        return self.num1 * self.num2

    def divisao(self):
        return self.num1/self.num2
        

c = Calculadora(10,2)
print("Soma:", c.soma())               
print("Subtração:", c.subtracao())     
print("Multiplicação:", c.multiplicacao())  
print("Divisão: ", c.divisao())

