

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


Q = None
num_action = 8 #you may need change it
epsilon = 0.1 #you may need change it
actions = {0:[0,1],1:[1,1],2:[1,0],3:[1,-1],4:[0,-1],5:[-1,-1],6:[-1,0],7:[-1,1]}
#actions = {0:[0,1],1:[1,0],2:[0,-1],3:[-1,0]}
last_action = None
last_x = None
last_y = None
alpha_step = 0.5


def agent_init():
	global Q,actions,last_action
	"""
	Hint: Initialize the variables that need to be reset before each run begins
	Returns: nothing
	"""
	#initialize the policy array in a smart way
	Q = np.zeros((10,7,num_action))
	last_x = 0
	last_y = 0
	last_action = 0

	if num_action == 9:
		actions[8] = [0,0]


	return

def agent_start(state):
	global Q,actions,last_action,last_y,last_x
	"""
	Hint: Initialize the variavbles that you want to reset before starting a new episode
	Arguments: state: numpy array
	Returns: action: integer
	"""
	# pick the first action, don't forget about exploring starts
	x = state[0]
	y = state[1]
	if rand_un() < epsilon:
		action_index = rand_in_range(num_action)
	else:
		action_index = np.argmax(Q[x][y]) #find best action

	last_action = action_index
	last_x = x
	last_y = y
	action = actions[action_index]
	return action


def agent_step(reward, state): # returns NumPy array, reward: floating point, this_observation: NumPy array
	global Q,actions,last_action,last_y,last_x
	"""
	Arguments: reward: floting point, state: integer
	Returns: action: floating point
	"""
	# select an action, based on Q

	# s' 
	x = state[0] 
	y = state[1]


	if rand_un() < epsilon:
		action_index = rand_in_range(num_action)
	else:
		action_index = np.argmax(Q[x][y]) #find best action



	Q[last_x][last_y][last_action] += alpha_step * (reward+Q[x][y][action_index]-Q[last_x][last_y][last_action])


	last_x = x
	last_y = y
	last_action = action_index
	action = actions[action_index]


	return action

def agent_end(reward):
	global  Q,actions,last_action,last_y,last_x

	Q[last_x][last_y][last_action] += alpha_step * (reward - Q[last_x][last_y][last_action])

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




