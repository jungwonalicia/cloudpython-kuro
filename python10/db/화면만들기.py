import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle("나는 윈도우야.")
w.setWindowIcon(QIcon('web.png'))
w.setGeometry(1000, 300, 300, 300) 
'''앞의 두 개의 값은 윈도우 위치값, 나머지는 창의 크기''' 
w.show()
app.exec()