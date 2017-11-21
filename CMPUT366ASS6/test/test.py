
import numpy as np


from importlib import import_module




tile = import_module("tiles3")
iht = tile.IHT(1000)

a =np.zeros(4)
b =np.zeros(4)
a[1] = 1
b[1] = 1

print(a*b)