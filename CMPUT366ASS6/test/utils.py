#!/usr/bin/env python

"""
"""

import numpy.random as rnd

maxN = 5
newalpha_step = 0.03125


def changeAlpha(new):
	global newalpha_step
	newalpha_step = new

def changeN(newN):
	global maxN 
	maxN = newN
	return

def rand_in_range(max): # returns integer, max: integer
    return rnd.randint(max)

def rand_un(): # returns floating point
    return rnd.uniform()

def rand_norm (mu, sigma): # returns floating point, mu: floating point, sigma: floating point
    return rnd.normal(mu, sigma)
    
