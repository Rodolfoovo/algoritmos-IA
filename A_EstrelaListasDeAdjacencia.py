class A_EstrelaListasDeAdjacencia:
    def __init__(self, estado, pai,custo) -> None:
        self.estado = estado
        self.pai = pai
        self.euristica = custo
grafo = {
    "A" : [("B",5),("H",10), ("D",10)],
    "B" : [("F",5)],
    "C" : [("D",5)],
    "D" : [("E",5), ("G",10)],
    "E" : [("A",5),("C", 5), ("K", 10)],
    "F" : [("G",15)],
    "G" : [("A",10), ("C", 5)],
    "H" : [("B",5), ("K",20)],
    "K" : [("K",10)]
}

def calculoEuristica(estado):
#     print(estado)
     if(estado == 'A' or estado == 'C' or estado == 'E'or estado == 'F'or estado == 'G'):
      return 10
     elif(estado == 'B'):
      return 20
     elif(estado == 'D'):
      return 5
     elif(estado == 'H' or estado == 'K'):
      return 0
     return 0
     
def melhorVertice(abertos):
  #Pega o primeiro vertice
  melhorVertice = abertos[0][0]
#  print(melhorVertice)
  for verticeConcorrente in abertos[0]:
    #Pega somente o custo do vertice
    m2 = melhorVertice[1]
    i2 = verticeConcorrente[1]
#    print(m2, "  ", i2)
    #Verifica se o custo atual é menor que o custo inicial
    if m2 > i2:
#      print("Antes: ",melhorVertice)
      melhorVertice = verticeConcorrente
#      print("Depois: ", melhorVertice)
    #retorna o melhor vertice encontrado
  return  melhorVertice

def aEstrela(grafo, meta):
   abertos = [grafo["G"]]
   pai = None
   fechados = []
   achou = False
   while abertos and not achou:
      verticeAtual = melhorVertice(abertos)
      print("Depois da busca \n")
      print(verticeAtual)
      if meta == verticeAtual:
        achou = True
      for vizinho in verticeAtual:
        if isinstance(vizinho,tuple):
          if isinstance(vizinho[0], str):
            novoF = calculoEuristica(vizinho)
          print(novoF)
#        novoF = calculoEuristica(melhorVertice) + calculoEuristica(verticeAtual)
#        print(melhorVertice, " ", verticeAtual)
        #Implementado somente para que o código possua um fim
        achou = True
def main():
   meta = grafo["K"]
   aEstrela(grafo, meta)

if __name__ == "__main__":
  main()