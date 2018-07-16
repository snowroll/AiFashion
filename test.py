from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie

from Widget import Ui_Form
import cv2

class Widget(QWidget, Ui_Form):
    def __init__(self, *args, **kwargs):
        super(Widget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.timer_camera = QTimer(self)
        self.cap = cv2.VideoCapture(0)
        self.timer_camera.timeout.connect(self.show_pic)
        self.timer_camera.start(10)

        self.setIcon()
        self.show()

    def show_pic(self):
        success, frame=self.cap.read()
        if success:
            show = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
            self.label.setPixmap(QPixmap.fromImage(showImage))
        self.timer_camera.start(10)      
    
    def setIcon(self):  #设置背景图片和程序的图标
        palette1 = QPalette()
        # palette1.setColor(self.backgroundRole(), QColor(192,253,123))   # 设置背景颜色
        palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('source/tech.jpg')))   # 设置背景图片
        self.setPalette(palette1)
        # self.setAutoFillBackground(True) # 不设置也可以

        # self.setGeometry(300, 300, 250, 150)
        self.setWindowIcon(QIcon('source/logo.png'))    

if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Image")

    window = Widget()
    app.exec_()
