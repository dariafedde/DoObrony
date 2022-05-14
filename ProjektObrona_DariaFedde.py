import pandas as pd
import os
import pathlib
# # pd.set_option('display.max_rows',500)
# pd.set_option('display.max_columns',50)
# # szerokość DF (wyświetlanie)
# pd.set_option('display.width',1000)
# pd.set_option('display.max_colwidth', 100)
#
ROOT_DIR = os.path.dirname(__file__)
#
# print(ROOT_DIR)
#
df= pd.read_csv(os.path.join(ROOT_DIR, '../data/nypd-motor-vehicle-collisions.csv'))
#
# #df.head()
#
#
#
#
# #ile osób zginęło na MANHATANIE
#
# # print('1. Ile osób zginęło na MANHATANIE?')
# # dead_manhattan = df[df.BOROUGH == 'MANHATTAN']
# #
# #
# # quantity = dead_manhattan['NUMBER OF PERSONS KILLED'].sum()
# # print(quantity)
#
# def calculate_deaths_in_selected_borough(borough_name: str, nypd_collisions_data: pd.DataFrame) -> int:
#     dead_manhattan = nypd_collisions_data[nypd_collisions_data.BOROUGH == borough_name]
#     return dead_manhattan['NUMBER OF PERSONS KILLED'].sum().astype(int)
#
# # tutaj poniżej wywołanie funkcji ( print aby pokazać wartość którą zwraca)
# print(calculate_deaths_in_selected_borough('MANHATTAN', df))
#
#
#
#
#
# #Jaka jest najczęstsza godzina wypadków
#
# print('2. Jaka jest najczęstsza godzina wypadków?')
#
# agg_accident_time_max = df.agg({'ACCIDENT TIME': 'max'})
# print(agg_accident_time_max)
#
#
#
# #w jakich 5 stanach najwiecej wypadków
#
# print('3. W jakich 5 stanach najwiecej wypadków?')
#
# agg_accident_time_max = df.groupby('BOROUGH').agg({'BOROUGH': 'max'})
# print(agg_accident_time_max)






def calculate_deaths_in_selected_borough(borough_name: str, nypd_collisions_data: pd.DataFrame) -> int:
    dead_manhattan = nypd_collisions_data[nypd_collisions_data.BOROUGH == borough_name]
    return dead_manhattan['NUMBER OF PERSONS KILLED'].sum().astype(int)

# tutaj poniżej wywołanie funkcji ( print aby pokazać wartość którą zwraca)
print(calculate_deaths_in_selected_borough('MANHATTAN', df))





# Jaka jest najczęstsza godzina wypadków
print('2. Jaka jest najczęstsza godzina wypadków?')

def calculate_agg_accident_time_max(nypd_collisions_data: pd.DataFrame):
    agg_accident_time_max = nypd_collisions_data.agg({'ACCIDENT TIME': 'max'})
    return agg_accident_time_max['ACCIDENT TIME']
print(calculate_agg_accident_time_max(df))



# w jakich 5 stanach najwiecej wypadków
print('3. W jakich 5 stanach najwiecej wypadków?')

def calculate_agg_borough_max(nypd_collisions_data: pd.DataFrame) -> list:
    agg_borough_max = nypd_collisions_data.groupby('BOROUGH').agg({'BOROUGH': 'max'})

    # print(type(agg_borough_max["BOROUGH"]))
    return agg_borough_max['BOROUGH'].tolist()

print(calculate_agg_borough_max(df))

#Średnia ilość wypadków z udziałem motocyklisty

print('4.Średnia ilość wypadków z udziałem motocyklisty')

def calculate_agregate_number_of_motorist_min(nypd_collisions_data: pd.DataFrame) ->int:
    nypd_collisions_data["NUMBER OF MOTORIST"] = nypd_collisions_data["NUMBER OF MOTORIST INJURED"] + \
                                                 nypd_collisions_data["NUMBER OF MOTORIST KILLED"]
    agg_number_of_motorist_mean = nypd_collisions_data.agg({'NUMBER OF MOTORIST': 'mean'})
    return agg_number_of_motorist_mean['NUMBER OF MOTORIST'].round(2)
print(calculate_agregate_number_of_motorist_min(df))

#