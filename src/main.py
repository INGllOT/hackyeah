import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

import input_processors.read_SIO as rs
import input_processors.financial_reports_processor as frp

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    w = QWidget()    
    layout = QHBoxLayout()
    btn = QPushButton("Hello World!")
    layout.addWidget(btn)
    w.setLayout(layout)
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    sys.exit(app.exec_())