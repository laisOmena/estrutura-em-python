from collections import deque

d = deque()

d.extend('raiar')

def palin(d):
  if len(d) <= 1:
    return True
  else:
    if d.pop() == d.popleft():
      return palin(d)
  return False

print(palin(d))  