import pandas as pd


class School:
    school_name= ""
    rspo = ""
    regon = ""
    wyniki = []
    fin_raporty = []
    uczniowie = []

    def __init__(self,rspo,regon,sources):
        self.rspo = int(float(rspo.replace(' ','')))
        self.regon = regon
        self.wyniki = self._filter_by(sources['exam_data'],'RSPO')
        self.fin_raporty = self._filter_by(sources['financial_reports'], 'Regon')
        self.uczniowie = self._filter_by(sources['pupils_data'],'Numer RSPO')


    def _filter_by(self,data: pd.DataFrame,key_name):
        return data[data[key_name].astype(str) == str(self.regon if key_name.lower() == "regon" else self.rspo)]


    def print(self):
        print(self.rspo,self.regon)
        print(self.wyniki)
        print(self.fin_raporty)
        print(self.uczniowie)

