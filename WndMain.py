from PySide2.QtWidgets import QLabel, QMainWindow, QMessageBox
from PySide2.QtWidgets import QListWidget
from PySide2.QtGui import Qt


class WndMain():
  #функция label_close_wnd.mouseMoveEvent
  def mouse_on_label_close_wnd(self, event):
    self.label_close_wnd.setStyleSheet(" \
    color: white; \
    font-size: 25px; \
    background-color: rgba(0, 0, 0, 0.1); \
    ")
    
  #функция wnd_main.mouseMoveEvent
  def mouse_on_wnd_main (self, event):
    self.label_close_wnd.setStyleSheet(" \
    color: blue; \
    font-size: 25px; \
    background-color: rgba(0, 0, 0, 0.1); \
    ")

  def __init__(self):
    #создание виджетов
    self.wnd_main = QMainWindow()
    self.list_theme = QListWidget(self.wnd_main)
    self.label_close_wnd = QLabel(self.wnd_main)

    #настройки поумолчанию wnd_main 
    self.wnd_main.setWindowTitle("Lite Note")
    self.wnd_main.setFixedSize (1300, 850)
    self.wnd_main.setWindowFlag (Qt.FramelessWindowHint)
    self.wnd_main.setStyleSheet(" \
    QMainWindow { \
    background-color: black; \
    background-image: url(./193342.jpg); \
    }") 
    self.wnd_main.setMouseTracking(True)
    self.wnd_main.mouseMoveEvent = self.mouse_on_wnd_main

    #настройки list_theme QListWidget
    self.list_theme.setGeometry(5, 50, 160, 650)
    self.list_theme.addItem("Item1")
    self.list_theme.setStyleSheet(" \
    color: white; \
    font-size: 25px; \
    background-color: rgba(0, 0, 0, 0.5); \
    ") 

    #label_close_wnd QLabel
    self.label_close_wnd.setText("X")
    self.label_close_wnd.setGeometry(1200, 25, 18, 20)
    self.label_close_wnd.setStyleSheet(" \
    color: blue; \
    font-size: 25px; \
    background-color: rgba(0, 0, 0, 0.1); \
    ") 
    self.label_close_wnd.setMouseTracking(True)
    self.label_close_wnd.mouseMoveEvent = self.mouse_on_label_close_wnd
    
    #вывод окна на экран
    self.wnd_main.show()

  
