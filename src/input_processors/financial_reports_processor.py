import pandas as pd
from lxml import etree
import os


term_map_27s = {
    'pl': 'Planowane',
    'na': 'Należności',
    'po': 'Potrącenia',
    'dw': 'Dochody Wykonane',
    'no': 'Należności pozostałe do zapłaty ogółem',
    'nz': 'Należne zaległości netto',
    'np': 'Nadpłaty',
    'so': 'Skutki obniżenia górnych stawek podatków obliczone za okres sprawozdawczy',
    'su': 'Skutki udzielonych ulg i zwolnień obliczone za okres sprawozdawczy',
    'uz': 'Umożenie zaległości podatkowych',
    'ot': 'Rozłożenie na raty, odłożenie terminu płatności, zwolnienie z obowiązku pobrania, ograniczenie poboru',
}

term_map_28s = {
    'pl': 'Plan',
    'za': 'Zaangażowanie',
    'ww': 'Wydatki wykonane',
    'zo': 'Zobowiązania ogółem',
    'zw': '',
    'wn': '',
    'lu': '',
    'rb': '',
    'wfs': 'Wydatki zrealizowane w ramach funduszu sołeckiego',
}

def _xml_to_record(input_data: str):
    reports = []
    root = etree.fromstring(input_data)
    jednostki = root.find(".//Jednostki")

    for unit in jednostki:
        sprawozdania = unit.find(".//Sprawozdania")
        for sprawozdanie in sprawozdania:
            report_type = sprawozdanie.tag
            report_id = sprawozdanie.attrib["Id"]
            okres = sprawozdanie.find(".//Okres")
            report_year = okres.find(".//Rok").text
            report_period_type = okres.find(".//TypOkresu").text
            report_period = okres.find(".//Okres").text

            unit = sprawozdania.find(".//Jednostka")
            unit_data = {}

            for field in unit:
                unit_data[field.tag] = field.text

            header = sprawozdanie.find(".//Naglowek")
            header_version = header.find(".//Wersja").text
            header_date = header.find(".//DataSprawozdania").text

            pozycje = sprawozdanie.find(".//Pozycje")

            for pozycja in pozycje:
                pozycja_data = {}
                for field in pozycja:
                    pozycja_data[field.tag] = field.text

                report = {
                    "report_type": report_type,
                    "report_id": report_id,
                    "report_year": report_year,
                    "report_period_type": report_period_type,
                    "report_period": report_period,
                    "header_version": header_version,
                    "header_date": header_date,
                }

                # add unit data
                for key, val in unit_data.items():
                    report[key] = val

                # add pozycja data
                for key, val in pozycja_data.items():
                    report[key] = val

                reports.append(report)
    return reports


def process_files_in_directory(dirname: str) -> pd.DataFrame:
    reports = []
    for filename in os.listdir(dirname):
        if filename.startswith("Sprawozdania"):
            with open("../Kutno_HackSQL/" + filename, "r") as f:
                input_data = f.read()
                reports += _xml_to_record(input_data)

    dataframe = pd.DataFrame.from_records(reports)
    return dataframe
