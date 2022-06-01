import matplotlib.pyplot as plt


plt.style.use('fivethirtyeight')


slices = [60, 40, 20]
labels = ['60', '40', '20']
colors = ['#008fd5', '#e5ae37','yellow']
explode = [0,0,.1]


plt.pie(
    slices,
    labels=labels,
    explode=explode,
    colors=colors,
    #autopct='%1.2f%%',
    autopct='%.2f%%',
    wedgeprops={'edgecolor':'black'}
)

plt.title('My Pie Chart - Where is the Party?')

# get rid of some padding
plt.tight_layout()

plt.savefig('pie.png')
#plt.show()
