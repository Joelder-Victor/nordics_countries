import weasyprint as wsp
import PIL as pil
import pandas as pd

indicators=pd.read_csv('indicators.csv',sep=',')
pop=pd.concat([indicators['Países'],indicators['População'],indicators['População Urbana'],indicators['População 65+']],axis=1)
temp=(pop['População Urbana']/pop['População'])*100
temp.name='População Urbana (%)'
pop=pd.concat([pop,temp],axis=1)
temp=(pop['População 65+']/pop['População'])*100
temp.name='População 65+ (%)'
pop=pd.concat([pop,temp],axis=1)

def trim(source_filepath, target_filepath=None, background=None):
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


img_filepath = 'pop_table.png'
css = wsp.CSS(string='''
@page { size: 2048px 2048px; padding: 0px; margin: 0px; }
table, td, tr, th { border: 1px solid black; }
td, th { padding: 4px 8px; }
''')
html = wsp.HTML(string=pop.to_html())
html.write_png(img_filepath, stylesheets=[css])
trim(img_filepath)