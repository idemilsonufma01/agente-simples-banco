from Banco import Banco
import time


class Bancario(Banco): # Agente
    
    def atender(self):
        meta = True # meta false quando atendimentos == 10

        while meta:
            atendimentos = 0
            
            # Bancario.filaFormada
            if len(fila) != 0 :
                for atendimento in fila: # atende
                    tamanho_lista = len(fila)
                    
                    print(f"Obrigado {atendimento} pela preferência")
                    fila.pop(0)
                
                    time.sleep(0.1)
                    atendimentos += 1
                    print(atendimentos)
            
            # else:
            #     if atendimentos == 9:
            #         meta = False
            #     Bancario.formaFila(self)                    
            #     print("Sejam bem vindos!")


    def filaFormada(self):
        if len(fila) == 0:
            return False
        else:
            return True

    def formaFila(self):
        global fila

        fila = []
        
        lista_clientes = Banco.gerarClientes(self)
        
        for cliente in lista_clientes:
            fila.append(cliente)


        return fila

    # def listaFila(self):
    #     for cliente in lista_clientes:
    #         print(cliente)
           

        

