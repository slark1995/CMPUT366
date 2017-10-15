import numpy as np
current_state = np.zeros((2,2,2))
current_state[1][1][1] = 8
x = current_state[1][1][1]
current_state[1][1][1] += 1
print(x)