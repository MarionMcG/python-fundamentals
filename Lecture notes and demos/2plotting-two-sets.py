#PLotting two sets of data on one set of axes

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.01)
#no.arange gives you a range of values that includes real numbers!!
#Above gives me every value from 0 to 10 using 0.01 intervals
y = 3*x + 1

noise = np.random.normal(0, 1.0, len(x))
#provides data that has centre 0, stnadard deviation 1 and length = x

plt.plot(x, y + noise, 'c.', label='Actual')
plt.plot(x, y, 'g-', label='Model')
#Title, axes labels and legend
plt.title('Simple Plot')
plt.xlabel('x values')
plt.ylabel('y labels')
##Before using plt.legend, make sure you have assigned labels to your sets of data!!
plt.legend()


plt.show()

#Taking forever for plots to appear when called....

