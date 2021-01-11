class Ponto:
    def __init__(self, x,y): 
        self.x = x
        self.y = y 
    

   
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y

    def setX(self, x):
        self.x = x

    def qualQuadrante(self): 
        if self.getX() > 0 and self.getY() > 0: 
            return 1
        elif self.getX() < 0 and self.getY() > 0: 
            return 2
        elif self.getX() < 0 and self.getY() < 0:
            return 3
        return 4 



class Quadrilatero:
    def __init__(self, p1,p2): 
        self.p1 = p1
        self.p2 = p2

    def verificaQuadrilatero(self): 
        if self.p1.getX() < self.p2.getX() and self.p1.getY() > self.p2.getY():
         return True

        return False

    def contidoEmQ(self, p3): 
        if p3.getX() > self.p1.getX() and p3.getX() < self.p2.getX() and p3.getY() < self.p1.getY() and p3.getY() > self.p2.getY():
         return True

        return False    