import openpyxl
import pandas as pd
import numpy as np



def load_exam(file_path) -> pd.DataFrame:
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active
    for i in range(12,52):
        ws.cell(row=2,column=i).value = f"{ws.cell(row=2,column=i).value} [{ws.cell(row=1,column=(i-(i-2)%5)).value}]"
    data = np.array(list(ws.values))
    cols = data[1]
    data = data[data[:,2]=="Kutno"]

    return pd.DataFrame(data,columns=cols)