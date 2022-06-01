import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')


# x-axis
minutes = list(range(1,10))

# I wonder if I could use dict.
# zip may help.

# series
p1 = [1,2,3,3,4,4,4,4,5]
p2 = [1,1,1,1,2,2,2,3,4]
p3 = [1,1,1,2,2,2,3,3,3]

labels = ['p1', 'p2', 'p3']
colors = ['#6d904f', '#008fd5', 'fc4f30']

plt.stackplot(
    minutes,
    p1,
    p2,
    p3,
    labels=labels,
    colors=colors
)

# explicitly specify legend and location.
plt.legend(loc='upper left')

plt.title('My Awesome Whatever Chart')
plt.tight_layout()

plt.savefig('stackplot.png')
