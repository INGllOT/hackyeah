import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QTextEdit,
    QLabel,
)

import input_processors.sio_reports_processor as srp
import input_processors.financial_reports_processor as frp
import input_processors.exam_result_processor as erp
from school import School

import finance.fin_proc as fp


def on_submit():
    print("submit")
    data = {
        "pupils_data": srp.load_sio_pupils("../Kutno_HackSQL/SIO 30.09.2021.csv"),
        "exam_data": erp.load_exam("../Kutno_HackSQL/Wyniki_E8_szkoly_2023.xlsx"),
        "financial_reports": frp.process_files_in_directory("../Kutno_HackSQL"),
    }

    schools = []
    for indc in data["pupils_data"].index:
        rspo = data["pupils_data"]["Numer RSPO"][indc]
        regon = data["pupils_data"]["REGON"][indc]
        school = School(rspo, regon, data)
        schools.append(school)

    print("submit end")


class TextInput(QWidget):
    def __init__(self, label_text, placeholder_text):
        super().__init__()

        self.label = QLabel(label_text)
        self.label.setText(label_text)

        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText(placeholder_text)
        self.text_edit.setFixedHeight(30)

        layout = QHBoxLayout()
        self.setLayout(layout)

        layout.addWidget(self.label)
        layout.addWidget(self.text_edit)


class SchoolRecord(QWidget):
    def __init__(self, school):
        super().__init__()

        self.label = QLabel(school.name)
        self.label.setText(school.name)

        self.label = QLabel(school.regon)
        self.label.setText(school.regon)

        layout = QHBoxLayout()
        self.setLayout(layout)

        layout.addWidget(self.label)
        layout.addWidget(self.text_edit)


def left_menu_def():
    widget = QWidget()
    layout = QVBoxLayout()
    widget.setLayout(layout)

    widget1 = TextInput("Nazwa szkoły", "Wpisz nazwę szkoły")
    layout.addWidget(widget1)

    widget2 = TextInput("REGON", "Wpisz REGON")
    layout.addWidget(widget2)

    widget3 = TextInput("Minimalna liczba uczniów", "20")
    layout.addWidget(widget3)

    widget4 = TextInput("Maksymalna liczba uczniów", "1000")
    layout.addWidget(widget4)

    submit_button = QPushButton("Wyślij")
    submit_button.setFixedHeight(30)
    layout.addWidget(submit_button)
    submit_button.clicked.connect(on_submit)

    return widget


def right_page_def():
    widget = QWidget()
    layout = QVBoxLayout()
    widget.setLayout(layout)

    return widget


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(1200, 800)
    w.move(300, 100)
    w.setWindowTitle("")

    layout = QHBoxLayout()
    w.setLayout(layout)

    left_menu = left_menu_def()
    layout.addWidget(left_menu)
    left_menu.setFixedSize(300, 800)

    right_page = right_page_def()
    layout.addWidget(right_page)
    right_page.setFixedSize(900, 800)

    # btn = QPushButton("Hello World!")
    # layout.addWidget(btn)

    w.show()
    sys.exit(app.exec_())


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        pass
