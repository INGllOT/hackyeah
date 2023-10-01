import math
import pandas as pd
from input_processors.sio_reports_processor import weights


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
        self.school_name = self.uczniowie['Nazwa szkoły/placówki'].iloc[0]
        
        # print(list(self.uczniowie.columns))


    def _filter_by(self,data: pd.DataFrame,key_name):
        return data[data[key_name].astype(str) == str(self.regon if key_name.lower() == "regon" else self.rspo)]

    def get_spending_per_pupil(self,year):
        total_spent = self._get_spending_for_year(year)
        total_pupils = self._get_total_pupils_for_year(year)
        print(total_spent/total_pupils)

    def _get_spending_for_year(self,year):
        data = self.fin_raporty[self.fin_raporty['report_type'] == "Rb-28s"]
        data = data[((data['report_year'] == str(year)) & (data['report_period'].astype(int) > 2)) | ((data['report_year'] == str(year+1)) & (data['report_period'].astype(int) <= 2))]
        sum = 0.0
        for x in data['WW']:
            x=float(x)
            if(not math.isnan(x)):
                sum += float(x)
        return sum

    def _get_total_pupils_for_year(self,year):
        data = self.uczniowie[self.uczniowie['Year'] == year]
        sum = 0.0
        for key,value in weights.items():
            if(key in data):
                sum += float(data[key].iloc[0]) * value
        return(sum)

    def print(self):
        print(self.rspo,self.regon)
        print(self.wyniki)
        print(self.fin_raporty)
        print(self.uczniowie)

