import matplotlib.pyplot as plt
import numpy as np
X = np.linspace(-3,3,100)
Y = [x**2 for x in X]
plt.plot(X,Y)
plt.show()