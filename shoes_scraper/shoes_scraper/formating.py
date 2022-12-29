
import pandas as pd
import json
import sys, os 
sys.path.append('../')

with open(r'shoes.json') as json_file:
   df = pd.DataFrame(json.load(json_file))

df['address'] = '65 Rue de Saintonge'
df['city'] =  'Paris' 
df['Lat,Long'] = '48.86391830444336, 2.3650076389312744'
# df['opening hours'] = ['Lundi 14h-19h', 'Mardi 11h-19h',
#                         'Mercredi 11h-19h', 'Jeudi 11h-19h,
#                         'Vendredi 14h-19h', 'Samedi 11h-19h',
#                         'Dimanche 14h-19h']


# df.to_csv('../shoes.csv', encoding = 'utf-8-sig')
# Save to excel file 
df.to_excel('../shoes.xlsx', encoding = 'utf-8-sig')