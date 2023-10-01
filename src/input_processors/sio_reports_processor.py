import numpy as np
import pandas as pd
import csv

def _parse_regon(regon: str) -> int:
    return int(float(regon.replace(' ', '')))

def load_sio_pupils(file_path: str) -> pd.DataFrame:
    with open(file_path, 'r') as f:
        input = csv.reader(f,delimiter=';')
        data = np.array(list(input))[1:]
        szkoly_podastawowe = data[data[::,10]=="Szkoła podstawowa"]
        gminne_szkoly_podstawowe = szkoly_podastawowe[szkoly_podastawowe[::,26]!="Organizacje Wyznaniowe"]
        gminne_szkoly_podstawowe[::,0] = [_parse_regon(x) for x in gminne_szkoly_podstawowe[::,0]]
        return pd.DataFrame(gminne_szkoly_podstawowe,columns=data[0])


def load_sio_teachers(file_path: str) -> pd.DataFrame:
    with open(file_path, 'r') as f:
        input = csv.reader(f,delimiter=';')
        teachers = np.array(list(input))[5:][:2]
        return pd.DataFrame(teachers[1:],columns=teachers[0])

# print(load_sio_teachers('Kutno_HackSQL/SIO 30.09.2021_Nauczyciele.csv'))
# print(load_sio_pupils('Kutno_HackSQL/SIO 30.09.2021.csv'))