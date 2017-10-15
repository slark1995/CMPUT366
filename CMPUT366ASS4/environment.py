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
wind_list = [0,0,0,1,1,1,2,2,1,0]
end_position = [7,3]
start_position = [0,3]
top_boundary = 6
right_boundary = 9
bot_boundary = 0
left_boundary = 0


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
        current_state = [newx,newy]


    current_state[1]+=wind_list[x]
    if current_state[1]>top_boundary:
        current_state[1] = top_boundary

         

    is_terminal = (current_state == end_position)
    if is_terminal:
        reward = 1
    else:
        reward = -1



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
