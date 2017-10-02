
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
V = {} 
Pi = {}
dis = 0.9 # you may need change it
head_pro = 0.6 # you may need change it
small_number = 0.001 # you may need change it




# initial dict V from 1 to 99 each value is 0
def initializeV():
	global dis,Pi,V
	for key in range(1,100):
		V[key] = 0
		Pi[key] = []
		Pi[key].append(min(key,100-key))


	return

# value evaluation 
def getVmap(small_p_number):
	global dis,Pi,V,version
	loop = True

	while loop:
		difference = 0
		for s in range(1,100):
			v = V[s]
			V[s] = getMaxValueUnderS(s)
			difference = max(abs(V[s]-v),difference)
		if difference < small_p_number:
			loop = False 
	return

#update policy check if policy is stable
def updatePolicy():
	global dis,Pi,V
	stable = True
	for s in range(1,100):
		old_action = Pi[s]
		Pi[s] = getBestActionUnderS(s)
		if Pi[s] != old_action:
			stable = False
	return stable

# under state s find the best actions
def getBestActionUnderS(s):
	global dis,Pi,V
	maxValue = 0
	best_action = []
	for action in range(1,min(s,100-s)+1):
		head_result = 0
		if s+action >=100:
			head_result = 1

			head = head_pro*(head_result + dis*0) #0.6 pro to go next state = state+reward
		else:
			head = head_pro*(head_result + dis*V[action+s]) #0.6 pro to go next state = state+reward
		
		back_result = 0
		if s-action<= 0:
			back = (1- head_pro)*(back_result + dis*0)
		else:
			back = (1- head_pro)*(back_result + dis*V[s-action])
		if  (head+back)>maxValue:
			best_action = [action]
			maxValue = head+back
		elif (head+back) == maxValue:
			best_action.append(action)
	return best_action

# input: s: int    s->state
# output: value: float    value->V[s]
def getMaxValueUnderS(s):
	global dis,Pi,V
	totalValue = 0

	for action in Pi[s]: # action 
		head_result = 0
		if s+action >=100:
			head_result = 1
			gameOver = True
			head = head_pro*(head_result + dis*0) #0.6 pro to go next state = state+reward
		else:
			head = head_pro*(head_result + dis*V[action+s]) #0.6 pro to go next state = state+reward
		
		back_result = 0
		if s-action<= 0:
			gameOver = True
			back = (1- head_pro)*(back_result + dis*0)
		else:
			back = (1- head_pro)*(back_result + dis*V[s-action])

		totalValue += (head+back)
	return totalValue/float(len(Pi[s]))



def main():

	start_time = time.time()
	npV = np.zeros(99)
	npPi = np.zeros(99)
	initializeV() #initial V
	getVmap(small_number) # first find all value(value evaluation)
	stable = updatePolicy() #check if stable
	while stable == False :  #if V != v* pi != Pi*
		getVmap(small_number) #value evaluation
		stable = updatePolicy() #check if stable
	for i in range(0,99):
		npV[i] = V[i+1]
		npPi[i] = Pi[i+1][-1]
	np.save("Value",npV)
	np.save("Policy",npPi)

	end_time = time.time()
	print("------total time----> %f sec" %round((time.time() - start_time),2))

	return
if __name__ == '__main__':
	main()


