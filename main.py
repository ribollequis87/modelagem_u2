from aigyminsper.search.SearchAlgorithms import BuscaCustoUniforme
from aigyminsper.search.Graph import State
from collections import deque


class U2(State):
    def __init__(self, op, bono, edge, adam, larry, lanterna, _cost):
        self.operator = op
        self.bono = bono
        self.edge = edge
        self.adam = adam
        self.larry = larry
        self.lanterna = lanterna
        self._cost = _cost

    def cost(self):
        return self._cost
    
    def is_goal(self):
        return not self.bono and not self.edge and not self.adam and not self.larry and not self.lanterna
    
    def description(self):
        return "Travessia da banda U2 pela ponte"

    def successors(self):
        sucessors = []
        # bono pra direita
        if self.bono == False and self.lanterna == False:
            sucessors.append(U2("bono_dir", True, self.edge, self.adam, self.larry, True,1))
        # edge pra direita
        if self.edge == False and self.lanterna == False:
            sucessors.append(U2("edge_dir", self.bono, True, self.adam, self.larry, True,2))
        # adam pra direita
        if self.adam == False and self.lanterna == False:
            sucessors.append(U2("adam_dir", self.bono, self.edge, True, self.larry, True,5))
        # larry pra direita
        if self.larry == False and self.lanterna == False:
            sucessors.append(U2("larry_dir", self.bono, self.edge, self.adam, True, True, 10))

        # bono pra esquerda
        if self.bono == True and self.lanterna == True:
            sucessors.append(U2("bono_esq", False, self.edge, self.adam, self.larry, False,1))
        # edge pra esquerda
        if self.edge == True and self.lanterna == True:
            sucessors.append(U2("edge_esq", self.bono, False, self.adam, self.larry, False, 2))
        # adam pra esquerda
        if self.adam == True and self.lanterna == True:
            sucessors.append(U2("adam_esq", self.bono, self.edge, False, self.larry, False,5))
        # larry pra esquerda
        if self.larry == True and self.lanterna == True:
            sucessors.append(U2("larry_esq", self.bono, self.edge, self.adam, False, False,10))

        # bono e edge pra direita
        if self.bono == False and self.edge == False and self.lanterna == False:
            sucessors.append(U2("bono_edge_dir", True, True, self.adam, self.larry, True,2))
        # bono e adam pra direita
        if self.bono == False and self.adam == False and self.lanterna == False:
            sucessors.append(U2("bono_adam_dir", True, self.edge, True, self.larry, True,5))
        # bono e larry pra direita
        if self.bono == False and self.larry == False and self.lanterna == False:
            sucessors.append(U2("bono_larry_dir", True, self.edge, self.adam, True, True,10))
        # edge e adam pra direita
        if self.edge == False and self.adam == False and self.lanterna == False:
            sucessors.append(U2("edge_adam_dir", self.bono, True, True, self.larry, True,5))
        # edge e larry pra direita
        if self.edge == False and self.larry == False and self.lanterna == False:
            sucessors.append(U2("edge_larry_dir", self.bono, True, self.adam, True, True,10))
        # adam e larry pra direita
        if self.adam == False and self.larry == False and self.lanterna == False:
            sucessors.append(U2("adam_larry_dir", self.bono, self.edge, True, True, True,10))
        
        # bono e edge pra esquerda
        if self.bono == True and self.edge == True and self.lanterna == True:
            sucessors.append(U2("bono_edge_esq", False, False, self.adam, self.larry, False,2))
        # bono e adam pra esquerda
        if self.bono == True and self.adam == True and self.lanterna == True:
            sucessors.append(U2("bono_adam_esq", False, self.edge, False, self.larry, False,5))
        # bono e larry pra esquerda
        if self.bono == True and self.larry == True and self.lanterna == True:
            sucessors.append(U2("bono_larry_esq", False, self.edge, self.adam, False, False,10))
        # edge e adam pra esquerda
        if self.edge == True and self.adam == True and self.lanterna == True:
            sucessors.append(U2("edge_adam_esq", self.bono, False, False, self.larry, False,5))
        # edge e larry pra esquerda
        if self.edge == True and self.larry == True and self.lanterna == True:
            sucessors.append(U2("edge_larry_esq", self.bono, False, self.adam, False, False,10))
        # adam e larry pra esquerda
        if self.adam == True and self.larry == True and self.lanterna == True:
            sucessors.append(U2("adam_larry_esq", self.bono, self.edge, False, False, False,10))
        
        return sucessors
    
    def env(self):
        return (self.bono, self.edge, self.adam, self.larry, self.lanterna)
    

    
def main():
    print('Busca em custo uniforme')
    estado_inicial = U2('', True, True, True, True, True, 0)
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(estado_inicial, trace=True)
    if result != None:
        print('Achou!')
        print(result.show_path())
        print(result.g)
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()