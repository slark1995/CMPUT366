
from utils import rand_in_range, rand_un
import numpy as np
a = np.full(10,5)
b = np.full(10,10)
b[0] +=1
b[1] +=100
c = np.argmax(b)+1
print(b,c)
