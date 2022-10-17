import matplotlib
import pandas as pn
matplotlib.use('Tkagg')
import matplotlib.pyplot as plt
import apiRequests

moths = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
# creating the dataset
res = apiRequests.getImports()
df = pn.DataFrame(res)
# TABLE 1
tb1 = df[['month','year','total']].values.tolist()
plt.figure(figsize =(10, 7))
plt.xticks(
    rotation=45, 
    horizontalalignment='right',
    fontweight='light',
    fontsize='small'  
)
plt.bar(
    ["{}/{}".format(moths.index(str(i[0]).replace(" ","")) +1 ,str(i[1])[2:4]) for i in tb1],
    [i[2] for i in tb1],
        width = 0.7),
plt.xlabel('Months')
plt.ylabel('Total mean')
plt.savefig('accomulative_mean.png', bbox_inches='tight')
plt.show()
# TABLE 2
tb2 = df.groupby(['year'],as_index=False)['total'].mean().values.tolist()
plt.plot(
    [i[0] for i in tb2],
    [i[1] for i in tb2],
    '-ok')
plt.xlabel('Year')
plt.ylabel('Total mean')
plt.savefig('total_mean.png', bbox_inches='tight')
plt.show()
# TABLE 3
tb3 = df.groupby(['year'],as_index=False)['consumerGoods'].mean().values.tolist()
plt.plot(
    [i[0] for i in tb3],
    [i[1] for i in tb3],
    '-ok')
plt.xlabel('Year')
plt.ylabel('Consumer goods mean')
plt.savefig('consumer_goods_mean.png', bbox_inches='tight')
plt.show()
