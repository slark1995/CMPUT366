
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
import numpy as np
import numpy.random as rnd
import sys, time


#-----global variable-----#
V = np.zeros(101)
npV = np.zeros((99,4))
totalValue = np.zeros(1)
npPi = np.zeros(99)
dis = 1 # you may need change it
head_pro = 0.4 # you may need change it
small_number = 0.0000000000000000000000000000001 # you may need change it
swp = 0



# value evaluation 
def getVmap(small_p_number):
	global dis,V,version,swp
	loop = True

	while loop:
		difference = 0
		for s in range(1,100): # 1-99
			v = V[s]
			V[s] = getMaxValueUnderS(s)
			difference = max(abs(V[s]-v),difference)
			if swp<3:
				npV[s-1][swp] = V[s]
			else:
				npV[s-1][3] = V[s]
		if difference < small_p_number:
			loop = False 
		swp+=1
	return



# input: s: int    s->state
# output: value: float    value->V[s]
def getMaxValueUnderS(s):
	global dis,V,totalValue
	maxValue = np.zeros(1)
	best_action = 0
	for action in range(1,min(s,100-s)+1): #0-min(s,100-s)
		if s+action >=100:
			totalValue[0] = head_pro*(1+ dis*V[action+s])+(1- head_pro)*(0 + dis*V[s-action])
		else:
			totalValue[0] = head_pro*(0+ dis*V[action+s])+(1- head_pro)*(0 + dis*V[s-action])
		if totalValue>maxValue:
			maxValue[0] = totalValue[0]
			best_action = action
	if maxValue < V[s]:
		maxValue = V[s]
		action =0
	npPi[s-1] = best_action
	return maxValue[0]



def main():
	start_time = time.time()
	getVmap(small_number) # first find all value(value evaluation)
	print("------total swp---->%d" %swp)
	np.save("Value",npV)
	np.save("Policy",npPi)

	end_time = time.time()
	print("------total time----> %f sec" %round((time.time() - start_time),2))

	return
if __name__ == '__main__':
	main()


