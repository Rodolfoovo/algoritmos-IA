class buscaMelhorEscolha:
    def __init__(self, estado, pai=None):
        self.estado = estado
        self.euristica = self.euristica(estado)
        self.pai = pai

    def euristica(self, estado):
        return 0    

    @staticmethod
    def buscaMelhorEscolha(estadoInicial):
        visitado = set()
        pilhaDeRestantes = [buscaMelhorEscolha(estadoInicial)]
        while pilhaDeRestantes:
            estado = pilhaDeRestantes.pop()
            if str(estado.estado) in visitado:
                continue
            if estado.validacao():
                return estado
            visitado.add(str(estado.estado))
            for vizinho in estado.movimentoPossiveis():
                if str(vizinho.estado) not in visitado:
                    pilhaDeRestantes.append(vizinho)

    def validacao(self):
        estadoFinal = ["E","E","","D","D"]
        return self.estado == estadoFinal

    def movimentoPossiveis(self):
        vizinhos = []
        for pos, conteudo in enumerate(self.estado):
            novo_estado = self.estado.copy()
            if conteudo == "E":
                if pos > 0 and novo_estado[pos - 1] == "":
                    novo_estado[pos], novo_estado[pos - 1] = novo_estado[pos - 1], novo_estado[pos]
                    vizinhos.append(buscaMelhorEscolha(novo_estado, self))
                if pos > 1 and novo_estado[pos - 2] == "":
                    novo_estado[pos], novo_estado[pos - 2] = novo_estado[pos - 2], novo_estado[pos]
                    vizinhos.append(buscaMelhorEscolha(novo_estado, self))
            if conteudo == "D":
                if pos < 3 and novo_estado[pos + 1] == "":
                    novo_estado[pos], novo_estado[pos + 1] = novo_estado[pos + 1], novo_estado[pos]
                    vizinhos.append(buscaMelhorEscolha(novo_estado, self))
                if pos < 2 and novo_estado[pos + 2] == "":
                    novo_estado[pos], novo_estado[pos + 2] = novo_estado[pos + 2], novo_estado[pos]
                    vizinhos.append(buscaMelhorEscolha(novo_estado, self))
        return vizinhos

estadoInicial = ["D","D","","E","E"]
estadoFinal = buscaMelhorEscolha.buscaMelhorEscolha(estadoInicial)
print(estadoFinal.estado)

