import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle("나는 윈도우야.")
w.setWindowIcon(QIcon('web.png'))
w.setGeometry(1000, 300, 300, 300) 
'''앞의 두 개의 값은 윈도우 위치값, 나머지는 창의 크기'''
 
btn = QPushButton('나를 눌러요...', w)
btn.move(50, 50)
btn.clicked.connect(QCoreApplication.instance().quit)


        
w.show()
app.exec()