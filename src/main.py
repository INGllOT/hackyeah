import input_processors.financial_reports_processor as frp

df = frp.process_files_in_directory('../Kutno_HackSQL')
print(df)