import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout

import input_processors.sio_reports_processor as srp
import input_processors.financial_reports_processor as frp
import input_processors.exam_result_processor as erp
from school import School

import finance.fin_proc as fp

def do():
    data = {
    'pupils_data': srp.load_sio_pupils('../Kutno_HackSQL/SIO 30.09.2021.csv'),
    'exam_data': erp.load_exam('../Kutno_HackSQL/Wyniki_E8_szkoly_2023.xlsx'),
    'financial_reports': frp.process_files_in_directory('../Kutno_HackSQL')}

    schools = []
    for indc in data['pupils_data'].index:
        rspo = data['pupils_data']['Numer RSPO'][indc]
        regon = data['pupils_data']['REGON'][indc]
        school = School(rspo,regon,data)
        schools.append(school)


    schools[0].print()

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    w = QWidget()    
    layout = QHBoxLayout()

    left_layout = QVBoxLayout()
    right_layout = QVBoxLayout()

    do()

    btn = QPushButton("Hello World!")
    layout.addWidget(btn)
    w.setLayout(layout)
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    sys.exit(app.exec_())

# print(financial_reports)
# dp = fp.get_dochodowe_paragraphs()
# wp = fp.get_wydatkowe_paragraphs()

# print(set(dp.keys()).intersection(set(wp.keys())))

# print(dp['256'])
# print(wp['256'])