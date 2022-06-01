import pandas as pd
import matplotlib.pyplot as plt

#plt.style.use('seaborn')
plt.style.use('fivethirtyeight')
#plt.xkcd()

raw = r'line.csv'
df = pd.read_csv(raw)

print(df.head())

plt.plot(
    df['Age'],
    df['All_Devs'],
    color='#444444',
    linestyle='--',
    label='All Devs'
)

plt.plot(
    df['Age'],
    df['Python'],
    #color='#444444',
    #linestyle='--',
    label='Python'
)

# fill_between
plt.fill_between(
    df['Age'],
    df['Python'],
    #df['All_Devs'],
    y2=57287,
    alpha=.25,
)

plt.legend()

plt.tight_layout()
plt.savefig('line_chart.png')

#plt.show()
