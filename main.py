import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

df1 = pd.read_csv('cpiypl_m_d.csv')
df2 = pd.read_csv('usdpln_m.csv')
df3 = pd.read_csv('wig20_m.csv')
df4 = df2['Data']

df1['Month'] = pd.DatetimeIndex(df1['Data']).month
df1['Year'] = pd.DatetimeIndex(df1['Data']).year
df1['Period'] = pd.to_datetime(df1[['Year', 'Month']].assign(DAY=1))


df2['Month'] = pd.DatetimeIndex(df2['Data']).month
df2['Year'] = pd.DatetimeIndex(df2['Data']).year
df2['Period'] = pd.to_datetime(df2[['Year', 'Month']].assign(DAY=1))

df3['Month'] = pd.DatetimeIndex(df3['Data']).month
df3['Year'] = pd.DatetimeIndex(df3['Data']).year
df3['Period'] = pd.to_datetime(df3[['Year', 'Month']].assign(DAY=1))

corr1, _ = pearsonr(df1['Zamkniecie'], df3['Zamkniecie'])
print('Pearsons correlation: %.3f' % corr1)

corr2, _ = pearsonr(df1['Zamkniecie'], df2['Zamkniecie'])
print('Pearsons correlation: %.3f' % corr2)

corr3, _ = pearsonr(df3['Zamkniecie'], df2['Zamkniecie'])
print('Pearsons correlation: %.3f' % corr3)

fix, ax1 = plt.subplots()

date = df1['Period']
cpi = df1['Zamkniecie']
usd = df2['Zamkniecie']
wig = df3['Zamkniecie']

ax1.plot(date,cpi, color='blue')

ax2 = ax1.twinx()
ax2.plot(date,usd, color='red')

ax3 = ax1.twinx()
ax3.plot(date,wig, color='green')
plt.show()
