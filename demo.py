#encoding=utf-8
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush, QScreen, QGuiApplication, QPainter, QColor, QBrush
from PyQt5.QtCore import QRect, QTimer


class Demo(QWidget):
	def __init__(self):
		super(Demo, self).__init__()

		self.initUI()

	def initUI(self):
		self.height, self.speed = 0, 20
		width, height = 600, 800
		demoSize = self.centerRect(width, height)
		self.setGeometry(demoSize)
		self.setWindowTitle('Demo')
		self.show()

		#初始化timer
		timer = QTimer(self)
		timer.timeout.connect(self.update)
		timer.start(100)

	#计算出合适的尺寸
	def centerRect(self, width, height):
		screen = QGuiApplication.primaryScreen()

		screenWidth = screen.geometry().width()
		screenHeight = screen.geometry().height()
		
		centerWidth, centerHeight = screenWidth // 2, screenHeight // 2 
	
		startWidth, startHeight = centerWidth - width // 2, centerHeight - height // 2

		return QRect(startWidth, startHeight, width, height)

	def paintEvent(self, event):
		self.height += self.speed
		if self.height >= 750:
			self.height = 0

		qp = QPainter()
		qp.begin(self)
		qp.setPen(QColor(100, 10, 10))
		qp.setBrush(QColor(200, 100, 100))
		qp.drawRect(275, self.height, 40, 40)
		qp.end()
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Demo()
	sys.exit(app.exec_())
