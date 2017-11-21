#!/usr/bin/env python

"""
 Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Sina Ghiassian, Zach Holland
 Purpose: for use of Rienforcement learning course University of Alberta Fall 2017
"""

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":


	#data1 = open("output1.txt", "r")
	data2 = open("output.txt", "r")
	#data3 = open("output3.txt", "r")
	#datay1 = []
	datay2 = []
	#datay3 = []

	#for line in data1:
		#line = line.strip()
		#datay1.append(line)
	for line in data2:
		line = line.strip()
		datay2.append(line)
	#for line in data3:
	#	line = line.strip()
	#	datay3.append(line)
	plt.show()

	#plt.plot(datay1,label = "n=0")
	plt.plot(datay2)
	#plt.plot(datay3,label = "n=50")
	plt.xlim([1,1000])
	plt.xticks([1,250,500,750,999])

	plt.legend()
	plt.show()
	
'''
##2

	#data1 = open("output1.txt", "r")
	data2 = open("output.txt", "r")
	#data3 = open("output3.txt", "r")
	#datay1 = []
	datay2 = []
	#datay3 = []

	#for line in data1:
		#line = line.strip()
		#datay1.append(line)
	for line in data2:
		line = line.strip()
		for i in range(100):
			datay2.append(line)
	#for line in data3:
	#	line = line.strip()
	#	datay3.append(line)
	plt.show()

	#plt.plot(datay1,label = "n=0")
	plt.plot(datay2)
	#plt.plot(datay3,label = "n=50")
	plt.xlim([1,1000])
	plt.xticks([1,250,500,750,999])

	plt.legend()
	plt.show()


	'''