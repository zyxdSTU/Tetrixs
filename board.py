#encoding=utf-8
from config import *
from box import *

from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtGui import QPainter, QPalette
from PyQt5.QtCore import QRect, QTimer, QElapsedTimer,pyqtSignal,pyqtSlot
import random

class Canvas(QWidget):

    #得分信号
    getScoreSignal = pyqtSignal(int)
    gameOverSignal = pyqtSignal()

    def __init__(self):
        super(Canvas, self).__init__()
        #初始化画布
        self.board = [[0 for i in range(canvasWidth)] for i in range(canvasHeight)]
        self.box = None    

        #初始化定时器
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.down)

        #初始化速度
        self.speed = speed

    def paintEvent(self, event):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                    self.drawBlock(i, j, self.board[i][j])

        if self.box != None:
            for element in self.box.getPosition():
                self.drawBlock(element[0], element[1], self.box.color)


    def drawBlock(self, i, j, shapeIndex):

        painter = QPainter()

        painter.begin(self)

        painter.setBrush(BoxColor[shapeIndex])

        height, width = blockSize*i, blockSize*j

        painter.drawRect(width + margin, height+margin, blockSize, blockSize)

        painter.end()

    #判断坐标是否越界
    def bound(self,x, y):
        if x < 0 or x >= canvasHeight:
            return False

        if y < 0 or y >= canvasWidth:
            return False

        if self.board[x][y] != 0:
            return False

        return True

    #判断方块操作的可行性    
    def jungle(self, action):
        #关于方块的操作
        pos = self.box.getPosition()
 
        if action == actionPosition:
            for element in pos:
                if not self.bound(element[0], element[1]):
                    return False
            return True
                
        if action == actionLeft:
            for element in pos:
                if not self.bound(element[0], element[1]-1):
                    return False
            return True

        if action == actionRight:
            for element in pos:
                if not self.bound(element[0], element[1]+1):
                    return False
            return True

        if action == actionDown:
            for element in pos:
                if not self.bound(element[0]+1, element[1]):
                    return False
            return True

        if action == actionRotateLeft:
            posRotateLeft = self.box.getRotateLeftPosition()
            for element in posRotateLeft:
                if not self.bound(element[0], element[1]):
                    return False
            return True

        
        if action == actionRotateRight:
            posRotateRight = self.box.getRotateRightPosition()
            for element in posRotateRight:
                if not self.bound(element[0], element[1]):
                    return False
            return True


    def nextBox(self):
        number = random.randint(1, 7)
        if number == I:
            return IBox()
        if number == leftL:
            return LeftLBox()
        if number == rightL:
            return RightLBox()
        if number == square:
            return SquareBox()
        if number == leftZ:
            return LeftZBox()
        if number == T:
            return TBox()
        if number == rightZ:
            return RightZBox()

    #方块向左旋转
    def rotateLeft(self):
        if self.jungle(actionRotateLeft):
            #print self.box.getPosition()
            self.box.rotateLeft()
            self.update()

    #方块向右旋转
    def rotateRight(self):
        if self.jungle(actionRotateRight):
            #print self.box.getPosition()
            self.box.rotateRight()

            self.update()

    #方块向左移动
    def moveLeft(self):
        if self.jungle(actionLeft):
            self.box.moveLeft()
            self.update()
    
    #方块向右移动
    def moveRight(self):
        if self.jungle(actionRight):
            self.box.moveRight()
            self.update()

    #方块下落
    def down(self):
        if self.jungle(actionDown):
            self.box.down()
            self.update()
        else:
            self.dispose()

    #处理下落后的方块
    def dispose(self):
        #存储box
        self.saveBox()

        #是否右消行
        score = self.getScore()

        if score > 0:
            #添加提示音，设置分数值
            self.getScoreSignal.emit(score)
       
        self.box = self.nextBox()

        if self.jungle(actionPosition) == False:
            self.timer.stop()
            self.box = None
            self.board = [[0 for i in range(canvasWidth)] for i in range(canvasHeight)]
            self.update()
            self.gameOverSignal.emit()

        else: self.update()


    def downDirect(self):
        while True:
            if self.jungle(actionDown):
                self.down()
            else:
                self.dispose()
                break

    #存储下落的方块
    def saveBox(self):
        pos = self.box.getPosition()
        for element in pos:
            self.board[element[0]][element[1]] = self.box.color

    #更新board
    def getScore(self):
        #内嵌函数
        def ok(List):
            for element in List:
                if element == 0:
                    return True
            return False

        self.board = [x for x in self.board if ok(x)]

        score = canvasHeight - len(self.board)

        for i in range(score):
            self.board.insert(0, [0 for j in range(canvasWidth)])

        return score

    def start(self):
        self.box = self.nextBox()
        self.update()

        #设置初始速度, 开启定时器
        self.speed = speed
        self.timer.start(self.speed)

    def pause(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start()

    







