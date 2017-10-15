#!/usr/bin/env python

"""
 Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Sina Ghiassian, Zach Holland
 Purpose: for use of Rienforcement learning course University of Alberta Fall 2017
"""

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
	data= open("output.txt", "r")
	datax = []
	datay = []
	plt.show()
	for line in data:
		line = line.strip()
		x = int(line.split(",")[0])
		datax.append(x)
		y = int(line.split(",")[1])
		datay.append(y)

	for i in [0,49,149,199,249,-1]:	
		plt.plot(datax[i],datay[i],"ro")
		plt.text(datax[i], datay[i], "("+str(datax[i])+","+str(datay[i])+")")
	plt.plot(datax,datay)
	plt.xlim([0,8000])
	plt.xticks([0,1000,2000,3000,4000,5000,6000,7000,8000])
	plt.xlabel('steps')
	plt.ylabel('episode')
	plt.legend()
	plt.show()