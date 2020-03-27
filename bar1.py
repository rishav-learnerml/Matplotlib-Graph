# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 08:39:11 2019

@author: Dell
"""
import matplotlib.pyplot as plt
plt.bar([2,4,6,8], [7,11,15,3],label = "Democracy")
plt.bar([2,8,6,3], [9,6,5,8], label = "Population", color = "g")
plt.legend()
plt.xlabel("increase")
plt.ylabel("decrease")
plt.show()