class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "Ponto na posição X: {:.2f} e Y: {:.2f} \n".format(self.x, self.y)

class Retangulo:
    def __init__(self, largura, altura, ponto_inicio):
        self.largura = largura
        self.altura = altura
        self.ponto_inicio = ponto_inicio

    def centro_retangulo(self):
        x = self.ponto_inicio.x + (self.largura / 2)
        y = self.ponto_inicio.y + (self.altura / 2)
        centro = Ponto(x, y)
        print("Centro:", centro)

    def __str__(self):
        return "Retângulo: largura: {} altura: {} \nInicio em x: {} e y: {} \n".format(
        self.largura, self.altura, self.ponto_inicio.x, self.ponto_inicio.y)
    

def menu(largura, altura, x, y):
    ret = criar_retangulo(largura, altura, x, y)
    executar = True

    while executar:
        print("\n")
        print(ret)
        print("1 - Criar Retângulo")
        print("2 - Ver centro")
        print("3 - Sair")
        op = input("Selcione uma opção = ")
        print()

        if op == "1":
            ret = criar_retangulo(largura, altura,x,y)

        elif op == "2":
            ret.centro_retangulo()
            cont = input("Pressione qualquer tecla para continuar...")
        elif op == "3":
            executar = False

def criar_retangulo(largura, altura, x, y):
    print("------ Criar Retangulo ------")

    inicio = Ponto(0, 0)
    ret = Retangulo(5, 5, inicio)
    ret.largura = largura
    ret.altura = altura
    inicio = Ponto(x, y)
    ret.ponto_inicio = inicio

    return ret

largura = float(input("Largura: "))
altura = float(input("Altura: "))
x = float(input("Eixo X: "))
y = float(input("Eixo Y: "))
menu(largura, altura,x,y)
criar_retangulo(largura, altura,x,y)

menu()

