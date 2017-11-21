



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


import numpy as np
import pickle




w = None
currentState = None
lastState = None
alpha = 0.1
gamma = 0.9
x = None


def agent_init():
	global w,currentState,lastState,x

	x = np.identity(10)

	w = np.zeros(10)
	currentState = np.zeros(1)
	lastState = np.zeros(1)


	return

def agent_start(state):
	global w,currentState,lastState,x


	currentState[0] = state[0]/100
	lastState[0] = currentState[0]
	action = chooseAction(state[0])




	return action


def agent_step(reward, state): 
	global w,currentState,lastState,x

	currentState[0] = state[0]/100
	w = w + alpha*(reward+gamma*w[currentState[0]]- w[lastState[0]])*x[lastState[0]]
	action = chooseAction(state[0])
	lastState[0] = currentState[0]

	return action

def agent_end(reward):
	global w,currentState,lastState,x
	w = w + alpha*(reward-w[lastState[0]])*x[lastState[0]]



	return

def agent_cleanup():
	"""
	This function is not used
	"""
	# clean up

	return

def agent_message(in_message): # returns string, in_message: string
   	global w
	"""
	Arguments: in_message: string
	returns: The value function as a string.
	This function is complete. You do not need to add code here.
	"""
	# should not need to modify this function. Modify at your own risk
	if (in_message == 'ValueFunction'):
		return w
	else:
		return "I don't know what to return!!"




def chooseAction(state):
	if np.random.randint(2) : #1
		result = np.random.randint(100)+1
		if result+state>=1000:
			return 1000-state
		else:
			return result

	else:
		result = (np.random.randint(100)+1)*(-1)
		if result+state<=0:
			return state*(-1)
		else:
			return result 










