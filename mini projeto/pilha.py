class PilhaArray:
  def __init__(self):
    self._pilha = []
  
  def __len__(self):
    return len(self._pilha)
  
  def size(self):
    return self.__len__()

  def is_empty(self):
    return len(self._pilha) == 0
  
  def push(self, e):
    self._pilha.append(e)

  def top(self):
    if self.is_empty():
      raise PilhaVazia("A pilha está vazia")
    return self._pilha[-1]

  def pop(self):
    if self.is_empty():
      raise PilhaVazia("A pilha está vazia")
    return self._pilha.pop()

  def getPilha(self):
    return self._pilha