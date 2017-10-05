
from utils import rand_in_range, rand_un
import numpy as np
a = np.array([[1,2,3],[3,2,1],[0,78,0]])

c  = np.nanargmax(a,axis= 0)
print(a,c)
