#!/usr/bin/env python

"""
	Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Andrew
	Jacobsen, Victor Silva, Sina Ghiassian
	Purpose: Implementation of the interaction between the Gambler's problem environment
	and the Monte Carlon agent using RL_glue. 
	For use in the Reinforcement Learning course, Fall 2017, University of Alberta

"""
import numpy as np
import pickle
import sys
import time
from rl_glue import *  # Required for RL-Glue



RLGlue("environment", "agent2")


def save_results(data, data_size, filename): # data: floating point, data_size: integer, filename: string
    with open(filename, "w") as data_file:
        for i in range(data_size):
            data_file.write("{0}\n".format(data[i]))


valueFunction = np.zeros(1000)
#valueFunction = np.zeros(10)
start_time = time.time()
if __name__ == "__main__":
	max_steps = 8000

	for i in range(1):
		print("=>here  ",i)
		RL_init()
		for m in range(8000):
			RL_episode(10000)


		valueFunction += RL_agent_message("ValueFunction")
		RL_cleanup()



	save_results(valueFunction,1000,"output.txt")
	#save_results(valueFunction/10,10,"output.txt")


	print ("=>finish! :D\n")
	print("=>total time: %f. " %round(time.time()-start_time,2))


