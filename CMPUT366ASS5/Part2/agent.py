

#!/usr/bin/env python

"""
  Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Sina Ghiassian
  Purpose: Skeleton code for Monte Carlo Exploring Starts Control Agent
		   for use on A3 of Reinforcement learning course University of Alberta Fall 2017
 
"""
"""
/*
 * Copyright (c) HAOTIAN ZHU ,COMPUT301,University Of Alberta All Rights Reserved.
 * You May Use, Distribute Or Modify This Code Under Term And 
 * Condition Of Code Of Students Behavior At University Of Alberta.
 *
 *
 * Author: Haotian Zhu
 * If You Have Any Question Please contact haotian1@ualberta.ca.
 * 
 */
"""
from utils import rand_in_range, rand_un
import numpy as np
import pickle




# policy[s][a]: numpy; has total 99*99 element to track and store all policy(a|s),some pi(a|s) are always 0
# Q[s][a]: numpy; has total 99*99 element to track and store all action-value under state s and action a
# returnsReward[s][a]: numpy; stores all history action-value reward-> " reward + discount*Q(a`,s`) " 
# returnsNum[s][a]: numpy: checks and stores the history total number of choosing a under s
# epsilon: float variable 
# track track times of the action under state has been chosen 
n = None
Q = None
model = None
num_action = 4 #you may need change it
epsilon = 0.1 #you may need change it
modelKey = None
actions = {0:[0,1],1:[1,0],2:[0,-1],3:[-1,0]}
last_action = None #tack last action
last_x = None #tack last state's x
last_y = None #tack last state's y
alpha_step = 0.1 #you may need change it
gamma = 0.95


def agent_init():
	global Q,last_action,last_y,last_x,model,n
	"""
	Hint: Initialize the variables that need to be reset before each run begins
	Returns: nothing
	"""
	#initialize the policy array in a smart way
	from utils import maxN
	n = maxN
	from utils import newalpha_step
	alpha_step = newalpha_step
	Q = np.zeros((9,6,num_action))

	model = np.full((9,6,num_action,3),-1.0)

	last_x = -1
	last_y = -1
	last_action = -1

	return

def agent_start(state):
	global Q,last_action,last_y,last_x,model
	"""
	Hint: Initialize the variavbles that you want to reset before starting a new episode
	Arguments: state: numpy array
	Returns: action: integer list
	"""
	# pick the first action, don't forget about exploring starts
	x = state[0]
	y = state[1]
	if rand_un() < epsilon:
		action_index = rand_in_range(num_action)
	else:
		action_index = np.argmax(Q[x][y]) #find best action
		if  Q[x][y][action_index] == 0:
			action_index = rand_in_range(4)



	last_action = action_index
	last_x = x
	last_y = y

	action = actions[action_index]
	return action


def agent_step(reward, state): # returns NumPy array, reward: floating point, this_observation: NumPy array
	global Q,last_action,last_y,last_x,model
	"""
	Arguments: reward: floting point, state: integer
	Returns: action: floating point
	"""
	# select an action, based on Q

	# s'x and y 
	x = state[0] 
	y = state[1]



	Q[last_x][last_y][last_action] += alpha_step * (reward+  gamma*np.max(Q[x][y]) - Q[last_x][last_y][last_action])


	modelKey = (last_x,last_y,last_action)
	model[modelKey] = [reward,x,y]

	i = 0
	while i < n:
		i += 1
		chosen = False
		while not chosen:
			modelX = rand_in_range(9)
			modelY = rand_in_range(6)
			modelA = rand_in_range(4)
			if model[(modelX,modelY,modelA)][0] != -1.0:
				chosen = True

		modelNextY = model[(modelX,modelY,modelA)][2]
		modelNextX = model[(modelX,modelY,modelA)][1]
		modelReward = model[(modelX,modelY,modelA)][0]

		Q[modelX][modelY][modelA] += alpha_step * (modelReward +gamma*np.max(Q[modelNextX][modelNextY]) - Q[modelX][modelY][modelA])


	if rand_un() < epsilon:
		action_index = rand_in_range(num_action)
	else:
		action_index = np.argmax(Q[x][y]) #find best action
		if  Q[x][y][action_index] == 0:
			action_index = rand_in_range(4)


	last_x = x
	last_y = y
	last_action = action_index
	action = actions[action_index]


	return action

def agent_end(reward):
	global  Q,actions,last_action,last_y,last_x,modelDict


	Q[last_x][last_y][last_action] += alpha_step * (reward + 0 - Q[last_x][last_y][last_action] )


	return

def agent_cleanup():
	"""
	This function is not used
	"""
	# clean up

	return

def agent_message(in_message): # returns string, in_message: string
   	global Q
	"""
	Arguments: in_message: string
	returns: The value function as a string.
	This function is complete. You do not need to add code here.
	"""
	# should not need to modify this function. Modify at your own risk
	if (in_message == 'ValueFunction'):
		return 
	else:
		return "I don't know what to return!!"




