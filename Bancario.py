from Banco import Banco
import time


class Bancario(Banco): # Agente
    
    def atender(self):
        meta = True # meta false quando atendimentos == 9

        while meta:
            #atendimentos = 0
            # Bancario.filaFormada
            if (len(fila)) != 0 :
                x = 0
                while x <= len(fila) and meta == True: # atende
                    #tamanho_lista = len(fila)
                    atendimento = fila[x]
                    print(f"Obrigado {atendimento} pela preferência")
                    fila.pop(0)
                    print("Fila Atual: \n",fila)
                    
                    time.sleep(1)
                    #atendimentos += 1
                    #print(atendimentos) 
                    if len(fila) == 0:
                        time.sleep(1)
                        y = 1
                        while (y<=10):
                            Bancario.formaFila(self) 
                            print("Cliente na Fila")
                        #print("valor X: ", y)
                            time.sleep(1)
                            y+=1
                            time.sleep(2)

                        
                        z=0
                        while(len(fila) != 0):
                            atendimento = fila[0]
                            print(f"Obrigado {atendimento} pela preferência")
                            print("Fila Atual:", fila)
                            time.sleep(1)
                            fila.pop(0) 
                            z+=1
                            
                            

                        meta = False
                        print("Fila Vazia: \n",fila)
                        print("Atendimento Finalizado!")
                           
                  


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
           

        
