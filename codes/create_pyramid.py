import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def create_pyramids(countries):
    '''
    Recebe  um dicionário em que as chaves
    são os nomes dos países em português e
    os valores são dataframes,  contendo as
    populações divididas por faixa etária.
    '''
    t=0
    fig,ax=plt.subplots(1,len(countries),figsize=(15,7),sharex=True)
    for i in countries.items():
        M=i[1]['M']
        F=i[1]['F']
        Age=i[1]['Age']
        ax[t].barh(Age,-M,label='Masculino',color='blue')
        ax[t].barh(Age,F,label='Feminino',color='red')
        ax[t].legend()
        plt.xticks([])
        ax[t].set_xlabel(i[0])  
        t+=1
    
    fig.savefig('pyramids.png')

denmark=pd.read_csv('Denmark-2019.csv',sep=',')

norway=pd.read_csv('Norway-2019.csv',sep=',')

sweden=pd.read_csv('Sweden-2019.csv',sep=',')

countries={'Dinamarca':denmark,'Noruega':norway,'Suécia':sweden}
create_pyramids(countries)