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
RLGlue("environment", "agent")




start_time = time.time()
if __name__ == "__main__":
	num_episodes = 0
	max_steps = 8000
	total_steps = 0
	data_file = open("output.txt", "w")
	RL_init()
	while total_steps<8000:
		RL_episode(10000)
		total_steps += RL_num_steps()
		num_episodes = RL_num_episodes()
		print(total_steps,num_episodes)
		data_file.write("%d,%d\n" %(total_steps,num_episodes))
	RL_cleanup()
	data_file.close()

	print ("=>finish! :D\n")
	print("=>total time: %f. " %round(time.time()-start_time,2))


