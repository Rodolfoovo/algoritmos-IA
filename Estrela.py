import networkx as nx
import heapq

# Novo grafo direcionado
Grafo = nx.DiGraph()

# Arestas com os custos
Grafo.add_edge('A', 'B', weight=5)
Grafo.add_edge('A', 'D', weight=10)
Grafo.add_edge('A', 'H', weight=10)
Grafo.add_edge('B', 'F', weight=5)
Grafo.add_edge('C', 'D', weight=5)
Grafo.add_edge('D', 'E', weight=5)
Grafo.add_edge('D', 'G', weight=10)
Grafo.add_edge('E', 'A', weight=5)
Grafo.add_edge('E', 'C', weight=10)
Grafo.add_edge('E', 'K', weight=10)
Grafo.add_edge('F', 'G', weight=15)
Grafo.add_edge('G', 'C', weight=5)
Grafo.add_edge('H', 'B', weight=5)
Grafo.add_edge('H', 'K', weight=20)
Grafo.add_edge('K', 'B', weight=10)

# Função heurística
def heuristica(estado):
    heuristics = {
        'A': 10, 'B': 20, 'C': 10, 'D': 20,
        'E': 10, 'F': 10, 'G': 10, 'H': 0, 'K': 0
    }
    return heuristics.get(estado, 0)

# Verifica se encontrou o nó
def eureka(noAtual, meta):
    return noAtual == meta

# Encontra o melhor vértice em 'abertos'
def melhorVertice(abertos, f_score):
    return min(abertos, key=lambda x: f_score[x])

# Algoritmo em si
def aEstrela(Grafo, noAtual, meta):
    abertos = []
    fechados = set()
    g_score = {noAtual: 0}
    f_score = {noAtual: heuristica(noAtual)}
    pai = {noAtual: None}

    heapq.heappush(abertos, (f_score[noAtual], noAtual))

    while abertos:
        _, noAtual = heapq.heappop(abertos)
        
        if eureka(noAtual, meta):
            caminho = []
            while noAtual:
                caminho.append(noAtual)
                noAtual = pai[noAtual]
            caminho.reverse()
            custo_total = g_score[caminho[-1]]
            print("Caminho escolhido:", caminho)
            print("Custo total do caminho:", custo_total)
            return caminho, custo_total

        fechados.add(noAtual)

        for vizinho in Grafo.neighbors(noAtual):
            if vizinho in fechados:
                continue

            tentativo_g_score = g_score[noAtual] + Grafo[noAtual][vizinho]['weight']
            
            if vizinho not in g_score or tentativo_g_score < g_score[vizinho]:
                pai[vizinho] = noAtual
                g_score[vizinho] = tentativo_g_score
                f_score[vizinho] = tentativo_g_score + heuristica(vizinho)
                
                if vizinho not in [i[1] for i in abertos]:
                    heapq.heappush(abertos, (f_score[vizinho], vizinho))

    print("Não foi possível encontrar um caminho.")
    return None, float('inf')

def main():
    noInicial = 'G'
    noFinal = 'K'
    aEstrela(Grafo, noInicial, noFinal)

if __name__ == "__main__":
    main()
