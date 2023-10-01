import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QTextEdit,
    QLabel,
    QGridLayout,
)

import input_processors.sio_reports_processor as srp
import input_processors.financial_reports_processor as frp
import input_processors.exam_result_processor as erp
from school import School

import finance.fin_proc as fp


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

    def text(self):
        return self.text_edit.toPlainText()


class SchoolRecord(QWidget):
    def __init__(self, school):
        super().__init__()

        self.label1 = QLabel(school.school_name)
        self.label1.setText(school.school_name)

        self.label2 = QLabel("Regon: " + school.regon)
        self.label2.setText("Regon: " + school.regon)

        spending_per_pupil = "{:.2f}PLN".format(school.get_spending_per_pupil(2022))
        self.label3 = QLabel("Spending per pupil: " + spending_per_pupil)
        self.label3.setText("Spending per pupil:" + spending_per_pupil)

        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(self.label1, 0, 0, 1, 3)
        layout.addWidget(self.label2, 0, 3, 1, 2)
        layout.addWidget(self.label3, 0, 5, 1, 2)


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.all_schools = []
        self.current_schools = []
        self.init_schools()
        self.setup()

    def setup(self):
        self.resize(1900, 800)
        self.move(300, 100)
        self.setWindowTitle("")

        layout = QHBoxLayout()
        self.setLayout(layout)

        left_menu = self.left_page()
        layout.addWidget(left_menu)
        left_menu.setFixedSize(300, 800)

        self.right_page = self.right_page()
        layout.addWidget(self.right_page)
        self.right_page.setFixedSize(1500, 800)

        self.show()

    def right_page(self):
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)

        for school in self.current_schools:
            school_widget = SchoolRecord(school)
            layout.addWidget(school_widget)

        return widget

    def left_page(self):
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)

        self.widget1 = TextInput("Nazwa szkoły", "Wpisz nazwę szkoły")
        layout.addWidget(self.widget1)

        self.widget2 = TextInput("REGON", "Wpisz REGON")
        layout.addWidget(self.widget2)

        self.widget3 = TextInput("Minimalna liczba uczniów", "20")
        layout.addWidget(self.widget3)

        self.widget4 = TextInput("Maksymalna liczba uczniów", "1000")
        layout.addWidget(self.widget4)

        submit_button = QPushButton("Wyszukaj")
        submit_button.setFixedHeight(30)
        submit_button.clicked.connect(self.filter_schools)
        layout.addWidget(submit_button)

        return widget

    def init_schools(self):
        data = {
            "pupils_data": srp.process_files_in_directory("../Kutno_HackSQL"),
            "exam_data": erp.process_files_in_directory("../Kutno_HackSQL"),
            "financial_reports": frp.process_files_in_directory("../Kutno_HackSQL"),
        }
        self.all_schools = []
        self.current_schools = []
        for indc in data["pupils_data"].index:
            rspo = data["pupils_data"]["Numer RSPO"][indc]
            regon = data["pupils_data"]["REGON"][indc]
            school = School(rspo, regon, data)
            self.all_schools.append(school)
            self.current_schools.append(school)

    def set_current_schools(self, schools):
        self.current_schools = schools
        self.update()

    def filter_schools(self):
        schools = self.all_schools.copy()
        if self.widget1.text() != "":
            schools = filter(lambda x: x.school_name == self.widget1.text(), schools)
        if self.widget2.text() != "":
            schools = filter(lambda x: x.regon == self.widget2.text(), schools)
        if self.widget3.text() != "":
            schools = filter(
                lambda x: x.get_total_pupils_for_year(2022) >= int(self.widget3.text()),
                schools,
            )
        if self.widget4.text() != "":
            schools = filter(
                lambda x: x.get_total_pupils_for_year(2022) <= int(self.widget4.text()),
                schools,
            )
        self.current_schools = schools

        layout = QVBoxLayout()
        QWidget().setLayout(self.right_page.layout())
        self.right_page.setLayout(layout)

        for school in self.current_schools:
            school_widget = SchoolRecord(school)
            layout.addWidget(school_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyApp()
    sys.exit(app.exec_())
