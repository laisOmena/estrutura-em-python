from collections import deque
from fila import *


d = deque()
'''1-

d.appendleft(4)
d.append(8)
d.append(9)
d.appendleft(5)
print(d[-1])
d.popleft()
d.pop()
d.append(7)
print(d[0])
print(d[-1])
d.append(6)
d.popleft()
d.popleft()
print(d)'''


'''2-
fila = FilaArray()

d.append(1)
d.append(2)
d.append(3)
d.append(4)
d.append(5)
d.append(6)
d.append(7)
d.append(8)

while len(d) != 0:
  fila.enqueue(d.popleft())

print(fila.getPilha())'''


