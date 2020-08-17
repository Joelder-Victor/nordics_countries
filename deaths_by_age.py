import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def death_by_age_graphic(nordics):
    death_by_age=pd.DataFrame()
    for country in nordics.keys():
        temp=pd.read_csv('deaths_by_age_'+country+'.csv',sep=',',index_col=0).fillna(0)
        death_by_age=pd.concat([death_by_age,temp],axis=1).rename(columns={"Deaths":"Óbitos por idade "+nordics[country]})
    
    return death_by_age

death_by_age=death_by_age_graphic({'sweden':'Suécia','norway':'Noruega','denmark':'Dinamarca'})
fig,ax=plt.subplots(figsize=(11,7))
ax.barh(death_by_age.index,death_by_age['Óbitos por idade Suécia'], label='Óbitos por idade Suécia',color='#FECB00')
ax.barh(death_by_age.index,death_by_age['Óbitos por idade Noruega'],label='Óbitos por idade Noruega',color='#EF2B2D')
ax.set_xlabel('Número de Óbitos')
ax.set_ylabel('Idade')
ax.legend()
fig.savefig('SwedenXNorway.png')

fig,ax=plt.subplots(figsize=(11,7))
ax.barh(death_by_age.index,death_by_age['Óbitos por idade Suécia'], label='Óbitos por idade Suécia',color='#FECB00')
ax.barh(death_by_age.index,death_by_age['Óbitos por idade Dinamarca'],label='Óbitos por idade Dinamarca',color='#C60C30')
ax.set_xlabel('Número de Óbitos')
ax.set_ylabel('Idade')
ax.legend()
fig.savefig('SwedenXDenmark.png')