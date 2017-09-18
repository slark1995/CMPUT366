#!/usr/bin/env python

"""
  Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian
  Purpose: for use of Rienforcement learning course University of Alberta Fall 2017
 
  agent does *no* learning, selects actions randomly from the set of legal actions
 
"""

from utils import rand_in_range,rand_un
import numpy as np

last_action = None # last_action: NumPy array
Qtable = None
num_actions = 10

def agent_init():
    global last_action
    createTable()
    last_action = np.zeros(1) # generates a NumPy array with size 1 equal to zero

def agent_start(this_observation): # returns NumPy array, this_observation: NumPy array
    global last_action

    local_action = np.zeros(1)
    if rand_un() < 0.1: # you may change it to 0
        local_action[0] = rand_in_range(num_actions)
    else:
        local_action[0] = findGreedyAction()
    last_action = local_action



    return local_action[0]


def agent_step(reward, this_observation): # returns NumPy array, reward: floating point, this_observation: NumPy array
    global last_action
    saveQInTable(reward)

    return last_action

def agent_end(reward): # reward: floating point
    # final learning update at end of episode
    return

def agent_cleanup():
    # clean up
    return

def agent_message(inMessage): # returns string, inMessage: string
    # might be useful to get information from the agent

    if inMessage == "what is your name?":
        return "my name is skeleton_agent!"
  
    # else
    return "I don't know how to respond to your message"




def createTable(): #create a Q table track all Q(a)
    global Qtable
    Q_a = 0 # you may need change it to 5
    Qtable = []
    for i in range(num_actions):
        Qtable.append(Q_a)
    return


def findGreedyAction():#find the largest Q in Qtable
    max_Q = Qtable[0]
    ava_table = []
    n = 0
    for one_Q in Qtable:
        if max_Q < one_Q:
            max_Q = one_Q
            ava_table = [n]
        elif max_Q == one_Q:
            ava_table.append(n)
        n+=1
    index = rand_in_range(len(ava_table))
    return ava_table[index]

def saveQInTable(reward): #update Qtable getting new Q(a)
    global Qtable, last_action 
    last_Q = Qtable[int(last_action[0])]
    new_Q = last_Q+(0.1)*(reward-last_Q)  
    Qtable[int(last_action[0])] = new_Q
    return 









