class FilaArray:

  CAPACIDADE_PADRAO = 8

  def __init__(self):
    self._dados = [None] * FilaArray.CAPACIDADE_PADRAO
    self._tamanho = 0
    self._inicio = 0

  def __len__(self):
    return self._tamanho
  
  def is_empty(self):
    return self._tamanho == 0

  def first(self):
    if self.is_empty():
      raise FilaVazia('A Fila está vazia')
    return self._dados[self._inicio]

  def dequeue(self):
    if self.is_empty():
      raise FilaVazia('A Fila está vazia')
    result = self._dados[self._inicio]
    self._dados[self._inicio] = None
    self._inicio = (self._inicio + 1) % len(self._dados)
    self._tamanho -= 1
    return result
  
  def enqueue(self, e): # - - x x x -
    if self._tamanho == len(self._dados):
      self._aumenta_tamanho(2 * len(self._dados))
    disponivel = (self._inicio + self._tamanho) % len(self._dados)
    self._dados[disponivel] = e
    self._tamanho += 1

  def _aumenta_tamanho(self, novo_tamanho): # novo_tamanho precisar ser >= len(self)
    dados_antigos = self._dados
    self._dados = [None] * novo_tamanho
    posicao = self._inicio
    for k in range(self._tamanho):
      self._dados[k] = dados_antigos[posicao] # intentionally shift indices
      posicao = (1 + posicao) % len(dados_antigos) # use dados_antigos size as modulus
    self._inicio = 0

  def getPilha(self):
    return self._dados