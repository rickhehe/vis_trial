import pandas as pd
import matplotlib.pyplot as plt

#plt.style.use('seaborn')
plt.style.use('seaborn')
#plt.xkcd()

raw = r'scatter.csv'
df = pd.read_csv(raw)

print(df.head())

view_count = df['view_count']
likes = df['likes']
ratio = df['ratio']

plt.scatter(
    view_count,
    likes,
    s=100,
    c=ratio,
    cmap='summer',  # along w/ color bar
    alpha=0.75,
    linewidth=1,
    edgecolor='black',
)

plt.xscale('log')
plt.yscale('log')

# color bar
cbar = plt.colorbar()
cbar.set_label('Ratio')

plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Likes')
#
#plt.legend()

plt.tight_layout()
plt.savefig('scatter.png')

#plt.show()
