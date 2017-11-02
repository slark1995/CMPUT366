#!/usr/bin/env python

"""
	Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Andrew
	Jacobsen, Victor Silva, Sina Ghiassian
	Purpose: Implementation of the interaction between the Gambler's problem environment
	and the Monte Carlon agent using RL_glue. 
	For use in the Reinforcement Learning course, Fall 2017, University of Alberta

"""
from utils import changeN
import numpy as np
import pickle
import sys
import time
from rl_glue import *  # Required for RL-Glue

RLGlue("environment", "agent")


def save_results(data, data_size, filename): # data: floating point, data_size: integer, filename: string
    with open(filename, "w") as data_file:
        for i in range(data_size):
            data_file.write("{0}\n".format(data[i]))


start_time = time.time()
if __name__ == "__main__":
	alist = [0,5,50]
	data = np.zeros((3,50))
	np.random.seed(100)
	for i in range(3):
		changeN(alist[i])
		print("... n: %d" %(alist[i]))

		for run in range(10):
			RL_init()
			print("\t... run num: %d" %(run))
			num_episodes = 0
			while num_episodes<50:
				RL_episode(2000)
				steps = RL_num_steps()
				data[i][num_episodes] += steps
				num_episodes +=1
			RL_cleanup()


	save_results(data[0]/10,50,"output1.txt")
	save_results(data[1]/10,50,"output2.txt")
	save_results(data[2]/10,50,"output3.txt")
	print ("=>finish! :D\n")
	print("=>total time: %f. " %round(time.time()-start_time,2))


