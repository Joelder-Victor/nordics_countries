import pandas as pd
import matplotlib.pyplot as plt

indicators=pd.read_csv('indicators.csv',sep=',',index_col=0)
# PIB pr capita
ppp=indicators['PPP(US$)']
fig,ax=plt.subplots(figsize=(11,7))
ax.bar(ppp.index,ppp,width=0.4,color='#FECB00',edgecolor='black')
ax.set_title('PIB per capita')
ax.set_ylabel('Valor em US$')
ax.set_xlabel('Países')
fig.savefig('ppp.png')

#Desindade Populacional
dp=indicators['DP(p/km²)']
fig,ax=plt.subplots(figsize=(11,7))
ax.bar(dp.index,dp,width=0.4,color='#D7DF01',edgecolor='#04B4AE')
ax.set_title('Densidade Populacional')
ax.set_xlabel('Países')
ax.set_ylabel('Pessoas por km²')
fig.savefig('dp.png')

# População
pop=pd.concat([indicators['População'],indicators['População Urbana']],axis=1)
fig,axs=plt.subplots(figsize=(11,7))
pop.plot.bar(ax=axs,rot=0)
axs.set_ylabel("População em milhões")
fig.savefig('pop.png')

#IDH
idh=indicators['IDH']
fig,ax=plt.subplots(figsize=(11,7))
ax.bar(idh.index,idh,width=0.4,color='#FE9A2E',edgecolor='#04B4AE')
ax.set_title('Índice de Desenvolvimento Humano')
ax.set_xlabel('Países')
ax.set_ylabel("IDH")
fig.savefig('idh.png')