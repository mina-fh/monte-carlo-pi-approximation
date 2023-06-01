import random

Nin = 0
Nout = 0

def inChk(x1, y1):
  if (x1 ** 2) + (y1 ** 2) <= (0.5 ** 2):
    return True
  else:
    return False

for i in range(1, 8):
  Nin = 0
  Nout = 0
  sample = 10 ** i
  j = 1
  while j < sample:
    x = random.random() - 0.5
    y = random.random() - 0.5
    if inChk(x, y):
       Nin += 1
    else:
       Nout += 1
    j += 1

  pi = (4 * Nin) / (Nin + Nout)

  print("Sample", sample, "Number of circles inside: ", Nin, "Approximate value of pi: ", pi)
