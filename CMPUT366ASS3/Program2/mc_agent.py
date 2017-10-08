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



# last_state : a variable to track last state given by enviroment
# last_action: a variable to track last action shosen by program under last state
# policy[s][a]: numpy; has total 99*99 element to track and store all policy(a|s),some pi(a|s) are always 0
# Q[s][a]: numpy; has total 99*99 element to track and store all action-value under state s and action a
# returnsReward[s][a]: numpy; stores all history action-value reward-> " reward + discount*Q(a`,s`) " 
# returnsNum[s][a]: numpy: checks and stores the history total number of choosing a under s
# epsilon: float variable 
# discount : flaot varibale <=> gamma
last_state = None
last_action = None
policy = None
Q = None
returnsReward = np.zeros((99,99))
returnsNum = np.zeros((99,99))

epsilon = 0.1 #you may need change it
discount = 1 # you may need change it



def agent_init():
	global Q,returnsNum,returnsReward,epsilon,last_action,last_state,policy
	"""
	Hint: Initialize the variables that need to be reset before each run begins
	Returns: nothing
	"""
	#initialize the policy array in a smart way
	setPolicy()
	Q = np.zeros((99,99))
	last_state = 0
	last_action = 0
	returnsReward = np.zeros((99,99))
	returnsNum = np.zeros((99,99))


def agent_start(state):
	global Q,returnsNum,returnsReward,epsilon,last_action,last_state,policy
	"""
	Hint: Initialize the variavbles that you want to reset before starting a new episode
	Arguments: state: numpy array
	Returns: action: integer
	"""
	# pick the first action, don't forget about exploring starts

	#------choose action-------#	
	action =  np.nanargmax(policy[state[0]-1])+1
	last_action = action #set last action
	last_state = state[0] #set last state
	returnsNum[state[0]-1][action-1]+=1
	return action


def agent_step(reward, state): # returns NumPy array, reward: floating point, this_observation: NumPy array
	global Q,returnsNum,returnsReward,epsilon,last_action,last_state,policy
	"""
	Arguments: reward: floting point, state: integer
	Returns: action: floating point
	"""
	# select an action, based on Q

	#------choose action-------#


	action =  np.nanargmax(policy[state[0]-1]*Q[state[0]-1])+1

	# when program chooses action = 1 first action, and action-value is 0 
	# it is means that all action-value under state is 0
	# we choose action randomly then. 
	if action == 1 and Q[state[0]-1][action-1] == 0:
		#action = np.nanargmax(policy[state[0]-1])+1
		action = rand_in_range(min(state[0],100-state[0]))+1


	returnsReward[last_state-1][last_action-1] += reward+discount*(Q[state[0]-1][action-1])
	last_action = action #set last action
	last_state = state[0] #set last state
	returnsNum[state[0]-1][action-1]+=1 #times + 1
	return action

def agent_end(reward):
	global Q,returnsNum,returnsReward,epsilon,last_action,last_state,policy
	"""
	Arguments: reward: floating point
	Returns: Nothing
	"""
	# do learning and update pi
	np.seterr(divide='ignore',invalid='ignore')
	returnsReward[last_state-1][last_action-1] += (reward+discount*0)
	#------update Q-------#
	Q = np.nan_to_num(returnsReward/returnsNum)  
	#------update Pi-------#
	for s in range(1,100):
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
		return pickle.dumps(np.nanmax(Q, axis=1), protocol=0)
	else:
		return "I don't know what to return!!"

def setPolicy():
	global policy
	policy = np.zeros((99,99))
	for s in range(1,100):
		a = min(s,100-s)
		policy[s-1][a-1] = 1.0 # under s choose a
	return






