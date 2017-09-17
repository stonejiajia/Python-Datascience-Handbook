#!/usr/bin/env python



 import matplotlib.pyplot as plt 
 plt.style.use('classic')
 import numpy as np

 x = np.linspace(0, 10, 1000)
 fig, ax = plt.subplots()
 ax.plot(x, np.sin(x), '-b', label='Sine')
 ax.plot(x, np.cos(x), '--b', label='Cosine')
 ax.axis('equal')
 leg = ax.legend()
 ax.legend(loc='lower center', frameon=False, ncol=2)
 

 fig
 plt.show()
 
 
 
