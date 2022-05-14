# Praca Dyplomowa Daria Fedde

### Analiza danych z wypadków w USA, na podstawie bazy 

import pandas as pd
import os
import pathlib



**Wczytanie pliku**
'df = pd.read_csv(os.path.join(os.path.dirname(__file__), '../data/nypd-motor-vehicle-collisions.csv'))'

**Wyciągnięcie danych**
(dane wyciągam na podstawie pliku .csv,  i przeprowadzam analizę na różne sposoby)




### Analiza osób które zginęły w różnych stanach 

def calculate_deaths_in_selected_borough(borough_name: str, nypd_collisions_data: pd.DataFrame) -> int:
    dead_manhattan = nypd_collisions_data[nypd_collisions_data.BOROUGH == borough_name]
    return dead_manhattan['NUMBER OF PERSONS KILLED'].sum().astype(int)

### Wyznaczenie godziny, z najwyższym współczynnikiem  wypadków 

def calculate_agg_accident_time_max(nypd_collisions_data: pd.DataFrame):
    agg_accident_time_max = nypd_collisions_data.agg({'ACCIDENT TIME': 'max'})
    return agg_accident_time_max['ACCIDENT TIME']

### Wyznaczenie stanów, w których najczęściej dochodzi do wypadków 

def calculate_agg_borough_max(nypd_collisions_data: pd.DataFrame, max_list: int = 5) -> list:
    nypd_collisions_data["NUMBER OF PERSONS"] = nypd_collisions_data[f"NUMBER OF PERSONS INJURED"] + \
                                                nypd_collisions_data[f"NUMBER OF PERSONS KILLED"]
    agg_borough_max = nypd_collisions_data.groupby('BOROUGH').agg({'NUMBER OF PERSONS': 'max'})
    borough_list = agg_borough_max.sort_values('NUMBER OF PERSONS', ascending=False).index.tolist()[:max_list]
    return borough_list

### Statystyka średniej ilości wypadków przy  udziale osób pieszych, rowerów i motocyklistów 

def calculate_agregate_number_accident_mean(nypd_collisions_data: pd.DataFrame, locomotion_type: str) -> float:
    nypd_collisions_data[f"NUMBER OF {locomotion_type}"] = nypd_collisions_data[
                                                               f"NUMBER OF {locomotion_type} INJURED"] + \
                                                           nypd_collisions_data[f"NUMBER OF {locomotion_type} KILLED"]
    agg_number_of_motorist_mean = nypd_collisions_data.agg({f'NUMBER OF {locomotion_type}': 'mean'})
    return agg_number_of_motorist_mean[f'NUMBER OF {locomotion_type}'].round(2)

### 5 ulica z największą liczbą wypadków z 3 stanów z największą liczbą wypadków" 

def clalculate_accident_per_street_per_borough(nypd_collisions_data: pd.DataFrame, max_street_list: int = 5,
                                               max_borough_list: int = 3) -> list:
    nypd_collisions_data["NUMBER OF PERSONS"] = nypd_collisions_data[f"NUMBER OF PERSONS INJURED"] + \
                                                nypd_collisions_data[f"NUMBER OF PERSONS KILLED"]
    borough_list = calculate_agg_borough_max(nypd_collisions_data, max_borough_list)
    dt_streets = nypd_collisions_data[nypd_collisions_data.BOROUGH.isin(borough_list)].groupby(['ON STREET NAME']).agg(
        {'NUMBER OF PERSONS': 'sum'})
    dt_streets_list = dt_streets.sort_values('NUMBER OF PERSONS', ascending=False).index.tolist()[:max_street_list]
    return[street.replace(' ','') for street in dt_streets_list]

### Dziękuję


