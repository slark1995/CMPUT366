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

endRightPosition = 1000
endLeftPosition = 0
startPosition = 500



def env_init():
    global current_state
    current_state = np.zeros(1)


def env_start():
    """ returns numpy array """
    global current_state
    current_state[0] = startPosition

    return current_state

def env_step(action):

    global current_state

    current_state[0] += action

    if current_state[0] <= endLeftPosition :
        is_terminal = True
        reward = -1

    elif current_state[0] >=endRightPosition:
        is_terminal = True
        reward = 1
    else:
        is_terminal = False
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
