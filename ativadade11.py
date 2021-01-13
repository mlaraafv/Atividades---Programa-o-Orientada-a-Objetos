import unittest
from atividade3 import Ponto, Quadrilatero 
ponto1 = Ponto(1,4)
ponto2 = Ponto(7,2)
quad = Quadrilatero(ponto1,ponto2)
class Teste(unittest.TestCase):
    def setUp(self): 
        self.ponto = Ponto (5,3)
        self.quadrilatero = quad

    def teste_QuadranteDoPonto(self): 
        self.assertEqual(self.ponto.qualQuadrante(), 1)
        self.assertEqual(ponto1.qualQuadrante(), 1)
        
    
    def testarSeEQuadrilatero(self): 
        self.assertEqual(self.quadrilatero.verificaQuadrilatero(), True)

    def test_verificaSeOPpontoEstaContido(self):
        self.assertEqual(self.quadrilatero.contidoEmQ(self.ponto),True)

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)