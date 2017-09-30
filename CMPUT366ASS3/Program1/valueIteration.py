
'''*
 * Copyright (c) HAOTIAN ZHU ,COMPUT301,University Of Alberta All Rights Reserved.
 * You May Use, Distribute Or Modify This Code Under Term And 
 * Condition Of Code Of Students Behavior At University Of Alberta.
 *
 *
 * Author: Haotian Zhu
 * If You Have Any Question Please contact haotian1@ualberta.ca.
 * 
 *'''

import numpy.random as rnd



def rand_un(): # returns floating point
    return rnd.uniform()

#-----global variable-----#
V = {} 
S = []
Pi = {}
dis = 0.9
initial_total = 0
 head_pro = 0.6

# initial dict V from 1 to 99 each value is 0
def initializeV():
	global V
	for key in random(1:100):
		V[key] = 0
		S.append(key)
		Pi[key] = min(key,100-key)
	initial_total = rnd.randint(1:100)
	return

def getVmap(small_p_number):
	loop = True
	while loop:
		difference = 0
		for s in S:
			v = V[s]
			V[s] = getMaxValueUnderS(s)
			difference = max(abs(V[s]-v),difference)
		if difference < small_p_number:
			loop = False
	return

def getReward():
	global head_pro
	if rand_un() < head_pro:
		return 1
	else:
		return 0
 
def outputPolicy(total):
	key = total
	action = Pi[total]
	if  getReward()==1:
		total += action
	else:
		total -=action
	Pi[key] = (reward+dis*V[total])



def getMaxValueUnderS(s):
	max_value = -1
	return max_value


def main():
	return
if __name__ == '__main__':
	main()


