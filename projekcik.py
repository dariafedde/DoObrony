import pandas as pd
import os
import pathlib
# pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',50)
# szerokość DF (wyświetlanie)
pd.set_option('display.width',1000)
pd.set_option('display.max_colwidth', 100)


ROOT_DIR = os.path.dirname(__file__)

print(ROOT_DIR)

df= pd.read_csv(os.path.join(ROOT_DIR, 'data/nypd-motor-vehicle-collisions.csv'))

#df.head()




#ile osób zginęło na MANHATANIE

print('1. Ile osób zginęło na MANHATANIE?')
dead_manhattan = df[df.BOROUGH == 'MANHATTAN']


quantity = dead_manhattan['NUMBER OF PERSONS KILLED'].sum()
print(quantity)





#Jaka jest najczęstsza godzina wypadków

print('2. Jaka jest najczęstsza godzina wypadków?')

agg_accident_time_max = df.agg({'ACCIDENT TIME': 'max'})
print(agg_accident_time_max)



#w jakich 5 stanach najwiecej wypadków

print('3. W jakich 5 stanach najwiecej wypadków?')

agg_accident_time_max = df.groupby('BOROUGH').agg({'BOROUGH': 'max'})
print(agg_accident_time_max)







