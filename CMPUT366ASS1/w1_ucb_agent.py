#!/usr/bin/env python

"""
  Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian
  Purpose: for use of Rienforcement learning course University of Alberta Fall 2017
 
  agent does *no* learning, selects actions randomly from the set of legal actions
 
"""

from utils import rand_in_range,rand_un
import numpy as np
import math
last_action = None # last_action: NumPy array
Qtable = None
num_actions = 10
total_t = 1

def agent_init():
    global last_action
    createTable(0) #you may change it
    last_action = np.zeros(1) # generates a NumPy array with size 1 equal to zero

def agent_start(this_observation): # returns NumPy array, this_observation: NumPy array
    global last_action,total_t

    local_action = np.zeros(1)
    if epsilon_case(0.1): # you may change it 
        local_action[0] = rand_in_range(num_actions)
    else:
        local_action[0] = findGreedyAction(2) # c = 2, you may change it 
    last_action = local_action
    total_t+=1


    return local_action[0]


def agent_step(reward, this_observation): # returns NumPy array, reward: floating point, this_observation: NumPy array
    global last_action
    saveQInTable(reward,0.1) #you may need change it

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




def createTable(Q_a): #create a Q table tracks all Q(a) Q_a = Q_estimate
    global Qtable
    Qtable = []
    for i in range(num_actions):
        Qtable.append([Q_a,1])
    return


def findGreedyAction(c):#find the largest value ,c is a constant
    m = -999999
    n = 0
    a = [n]
    for Q in Qtable:
        v =  Q[0]+c*(math.sqrt(math.log(total_t)/float(Q[1])))
        if m < v :
            m = v
            a = [n]
        elif m == v:
            a.append(n)

        n+=1
    index = rand_in_range(len(a))
    return a[index]

def saveQInTable(reward,alpha): #update Qtable getting new Q(a)
    global Qtable, last_action,total_t
    last_Q = Qtable[int(last_action[0])][0]
    t = Qtable[int(last_action[0])][1]
    t += 1
    Qtable[int(last_action[0])][1] = t #update t
    new_Q = last_Q+(alpha)*(reward-last_Q)  
    Qtable[int(last_action[0])][0] = new_Q
    return 


def epsilon_case(epsilon):
    return rand_un() < epsilon






