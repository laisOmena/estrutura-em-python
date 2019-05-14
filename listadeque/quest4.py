from collections import deque

d = deque()

word = 'raiar'

def palin():
  if word[0] == word[-1]:
    return True
  
  