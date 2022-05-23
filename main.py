import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('cpiypl_m_d.csv')
df2 = pd.read_csv('usdpln_d.csv')
df3 = pd.read_csv('wig20_d.csv')

# cpi plot
# i = df1['Data']
# j = df1['Zamkniecie']

# plt.plot(i, j)
# plt.xlabel('Date')
# plt.ylabel('Inflation')
# plt.title('CPI Y/Y')
# plt.show()

# usdpln plot
# k = df2['Data']
# m = df2['Zamkniecie']

# plt.plot(k, m)
# plt.xlabel('Date')
# plt.ylabel('Currency rate')
# plt.title('USDPLN D/D')
# plt.show()

# wig20 plot
# n = df2['Data']
# o = df2['Zamkniecie']

# plt.plot(n, o)
# plt.xlabel('Date')
# plt.ylabel('Pts')
# plt.title('WIG20 D/D')
# plt.show()
