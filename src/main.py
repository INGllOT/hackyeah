import input_processors.financial_reports_processor as frp
import input_processors.read_SIO as rs

df = frp.process_files_in_directory('../Kutno_HackSQL')
# print(df[["Dzial","Rozdzial", "Paragraf"]].drop_duplicates())
print(df)

print(rs.load_sio_pupils('../Kutno_HackSQL/SIO 30.09.2021.csv'))