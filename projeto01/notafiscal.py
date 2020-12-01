"""
    Módulo notafiscal -
    Classe NotaFiscal - 
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado. 
"""
import datetime
from cliente        import Cliente
from produto        import Produto
from itemnotafiscal import ItemNotaFiscal


class NotaFiscal():         
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo=codigo
        self._cliente=cliente 
        self._data=datetime.datetime.today()   
        self._itens=[]
        self._valorNota=0.0        
        
    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente=cliente    
            
    def adicionarItem(self, item): 
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)
        
    def calcularNotaFiscal(self):
        valor=0.0
        for item in self._itens:
            valor += item._valorItem
        self.valorNota=valor
     
    def imprimirNotaFiscal(self):    
        print("-" * 100)   
        print("NotaFiscal:\t\t\t\t\t\t\t\t\t{}/{}/{}" .format(self._data.day, self._data.month, self._data.year))
        print("Cliente:", self._Id,  "\tNome:", self._cliente._nome)
        print("CPF/CNPJ:", self._cliente._cnpjcpf)
        print("-" *100, "\nItens")
        print("-" *100)
        print("Seq\t Descrição\t\t  QTD\t  Valor Unit\t       Preço") 
        print("-"*4,"\t","-"*15 ,"\t","-"*5,"\t","-"*12,"\t","-"*15 )
        
        
    
    