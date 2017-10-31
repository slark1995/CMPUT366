#!/usr/bin/env python

"""
  Author: Adam White, Mohammad M. Ajallooeian, Sina Ghiassian
  Purpose: Code for the Gambler's problem environment from the Sutton and Barto
  Reinforcement Learning: An Introduction Chapter 4.
  For use in the Reinforcement Learning course, Fall 2017, University of Alberta 
"""

from utils import rand_norm, rand_in_range, rand_un
import numpy as np

current_state = None
end_position = [8,5]
start_position = [0,3]
top_boundary = 5
right_boundary = 8
bot_boundary = 0
left_boundary = 0

obstcles = [[2,2],[2,3],[2,4],[5,1],[7,3],[7,4],[7,5]]


def env_init():
    global current_state
    current_state = np.zeros(2)


def env_start():
    """ returns numpy array """
    global current_state
    current_state = start_position

    return current_state

def env_step(action):
    '''
    parameter: action [int,int]
    return: result ={"reward": int , "state": numpy array, "isTerminal": boolean}

    '''
    global current_state


    h_move = action[0]
    v_move = action[1]

    x = current_state[0]
    y = current_state[1]



    newx = x + h_move
    newy = y + v_move


    
    if newx>=left_boundary and newx<=right_boundary and newy>=bot_boundary and newy<=top_boundary :
        if [newx,newy] not in obstcles:
            current_state = [newx,newy]


         

    is_terminal = (current_state == end_position)
    if is_terminal:
        reward = 1
    else:
        reward = 0



    result = {"reward": reward, "state": current_state, "isTerminal": is_terminal}

    return result

def env_cleanup():
    #
    return

def env_message(in_message): # returns string, in_message: string
    """
    Arguments
    ---------
    inMessage : string
        the message being passed

    Returns
    -------
    string : the response to the message
    """
    return ""
