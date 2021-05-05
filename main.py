#импорт библиотек и модулей
import sys
from PySide2.QtWidgets import QApplication
from WndMain import WndMain

#создание приложения pyside
app = QApplication(sys.argv)

#main_window создание
main_window = WndMain()

app.exec_()
