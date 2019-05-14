class Pilha:
    def __init__(self):
        self.pilha = []

    def push(self, elem):
        self.pilha.append(elem)

    def pop(self):
        if len(self.pilha) > 0:
            return self.pilha.pop()
        raise PilhaVazia("A pilha está vazia")

    def top(self):
        if len(self.pilha) == 0:
            raise PilhaVazia("A pilha está vazia")
        return self.pilha[-1]
