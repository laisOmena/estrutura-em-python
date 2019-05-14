from fila import FilaArray
from pilha import PilhaArray

qtdMov = 0
pilha = PilhaArray()
fila = FilaArray()

for i in range(fila.CAPACIDADE_PADRAO):
  carta = int(input('Digite o valor da carta: '))
  fila.enqueue(carta)
  qtdMov += 1

while len(fila) > 0:
  while len(fila) > fila.first():
    num = fila.dequeue()
    qtdMov += 1
    fila.enqueue(num)
    qtdMov += 1

  if fila.first() == len(fila):
    num = fila.dequeue()
    qtdMov += 1
    pilha.push(num)
    qtdMov += 1

while len(pilha) > 0:
  num = pilha.pop()
  qtdMov += 1
  fila.enqueue(num)
  qtdMov += 1

while len(fila) > 0:
  num = fila.dequeue()
  qtdMov += 1
  pilha.push(num)
  qtdMov += 1

print('Aqui é minha pilha', pilha.getPilha())
print("Quantidade de movimentos", qtdMov)