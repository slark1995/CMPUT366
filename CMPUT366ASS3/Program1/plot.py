#!/usr/bin/env python

"""
 Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Sina Ghiassian, Zach Holland
 Purpose: for use of Rienforcement learning course University of Alberta Fall 2017
"""

'''*
 * Copyright (c) HAOTIAN ZHU ,COMPUT301,University Of Alberta All Rights Reserved.
 * You May Use, Distribute Or Modify This Code Under Term And 
 * Condition Of Code Of Students Behavior At University Of Alberta.
 *
 *
 * Author: Haotian Zhu 
 * Modify the code of Assignment3 plot.py
 * If You Have Any Question Please contact haotian1@ualberta.ca.
 * '''

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
   a = int(input("V(1) or Pi(2), enter 1 or 2: "))
   if a == 1:
      V = np.load('Value.npy')
   elif a ==2:
      V = np.load('Policy.npy')
   else:
      print("error input")
   plt.show()
   plt.plot(V,label='')
   plt.xlim([0,100])
   plt.xticks([1,25,50,75,99])
   plt.xlabel('Capital')
   plt.ylabel('Value estimates')
   plt.legend()
   plt.show()