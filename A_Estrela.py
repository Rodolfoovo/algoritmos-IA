import networkx as nx
class A_estrela:
  def __init__(self, estado, heuristica, pai) -> None:
    self.estado = estado
    self.heuristica = heuristica(estado)
    self.pai = pai
# Cria um grafo direcionado
Grafo = nx.DiGraph()

# Adiciona arestas com custos
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
  if(estado == 'A' or estado == 'C' or estado == 'E'or estado == 'F'or estado == 'G'):
    return 10
  elif(estado == 'B'):
    return 20
  elif(estado == 'D'):
    return 20
  elif(estado == 'H' or estado == 'K'):
    return 0
  
# Verifica se encontrou o nó
def eureka(noAtual, meta):

  if(noAtual == meta):
    return True
  else:
    return False
  
def melhorVertice(abertos):

  
# Algoritmo A*
def aEstrela(Grafo, noAtual, meta):

  abertos = [noAtual]
  fechados = []
  
  while abertos and not eureka(noAtual, meta):

    abertos.append(noAtual)
    vizinhos =  melhorVertice(abertos)
    
    for vizinhoAtual in vizinhos:
      if vizinhoAtual in fechados:
        continue

      if eureka(noAtual, meta):




    

def main():
  noInicial =  A_estrela('G', heuristica, False)
  aEstrela(Grafo, noInicial, 'K')

if __name__ == "__main__":
  main()