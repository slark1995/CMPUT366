#!/usr/bin/env python

"""
  Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Sina Ghiassian
  Purpose: Skeleton code for Monte Carlo Exploring Starts Control Agent
		   for use on A3 of Reinforcement learning course University of Alberta Fall 2017
 
"""

from utils import rand_in_range, rand_un
import numpy as np
import pickle



last_state = None
last_action = None
policy = None
Q = None
returnsReward = np.zeros((99,99))
returnsNum = np.zeros((99,99))
actions = []
num_total_states = 99
epsilon = 0.1
discount = 0.9

def setActions():
	global actions
	actions = []
	for i in range(1,100):
		actions.append(i)
	return

def agent_init():
	global actions,Q,returnsNum,returnsReward,epsilon,track
	"""
	Hint: Initialize the variables that need to be reset before each run begins
	Returns: nothing
	"""
	#initialize the policy array in a smart way
	setActions()
	setPolicy()
	Q = np.zeros((99,99))
	last_state = np.zeros(1)
	last_action = np.zeros(1)
	returnsReward = np.zeros((99,99))
	returnsNum = np.zeros((99,99))


def agent_start(state):
	global actions,Q,returnsNum,returnsReward,epsilon,track
	"""
	Hint: Initialize the variavbles that you want to reset before starting a new episode
	Arguments: state: numpy array
	Returns: action: integer
	"""
	# pick the first action, don't forget about exploring starts	
	action =  nanargmax(policy*Q)+1

	returnsReward[last_state[0]-1][last_action[0]-1] += (reward+discount*(Q[state[0]-1][action-1]))
	last_action[0] = action
	last_state[0] = state
	returnsNum[state[0]-1][action-1]+=1
	return action


def agent_step(reward, state): # returns NumPy array, reward: floating point, this_observation: NumPy array
	global actions,Q,returnsNum,returnsReward,epsilon,track
	"""
	Arguments: reward: floting point, state: integer
	Returns: action: floating point
	"""
	# select an action, based on Q
	action =  nanargmax(policy*Q)+1
	returnsReward[last_state[0]-1][last_action[0]-1] += (reward+discount*(Q[state[0]-1][action-1]))
	last_action[0] = action
	last_state[0] = state
	returnsNum[state[0]-1][action-1]+=1
	return action

def agent_end(reward):
	global actions,Q,returnsNum,returnsReward,epsilon,track
	"""
	Arguments: reward: floating point
	Returns: Nothing
	"""
	# do learning and update pi

	returnsReward[last_state[0]-1][last_action[0]-1] += (reward+0)

	print(returnsReward[49],returnsNum[49])
	Q = np.nan_to_num(returnsReward/returnsNum)
	for s in range(1,100): #update Pi
		best_a = np.nanargmax(Q[s-1])+1
		if best_a == 1 and Q[s-1][best_a-1] == 0 :
			best_a = min(s,100-s)
		c = epsilon/(min(s,100-s))
		for j in range(min(s,100-s)):
			policy[s-1][j] = c
		policy[s-1][best_a-1] = 1 - epsilon+c
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
		return pickle.dumps(np.max(Q, axis=0), protocol=0)
	else:
		return "I don't know what to return!!"

def setPolicy():
	global policy
	policy = np.zeros((99,99))
	for s in range(1,100):
		a = min(s,100-s)
		policy[s-1][a-1] = 1.0 # under s choose a
	return






