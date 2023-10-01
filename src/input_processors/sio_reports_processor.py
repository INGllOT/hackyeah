import os
import numpy as np
import pandas as pd
import csv

def _parse_regon(regon: str) -> int:
    return int(float(regon.replace(' ', '')))

def load_sio_pupils(file: str) -> pd.DataFrame:
    input = csv.reader(file,delimiter=';')
    data = np.array(list(input))[5:]
    szkoly_podstawowe = data[data[::,10]=="Szkoła podstawowa"]
    gminne_szkoly_podstawowe = szkoly_podstawowe[szkoly_podstawowe[::,26]!="Organizacje Wyznaniowe"]
    gminne_szkoly_podstawowe[::,0] = [_parse_regon(x) for x in gminne_szkoly_podstawowe[::,0]]
    return pd.DataFrame(gminne_szkoly_podstawowe,columns=data[0])
    
def process_files_in_directory(dirname: str) -> pd.DataFrame:
    reports = None
    for filename in os.listdir(dirname):
        if filename.startswith("SIO 30") and filename.endswith("csv"):
            with open("../Kutno_HackSQL/" + filename, "r") as f:
                result = load_sio_pupils(f)
                result['Year'] = int(filename[-8:-4])
                if reports is None:
                    reports = result
                else:
                    result = result.reset_index(inplace=True, drop=True)
                    pd.concat([reports,result])
    return reports

weights = {
    "Liczba uczniów":1,
    "Liczba uczniów poza szkołą":0.8,
    "P1":0.4,
    "P2":0.2,
    "P3":0.33,
    "P4":0.2,
    "P5":1.4,
    "P6":2.9,
    "P7":3.6,
    "P8":9.5,
    "P9":0.8,
    "P10":0.082,
    "P11":0.12,
    "P12":0.4,
    "P13":0.95,
    "P14":0.85,
    "P15":0.23,
    "P16":0.4,
    "P17":0.35,
    "P18":0.29,
    "P19":0.23,
    "P20":0.1,
    "P21":0.08,
    "P22":0.2,
    "P23":0.08,
    "P24":0.2,
    "P25":0.08,
    "P26":0.05, 
    "P27":0.2,
    "P27a":0.1,
    "P28":1,
    "P28a":0.5,
    "P29":1.3,
    "P29a":0.65,
    "P30":0.6,
    "P31":0.2,
    "P32":1,
    "P33":0.85,
    "P34":0.85,
    "P35":1.5,
    "P36":2.01,
    "P37":3.36,
    "P38":0.92,
    "P39":1,
    "P40":1.35,
    "P41":1.1,
    "P42":1.94,
    "P43":0.6,
    "P44":0.17,
    "P45":0.06,
    "P46":0.05,
    "P47":3, 
    "P48":0.36,
    "P49":0.345,
    "P50":0.68,
    "P51":0.065,
    "P52":1.5,
    "P53":0.4,
    "P54":0.025,
    "P55":0.012,
    "P56":0.18,
    "P57":0.112,
    "P58":0.045,
    "P59":0.015,
    "P60":0.011,
    "P61":0.75,
    "P62":0.66,
    "P63":0.15,
    "P64":3.04,
    "P65":1.5,
    "P66":0.5,
    "P67":3.64,
    "P68":6.3,
    "P69":6.5,
    "P70":7.8,
    "P71":5,
    "P72":10,
    "P73":1.5,
    "P74":9.5,
    "P75":0.02,
    "P76":0.84,
    "P77":0.25,
    "P78":2.9,
    "P79":3.6,
    "P80":0.18,
    "P81":0.112,
    "P82":0.045,
    "P83":0.015,
    "P84":0.011,
    "P85":0.191,
    "P86":0.146,
    "P87":0.079,
    "P88":0.045,
    "P89":0.039,
    "P90":0.18
}