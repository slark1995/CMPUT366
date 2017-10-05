
from utils import rand_in_range, rand_un
import numpy as np
a = np.zeros((10,10))
b = np.zeros((10,10))


i = 0
while i < 100 :
	s = rand_in_range(10)
	i+=1
	action = min(s,9-s)
	if s == 5:
		print(s,action)
		if rand_un()<0.9:
			b[s+action][action]=rand_un()
			a[s][action] += b[s+action][action]


		else:
			a[s][action] += b[s-action][action]+rand_un()

		print(a[5][4])
