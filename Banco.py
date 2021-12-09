import random

class Banco(): # ambiente
        

    def __init__(self):
        self.clientes = [] # lista de clientes
        # self.fila = []

    def gerarClientes(self): # setor de Marketing/Vendas
        self.clientes = list(range(0, 10))
        return self.clientes

    
        
    
    
