#Plots for one-dimensional data -- HISTOGRAMS

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(0, 1, 1000)
plt.hist(x, bins=20)
plt.show()
#Will display data as a normally distributed histogram
#Distribution is as a result of the method used to generate data
#Bars referred to as bins, and we can specify the number of bins
#Here, we specified 20 bins

#Two Seperate Plots

plt.subplot(1, 2, 1)
# 1 row, 2 columns and this is the first one
x = np.random.normal(0, 1, 1000)
plt.hist(x)

plt.subplot(1, 2, 2)
# 1 row, 2 columns and this is the second
x = np.random.uniform(-3, 3, 1000)
#Uniform distribution specified this time
plt.hist(x)

plt.show()

#Other plots and Ian's examples can be found here: https://github.com/ianmcloughlin/pyplot-examples
