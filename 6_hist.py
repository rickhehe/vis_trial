import pandas as pd
import matplotlib.pyplot as plt

#plt.style.use('seaborn')
plt.style.use('fivethirtyeight')
#plt.xkcd()

raw = r'hist.csv'
df = pd.read_csv(raw)

#print(df.head())
ages = df['Age']
ids = df['Responder_id']

bins=[10,20,30,40,50,60,70]

plt.hist(
    ages,
    #bins=bins,
    bins=10,
    edgecolor='black',
)

# add a vertical line
median_age = 29
plt.axvline(
    median_age,
    color='#fc4f30',
    label='Age Median',
    linewidth=2,
)

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.legend()

plt.tight_layout()
plt.savefig('hist.png')

plt.show()
