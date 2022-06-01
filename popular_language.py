from collections import defaultdict, Counter

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')

raw = 'language.csv'
df = pd.read_csv(raw)
df.columns = ['','language'] 

c = Counter(
    [
        i
            for row in df.itertuples()
                for i in row.language.split(';')
    ]
)

df = pd.DataFrame.from_dict(
    data=c,
    orient='index',
    columns=['counts']
)

df.sort_values(
    by='counts',
    #ascending=False,
    inplace=True
)


plt.barh(
    df.index,
    df.counts,
)

plt.title('Popular Languages')
plt.xlabel('Number of Users of Each Language')

# get rid of some padding
plt.tight_layout()

plt.savefig('popular_language.png')
#plt.show()
