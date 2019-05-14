from tentativa import Pilha

'''1. Qual os valores retornados durante a a seguinte série de operações em uma pilha,
quando executadas em um pilha "p" inicialmente vazia? p.push(5), p.push(3), p.pop(),
p.push(2), p.push(8), p.pop(), p.pop(), p.push(9), p.push(1), p.pop(),p.push(7), p.push(6),
p.pop(), p.pop(), p.push(4), p.pop(), p.pop().'''

p = Pilha()
p.push(5)
print(p.pilha)
p.push(3)
print(p.pilha)
p.pop()
print(p.pilha)
p.push(2)
print(p.pilha)
p.push(8)
print(p.pilha)
p.pop()
print(p.pilha)
p.pop()
print(p.pilha)
p.push(9)
print(p.pilha)
p.push(1)
print(p.pilha)
p.pop()
print(p.pilha)
p.push(7)
print(p.pilha)
p.push(6)
print(p.pilha)
p.pop()
print(p.pilha)
p.pop()
print(p.pilha)
p.push(4)
print(p.pilha)
p.pop()
print(p.pilha)
p.pop()
print(p.pilha)

'''2. Considere que em uma pilha "p" inicialmente vazia foi executado um total de 25 operações push, 12 operações top e 10
operações pop, 3 das quais lançaram exceção "Pilha Vazia". Qual o tamanho atual da pilha?'''

'''25 push(adicionam 25)
12 top(mostram o topo 12 vezes)
10 pop(removem 10)

25 - 10 = 15'''

'''3. Desenvolva um método/função recursiva para remover todos os elementos de uma pilha.'''


def pop(self):
    if len(self.pilha) > 0:
        return self.pilha.pop()
    return pop(self)












