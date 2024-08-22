from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QMessageBox, QRadioButton

#class Widgets():
 #   def __init___()
app = QApplication([])
main_win = QWidget()

def win():
    victory_win = QMessageBox()
    victory_win.setText("Вірно\nВи не виграли золотий ділдо")
    victory_win.exec_()

def loose():
    victory_win2 = QMessageBox()
    victory_win2.setText("Не Вірно\nВи не виграли золотий ділдо")    
    victory_win2.exec_()

label = QLabel("Якого року канал отримав 'Золоту кнопку' від YouTube?")
btn_answer = QRadioButton("2001")
btn_answer2 = QRadioButton("1945")
btn_answer3 = QRadioButton("1488")
btn_answer4 = QRadioButton("2015")

layout = QVBoxLayout()
layout1 = QHBoxLayout()
layout2 = QHBoxLayout()
layout3 = QHBoxLayout()

main_win.resize(400, 200)


layout1.addWidget(btn_answer, alignment= Qt.AlignCenter)
layout1.addWidget(btn_answer2, alignment= Qt.AlignCenter)
layout3.addWidget(label, alignment= Qt.AlignCenter)
layout2.addWidget(btn_answer3, alignment= Qt.AlignCenter)
layout2.addWidget(btn_answer4, alignment= Qt.AlignCenter)
layout.addLayout(layout1)
layout.addLayout(layout2)
layout.addLayout(layout3)

main_win.setLayout(layout)
btn_answer.clicked.connect(loose)
btn_answer2.clicked.connect(loose)
btn_answer3.clicked.connect(loose)
btn_answer4.clicked.connect(win)


main_win.show() 
app.exec_()