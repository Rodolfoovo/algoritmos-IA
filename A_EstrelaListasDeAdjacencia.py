class A_EstrelaListasDeAdjacencia:
    def __init__(self, estado, pai, euristica) -> None:
        self.estado = estado
        self.pai = pai
        self.euristica = euristica
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