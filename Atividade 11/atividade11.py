from atividade3 import Ponto, Quadrilatero 

class Teste:
    def __init__(self, ponto, quadrilatero): 
        self.ponto = ponto
        self.quadrilatero = quadrilatero

    def testarQuadranteDoPonto(self,ponto): 
        print("O quadrante desse ponto é " + str(ponto.qualQuadrante()))
    
    def testarSeEQuadrilatero(self):
        if self.quadrilatero.verificaQuadrilatero():
            print("É um quadrilátero")
        
        else:
            print("Não é um quadrilátero")
    
    def verificaSeOPpontoEstaContido(self): 
        if self.quadrilatero.contidoEmQ(self.ponto):
            print("Está contido em Q")
        
        else:
            print("Não está contido em Q")


ponto1 = Ponto(1,4)
ponto2 = Ponto(7,2)
ponto3 = Ponto (5,3) 

quad = Quadrilatero(ponto1,ponto2) 

teste = Teste(ponto3,quad) 


teste.testarQuadranteDoPonto(ponto1) 
teste.testarQuadranteDoPonto(ponto2)
teste.testarQuadranteDoPonto(ponto3) 

teste.testarSeEQuadrilatero()

teste.verificaSeOPpontoEstaContido()