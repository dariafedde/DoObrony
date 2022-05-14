# Praca Dyplomowa Daria Fedde

### Requirements
    * Python 3.10.4 
    * Pandas 1.4.2
    
### Uruchomienie
    
``` python
python DoObrony.py 
```

### Analiza danych z wypadków w USA, na podstawie bazy 


```
import pandas as pd
import os
import pathlib
```


**Wczytanie pliku**
```
'df = pd.read_csv(os.path.join(os.path.dirname(__file__), '../data/nypd-motor-vehicle-collisions.csv'))'
```
**Wyciągnięcie danych**
(dane wyciągam na podstawie pliku .csv,  i przeprowadzam analizę na różne sposoby)




### Analiza osób które zginęły w różnych stanach 
wykorzystana funkcja `calculate_deaths_in_selected_borough`
Paramerty:
* borough_name: str - nazwa stanu
* nypd_collisions_data: DataFrame - dane wyjściowe w formie DataFrame

### Wyznaczenie godziny, z najwyższym współczynnikiem  wypadków 

wykorzystana funkcja `calculate_agg_accident_time_max`
Paramerty:

* nypd_collisions_data: DataFrame - dane wyjściowe w formie DataFrame

### Wyznaczenie stanów, w których najczęściej dochodzi do wypadków 
wykorzystana funkcja `calculate_agg_borough_max`
Paramerty:

* nypd_collisions_data: DataFrame - dane wyjściowe w formie DataFrame
* max_list: int - default = 5, oraniczenie listy stanów do podanej liczby

### Statystyka średniej ilości wypadków przy  udziale osób pieszych, rowerów i motocyklistów 

wykorzystana funkcja `calculate_agregate_number_accident_mean`
Paramerty:

* nypd_collisions_data: DataFrame - dane wyjściowe w formie DataFrame
*  locomotion_type: str - możliwe do wyboru: PEDESTRIANS, CYCLIST, MOTORIST

### Ilość ulilc z największą liczbą wypadków w stanach

wykorzystana funkcja `clalculate_accident_per_street_per_borough`
Paramerty:

* nypd_collisions_data: DataFrame - dane wyjściowe w formie DataFrame
* max_street_list: int - default = 5, Maksymalna ilość ulic w liście, którą chcemy wyświetlić
* max_borough_list: int default = 3, Maksymalna ilość stanów, z których chcemy wyciągnąć ulice




### Dziękuję


