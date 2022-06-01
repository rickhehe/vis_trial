import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#plt.style.use('seaborn')
plt.style.use('fivethirtyeight')
#plt.xkcd()

raw = r'raw.csv'
df = pd.read_csv(raw)

fig, ax = plt.subplots(2,2)

ax[0,0].scatter(
    df.x,
    df.y1,
    color='k',
    marker='^'
)

ax[0,0].scatter(
    df.x,
    df.y2,
    color='b',
    marker='o'
)

ax[0,0].set_title('title 00')
ax[0,0].set_xlabel('x')
ax[0,0].set_ylabel('y')



ax[0,1].plot(
    df.x,
    df.y1,
    color='k',
    marker='^',
    linestyle='-',
)

ax[0,1].plot(
    df.x,
    df.y2,
    color='b',
    marker='o',
    linestyle='--',
)

ax[0,1].set_title('title 01')
ax[0,1].set_xlabel('x')
ax[0,1].set_ylabel('y')


raw = 'data.csv'
df = pd.read_csv(raw)
df.columns = ['','language'] 
counts = df.language.value_counts()
print(counts)

# setup bar width for making cluster column chart
x_indices = np.arange(len(df.x))
print(x_indices)
bar_width = 0.25

ax[1,1].bar(
    df.x-bar_width,
    df.y1,
    color='k',
    width=bar_width,
)

ax[1,1].bar(
    df.x,
    df.y2,
    color='b',
    width=bar_width,
)

ax[1,1].set_title('title 11')
ax[1,1].set_xlabel('x')
ax[1,1].set_ylabel('y')

#ax[1,1].set_xticks(
#    ticks=df.x,
#    #label=df.x  # how to set labels?
#)

# get rid of some padding
plt.tight_layout()

plt.savefig('fig.png')
#plt.show()

print(df.y2.value_counts())

most_
