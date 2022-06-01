import pandas as pd
import matplotlib.pyplot as plt

#plt.style.use('ggplot')
#plt.style.use('fivethirtyeight')
plt.xkcd()

year = [2013, 2014, 2015, 2016]
aapl = [123, 145, 167, 155]
msft = [70 , 80, 65, 85]

fig, ax = plt.subplots(2,2)

ax[0,1].plot(
    year,
    aapl,
    color='g',
    linestyle='--',
    marker='x',
    label='x',
)

ax[0,1].plot(
    year,
    msft,
    color='k',
    linestyle='-',
    marker='^',
    label='xy'
)

ax[0,1].legend()
ax[0,1].set_title('title')
ax[0,1].set_xlabel('xlabel')
ax[0,1].set_ylabel('ylabel')


#ax[1,0].plot(year, msft, 'k')

#
ax[1,0].scatter(
    year,
    aapl,
    c='g',
    marker='o',
    label='x',
)

ax[1,0].scatter(
    year,
    msft,
    c='k',
    marker='o',
    label='xy'
)

ax[1,0].legend()
ax[1,0].set_title('title')
ax[1,0].set_xlabel('xlabel')
ax[1,0].set_xlabel('ylabel')

plt.tight_layout()

#plt.axis([2012, 2018, 0, 200])

plt.savefig('xxx.png')
plt.show()
