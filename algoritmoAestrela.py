import networkx as nx

class algoritmoAestrela:
    def __init__(self, vertice,euristica,g,h, pai):
        self.vertice = vertice
        self.euristica = euristica(g,h)
        self.pai = pai
    
    def euristica():
        return 0
    def algoritmoAestrela(grafo):
        abertos = []
        solucao = False
        while len(abertos) > 0 and solucao == False:
            v = melhorVertice(abertos)
            if v == t:
                solucao = True


def main():
    grafo = nx.Graph()
    algoritmoAestrela(grafo)

if __name__ == "__name__":
    main()