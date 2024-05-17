class A_EstrelaListasDeAdjacencia:
  def __init__(self,custo,pai) -> None:
    self.custo = custo
    self.pai = pai

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
     if(estado[0] == 'A' or estado[0] == 'C' or estado[0] == 'E'or estado[0] == 'F'or estado[0] == 'G'):
      return  10 + estado[1]
     elif(estado[0] == 'B'):
      return 20 + estado[1]
     elif(estado[0] == 'D'):
      return 5 + estado[1]
     elif(estado[0] == 'H' or estado[0] == 'K'):
      return 0 + estado[1]
     
     
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

def aEstrela(grafo, abertos,meta):
#   print(abertos)
   fechados = []
   gFuncao = []
   fFuncao = []
   achou = False
   while abertos and not achou:
      verticeAtual = melhorVertice(abertos)
#      print(verticeAtual)
#      print("Depois da busca \n")
#      print(verticeAtual)
      if meta == verticeAtual:
        achou = True
      
      vizinho = verticeAtual
      novoF = calculoEuristica(vizinho)+calculoEuristica(verticeAtual)+ verticeAtual[1]
      print(novoF)
#      print(novoF)
      #Verifica se a euristica calculada é maior que a anterior.
      if (vizinho in fechados or vizinho in abertos) and novoF > calculoEuristica(vizinho):
        continue
      else:
        achou = True
            



#        novoF = calculoEuristica(melhorVertice) + calculoEuristica(verticeAtual)
#        print(melhorVertice, " ", verticeAtual)
        #Implementado somente para que o código possua um fim
      achou = True
def main():
   meta = grafo["K"]
   abertos = [grafo["G"]]
   aEstrela(grafo,abertos, meta)

if __name__ == "__main__":
  main()