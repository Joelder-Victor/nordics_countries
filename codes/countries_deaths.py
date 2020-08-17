import weasyprint as wsp
import PIL as pil
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

url='https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
countries_covid=pd.read_csv(url,sep=',')

def trim(source_filepath, target_filepath=None, background=None):
    '''
    Recebe uma imagem e recorta, para um tamanho que 
    comporte os dados.
    '''
    if not target_filepath:
        target_filepath = source_filepath
    img = pil.Image.open(source_filepath)
    if background is None:
        background = img.getpixel((0, 0))
    border = pil.Image.new(img.mode, img.size, background)
    diff = pil.ImageChops.difference(img, border)
    bbox = diff.getbbox()
    img = img.crop(bbox) if bbox else img
    img.save(target_filepath)

def countries_deaths(df,number,countries):
    '''
     Recebe um dataframe,um número inteiro que diz
     respeito número de óbitos que se deseja buscar
     e por fim recebe um dicionário com os nomes dos 
     países em inglês e português.
    '''
    indexes=[]
    deaths=pd.DataFrame()
    for country in countries.keys():
        temp=df.set_index('Date').query('Country== @country and Deaths>=@number')['Deaths']
        indexes.append(temp.index[0])
    index=min(indexes)
    for country in nordics.keys():
        temp=df.set_index('Date').query('Country== @country and Date>=@index')['Deaths']
        temp.name='Óbitos '+countries[country]
        deaths=pd.concat([deaths,temp],axis=1)
    return deaths

def countries_deaths_graphic(df,days):
    '''
    Recebe um dataframe e número de dias que 
    se deseja plotar o gráfico.
    '''
    df=df.head(days)
    fig,ax=plt.subplots(figsize=(11,9))
    for name in ['Óbitos Suécia','Óbitos Noruega','Óbitos Dinamarca']:
        ax.plot(pd.to_datetime(df.index),df[name],label=name)
    ax.set_xlabel('Data') 
    ax.set_ylabel('Número de Óbitos') 
    ax.set_title(' Óbitos por COVID-19')
    ax.legend()
    if days<=7:
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    elif days<=30:
        ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1)) 
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=7))
    else:
        ax.xaxis.set_minor_locator(mdates.DayLocator(interval=7)) 
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=21))
            
    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=45)
    fig.savefig('day_'+str(days)+'_deaths.png')
    
nordics={'Sweden':'Suécia','Norway':'Noruega','Denmark':'Dinamarca'}
d10=countries_deaths(countries_covid,10,nordics).fillna(0)
countries_deaths_graphic(d10,7)
d10=countries_deaths(countries_covid,10,nordics).fillna(0)
countries_deaths_graphic(d10,30)
d50=countries_deaths(countries_covid,50,nordics).fillna(0)
countries_deaths_graphic(d50,len(d50))

img_filepath = 'd10_table.png'
css = wsp.CSS(string='''
@page { size: 2048px 2048px; padding: 0px; margin: 0px; }
table, td, tr, th { border: 1px solid black; }
td, th { padding: 4px 8px; }
''')
html = wsp.HTML(string=d10.head(6).to_html())
html.write_png(img_filepath, stylesheets=[css])
trim(img_filepath)

img_filepath = 'd50_table.png'
css = wsp.CSS(string='''
@page { size: 2048px 2048px; padding: 0px; margin: 0px; }
table, td, tr, th { border: 1px solid black; }
td, th { padding: 4px 8px; }
''')
html = wsp.HTML(string=d50.head(9).to_html())
html.write_png(img_filepath, stylesheets=[css])
trim(img_filepath)