#encoding=utf-8
import sys
from config import *
from box import *
from board import *

from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QLCDNumber, QPushButton
from PyQt5.QtGui import QPainter, QColor, QBrush, QScreen, QGuiApplication, QPalette
from PyQt5.QtCore import QRect, QTimer, Qt


class Tetrixs(QWidget):
    def __init__(self):
        super(Tetrixs, self).__init__()
        self.initUI()

    def initUI(self):
        #窗口大小固定
        size = self.centerRect(tetrixsWidth, tetrixsHeight)
        self.setGeometry(size)
        self.setWindowTitle('Tetrixs')

        #设置背景色
        self.setStyleSheet(mainWindowColor)


        #LCD和Button
        self.levelNumber = QLCDNumber(self)
        self.scoreNumber = QLCDNumber(self)

        #设置初始值
        self.levelNumber.display(0)
        self.scoreNumber.display(0)

        self.pauseButton = QPushButton('PAUSE', self)
        self.startButton = QPushButton('START', self)

        #设置两个按钮无焦点
        self.pauseButton.setFocusPolicy(Qt.NoFocus)
        self.startButton.setFocusPolicy(Qt.NoFocus)

        #self.setFocusPolicy(Qt.StrongFocus)
        #self.startButton.set

        self.levelNumber.setFixedSize(150, 100)
        self.scoreNumber.setFixedSize(150, 100)
        self.pauseButton.setFixedSize(150, 100)
        self.startButton.setFixedSize(150, 100)

        self.levelNumber.setStyleSheet(lcdNumberColor)
        self.scoreNumber.setStyleSheet(lcdNumberColor)
        self.pauseButton.setStyleSheet(buttonColor)
        self.startButton.setStyleSheet(buttonColor)

        ##LCD和Button绑定action函数
        self.startButton.clicked.connect(self.startButtonAction)
        self.pauseButton.clicked.connect(self.pauseButtonAction)


        vLayout = QVBoxLayout()
        vLayout.addWidget(self.levelNumber)
        vLayout.addWidget(self.scoreNumber)
        vLayout.addWidget(self.pauseButton)
        vLayout.addWidget(self.startButton)

         #画布
        self.canvas = Canvas()
        self.canvas.setFixedSize(500, 800)

        self.canvas.getScoreSignal.connect(self.getScoreAction)
        self.canvas.gameOverSignal.connect(self.gameOverAction)

        hLayout = QHBoxLayout()
        hLayout.addWidget(self.canvas)
        hLayout.addLayout(vLayout)
        
        self.setLayout(hLayout)
        self.setFixedSize(tetrixsWidth, tetrixsHeight)
        self.show()

    def centerRect(self, width, height):
        screen = QGuiApplication.primaryScreen()
        screenWidth = screen.geometry().width()
        screenHeight = screen.geometry().height()
        centerWidth, centerHeight = screenWidth // 2, screenHeight // 2
        startWidth, startHeight = centerWidth - width // 2, centerHeight - height // 2

        return QRect(startWidth , startHeight, width, height)  

    def keyPressEvent(self, event):
        #向左旋转
        if event.key() == Qt.Key_Up:
            self.canvas.rotateLeft()

        #向右旋转
        if event.key() == Qt.Key_Down:
            self.canvas.rotateRight()

        #向左移动
        if event.key() == Qt.Key_Left:
            self.canvas.moveLeft()
            

        #向右移动
        if event.key() == Qt.Key_Right:
            self.canvas.moveRight()

        if event.key() == Qt.Key_Space:
            self.canvas.downDirect()
            

    def startButtonAction(self):
        #设置初始值
        self.levelNumber.display(0)
        self.scoreNumber.display(0)

        self.canvas.start()

    def pauseButtonAction(self):
        self.canvas.pause()
        if self.pauseButton.text() == "PAUSE":
            self.pauseButton.setText("CONTINUE")
        else:
            self.pauseButton.setText("PAUSE")


    def getScoreAction(self, score):

        QApplication.beep()

        value = self.scoreNumber.intValue()

        newValue = value + score

        self.scoreNumber.display(newValue)

        #更新speed
        if value / levelStep != newValue / levelStep:
            self.levelNumber.display(newValue / levelStep)
            self.canvas.speed *= percent

    def gameOverAction(self):
        self.msg()

    def msg(self):
        reply = QMessageBox.information(self, "Tetrixs", "GameOver", QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.canvas.start()

        if reply == QMessageBox.No:
            app = QApplication(sys.argv)
            app.exit(0)

         

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tetrixs = Tetrixs()
    sys.exit(app.exec_())