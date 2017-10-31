#!/usr/bin/env python

"""
 Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Sina Ghiassian, Zach Holland
 Purpose: for use of Rienforcement learning course University of Alberta Fall 2017
"""

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
	data1 = open("output1.txt", "r")

	datay1 = []
	datax1 = [0.03125,0.0625,0.125,0.25,0.5,1.0]

	for line in data1:
		line = line.strip()
		datay1.append(line)
	plt.show()

	plt.plot(datax1,datay1,label = "n=5")
	plt.ylim(1,100)
	plt.yticks([0,20,40,60,80,100])
	plt.ylabel('steps per episode')
	plt.xlabel('alpha')
	plt.legend()
	plt.show()