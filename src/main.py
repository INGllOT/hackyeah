import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QTextEdit, QLabel

import input_processors.sio_reports_processor as srp
import input_processors.financial_reports_processor as frp

pupils = srp.load_sio_pupils("../Kutno_HackSQL/SIO 30.09.2021.csv")
financial_reports = frp.process_files_in_directory("../Kutno_HackSQL")

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


def left_menu_def():
    widget = QWidget()
    layout = QVBoxLayout()
    widget.setLayout(layout)

    widget1 = TextInput("Nazwa szkoły", "Wpisz nazwę szkoły")
    layout.addWidget(widget1)

    widget2 = TextInput("REGON", "Wpisz REGON")
    layout.addWidget(widget2)

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

    right_page = QWidget()
    layout.addWidget(right_page)
    right_page.setFixedSize(900, 800)

    # btn = QPushButton("Hello World!")
    # layout.addWidget(btn)

    w.show()
    sys.exit(app.exec_())


# print(financial_reports)
# dp = fp.get_dochodowe_paragraphs()
# wp = fp.get_wydatkowe_paragraphs()

# print(set(dp.keys()).intersection(set(wp.keys())))

# print(dp['256'])
# print(wp['256'])
