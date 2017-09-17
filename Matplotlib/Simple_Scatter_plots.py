

%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

x = np.linspace(0, 10, 300)
y = np.sin(x)
plt.plot(x, y, 'o', color='black')

x = np.linspace(-15, 15, 100)
y = np.sin(x)/x

plt.plot(x, y)
plt.plot(x, y, 'co')
plt.plot(x, 2*y, x, 3*y)

rng = np.random.RandomState(0)
for marker in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
    plt.plot(rng.rand(5), rng.rand(5), maker,
             label="maker='{0}'".format(marker))
    plt.legend(numpoints=1)
    plt.xlim(0, 1.8)

plt.plot(x, y, '-ok')


plt.plot(x, y, '-p', color='gray',
         markersize=15, linewidth=4,
         markerfacecolor='white',
         markeredgecolor='gray',
         markeredgewidth=2)
plt.ylim(-1.2, 1.2)



plt.scatter(x, y, marker='o')


rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,
            cmap='viridis')
plt.colorbar()

import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
features = iris.data.T
data = pd.DataFrame(features)
data
plt.scatter(features[0], features[1], alpha=0.2,
            s=100*features[3], c=iris.target, cmap='viridis')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
