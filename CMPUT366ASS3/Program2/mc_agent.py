

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

policy = None
Q = None
returnsReward = np.zeros((99,99))
returnsNum = np.zeros((99,99))
track = None
epsilon = 0.1 #you may need change it




def agent_init():
	global Q,returnsNum,returnsReward,epsilon,policy,track
	"""
	Hint: Initialize the variables that need to be reset before each run begins
	Returns: nothing
	"""
	#initialize the policy array in a smart way
	policy = np.zeros((99,99))
	Q = np.full((99,99),0.00000000001)
	returnsReward = np.zeros((99,99))
	returnsNum = np.full((99,99),1) 
	setPolicy()
	cleanTrack()

def agent_start(state):
	global Q,returnsNum,returnsReward,epsilon,policy
	"""
	Hint: Initialize the variavbles that you want to reset before starting a new episode
	Arguments: state: numpy array
	Returns: action: integer
	"""
	# pick the first action, don't forget about exploring starts

	#------choose action-------#	
	action = rand_in_range(min(state[0],100-state[0]))+1
	track[state[0]-1][action-1] += 1

	return action


def agent_step(reward, state): # returns NumPy array, reward: floating point, this_observation: NumPy array
	global Q,returnsNum,returnsReward,epsilon,policy
	"""
	Arguments: reward: floting point, state: integer
	Returns: action: floating point
	"""
	# select an action, based on Q

	action =  np.argmax(Q[state[0]-1]*policy[state[0]-1])+1
	track[state[0]-1][action-1] += 1



	return action

def agent_end(reward):
	global Q,returnsNum,returnsReward,epsilon,policy,track
	"""
	Arguments: reward: floating point
	Returns: Nothing
	"""
	# do learning and update pi

	np.seterr(divide='ignore',invalid='ignore')

	returnsReward += (track*reward)
	returnsNum += track
	cleanTrack()
	Q = returnsReward/returnsNum


	for s in range(1,100):
		best_a = np.argmax(Q[s-1])+1

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
		return pickle.dumps(np.max(Q, axis=1), protocol=0)
	else:
		return "I don't know what to return!!"



def cleanTrack():
	global track
	track = np.zeros((99,99))

def setPolicy():
	global policy
	policy = np.zeros((99,99))
	for s in range(1,100):
		a = min(s,100-s)
		policy[s-1][a-1] = 1.0 # under s choose a
	return





