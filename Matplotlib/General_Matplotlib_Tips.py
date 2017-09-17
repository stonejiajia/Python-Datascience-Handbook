
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

fig = plt.figure
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--')



from ipython.display import image
Image('my_figure')
