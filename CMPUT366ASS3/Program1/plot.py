#!/usr/bin/env python

"""
 Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Sina Ghiassian, Zach Holland
 Purpose: for use of Rienforcement learning course University of Alberta Fall 2017
"""

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